// Bateria de casos de borde del Modelo IDA.
//
// COMO SE CORRE: abrir el sitio, consola del navegador, pegar este archivo
// entero. Devuelve "fallas: ninguna" si el motor coincide con las formulas.
//
// POR QUE EN EL NAVEGADOR Y NO EN NODE: el motor vive en index.html y usa el
// DOM. Reimplementarlo aparte para testearlo seria testear la copia, no el
// original -- que es justo el error que este proyecto trata de evitar.
//
// COMO SE DERIVAN LAS EXPECTATIVAS: la funcion esperado() de abajo NO copia el
// codigo del motor. Aplica las formulas tal como estan publicadas en la pestaña
// Formulas y en el README. Si el motor y las formulas no dicen lo mismo, la
// prueba falla -- que es exactamente lo que se quiere detectar.
(function () {
  const $ = id => document.getElementById(id);
  const put = (id, v) => { const e = $(id); if (!e) throw new Error('falta #' + id); e.value = v; e.dispatchEvent(new Event('input', { bubbles: true })); };
  const radios = [...document.querySelectorAll('#arq input[type=radio]')];
  const chks = [...document.querySelectorAll('#arq input[type=checkbox]')];
  const fire = e => e.dispatchEvent(new Event('change', { bubbles: true }));
  const setLam = l => {
    const m = { 1.02: [2, 0, 0], 1.10: [1, 0, 0], 1.30: [0, 0, 0], 1.50: [0, 1, 0], 1.65: [0, 1, 1] }[l];
    if (!m) throw new Error('lambda no alcanzable con los agravantes: ' + l);
    radios[m[0]].checked = true; fire(radios[m[0]]);
    chks[0].checked = !!m[1]; fire(chks[0]);
    chks[1].checked = !!m[2]; fire(chks[1]);
  };

  // ---- Las formulas, tal como estan publicadas ----
  function esperado(c) {
    const H = c.P * c.hp;
    const aef = (c.a / 100) * (1 - c.r / 100) * (c.eta / 100);
    const Pmin = Math.ceil(c.Hmin / c.hp);
    const Pf = Math.max(Math.ceil(c.P * (1 - aef)), Pmin);
    const lib = c.P - Pf;
    const S = lib * (c.N / c.P) - (c.ctHora * H * aef) * c.lam - c.M;
    const cob = Pmin > 0 ? Math.min(c.R / Pmin, 1) : 0;
    return {
      Pf, lib, S,
      pb: S > 0 ? c.I / S : Infinity,
      IDA: Math.min(aef * c.lam * (1 - cob * 0.7) * 100, 100),
      techo: S > 0 ? S * c.Tmax : 0
    };
  }

  const base = { P: 10, N: 16000, hp: 160, a: 60, r: 20, eta: 80, ctHora: 2, M: 500, I: 50000, Hmin: 640, R: 0, lam: 1.5, Tmax: 18 };
  const casos = [
    ['00 · valores por defecto', {}],
    ['01 · sin automatizacion', { a: 0 }],
    ['02 · todo requiere firma humana', { r: 100 }],
    ['03 · automatizacion total sin piso', { a: 100, r: 0, eta: 100, Hmin: 0 }],
    ['04 · piso igual a la plantilla', { Hmin: 1600 }],
    ['05 · piso MAYOR que la plantilla', { Hmin: 3200 }],
    ['06 · una sola persona', { P: 1, N: 1600, Hmin: 160 }],
    ['07 · mil personas', { P: 1000, N: 1600000, Hmin: 64000 }],
    ['08 · hora de IA mas cara que la humana', { ctHora: 20 }],
    ['09 · respaldo externo cubre el piso', { R: 4 }],
    ['10 · respaldo externo desbordado', { R: 999 }],
    ['11 · respaldo con piso cero', { Hmin: 0, R: 50 }],
    ['12 · sin inversion inicial', { I: 0 }],
    ['13 · sin costo de IA ni mantenimiento', { ctHora: 0, M: 0 }],
    ['14 · arquitectura mas robusta', { lam: 1.02 }],
    ['15 · arquitectura mas fragil', { lam: 1.65 }],
    ['16 · eficiencia minima', { eta: 50 }],
    ['17 · plazo de recupero minimo', { Tmax: 1 }],
    ['18 · plazo de recupero largo', { Tmax: 120 }],
    ['19 · jornada doble', { hp: 320, Hmin: 640 }],
  ];

  const money = t => t === '—' ? 0 : +t.replace(/[^0-9-]/g, '') * (t.trim().startsWith('-') ? 1 : 1);
  const fallas = [], tabla = [];

  casos.forEach(([nombre, ov]) => {
    const c = { ...base, ...ov };
    $('btn-reiniciar').click();
    setLam(c.lam);
    ['P', 'N', 'hp', 'Hmin', 'R', 'I', 'M', 'Tmax'].forEach(k => put(k, c[k]));
    ['a', 'r', 'eta'].forEach(k => put(k, c[k]));
    // ctHora se deriva de C_mes, asi que se carga ULTIMO: si no, el motor lo
    // recalcula con las horas viejas y el caso corre con otro costo.
    const horasIA = c.P * c.hp * (c.a / 100) * (1 - c.r / 100) * (c.eta / 100);
    put('CtMes', Math.round(c.ctHora * horasIA * 1000) / 1000);

    const e = esperado(c);
    const got = { Pf: +$('out_P').textContent, S: money($('out_S').textContent), IDA: +$('out_IDA').textContent };
    const dif = [];
    if (got.Pf !== e.Pf) dif.push(`P': motor ${got.Pf} vs formula ${e.Pf}`);
    if (Math.abs(got.S - Math.round(e.S)) > 1) dif.push(`S: motor ${got.S} vs formula ${Math.round(e.S)}`);
    if (Math.abs(got.IDA - Math.round(e.IDA)) > 1) dif.push(`IDA: motor ${got.IDA} vs formula ${Math.round(e.IDA)}`);
    if (dif.length) fallas.push(nombre + ' → ' + dif.join(' · '));
    tabla.push({ caso: nombre, "P'": got.Pf, ahorro: $('out_S').textContent, recupero: $('out_pb').textContent, IDA: got.IDA, techo: $('out_techo').textContent });
  });

  $('btn-reiniciar').click();
  console.table(tabla);
  return { casos: casos.length, fallas: fallas.length ? fallas : 'ninguna' };
})()
