const http=require('http'),fs=require('fs'),path=require('path');const root=process.cwd();
const mime={'.html':'text/html; charset=utf-8','.png':'image/png','.svg':'image/svg+xml','.gif':'image/gif'};
http.createServer((q,s)=>{let p=decodeURIComponent(q.url.split('?')[0]);if(p.endsWith('/'))p+='index.html';
const f=path.join(root,p);if(!fs.existsSync(f)){s.statusCode=404;return s.end('404');}
s.setHeader('Content-Type',mime[path.extname(f)]||'application/octet-stream');s.end(fs.readFileSync(f));})
.listen(8802,()=>console.log('8802'));setTimeout(()=>process.exit(0),480000);
