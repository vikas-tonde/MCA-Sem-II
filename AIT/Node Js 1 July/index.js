const http = require('http');

http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end("FIrst Node program");
}).listen(8080, () => {
    console.log("Listening on port http://localhost:8080");
});