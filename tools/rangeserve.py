import http.server, os, re, socketserver, sys
ROOT=sys.argv[2] if len(sys.argv)>2 else '.'
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self,*a,**k): super().__init__(*a,directory=ROOT,**k)
    def log_message(self,*a): pass
    def do_GET(self):
        path=self.translate_path(self.path.split('?')[0])
        rng=self.headers.get('Range')
        if not rng or not os.path.isfile(path): return super().do_GET()
        size=os.path.getsize(path)
        m=re.match(r'bytes=(\d*)-(\d*)',rng)
        s,e=m.group(1),m.group(2)
        s=int(s) if s else 0
        e=int(e) if e else size-1
        e=min(e,size-1)
        self.send_response(206)
        self.send_header('Content-Type',self.guess_type(path))
        self.send_header('Accept-Ranges','bytes')
        self.send_header('Content-Range',f'bytes {s}-{e}/{size}')
        self.send_header('Content-Length',str(e-s+1))
        self.end_headers()
        with open(path,'rb') as f:
            f.seek(s); self.wfile.write(f.read(e-s+1))
    def end_headers(self):
        if 'Accept-Ranges' not in self._headers_buffer.__str__():
            self.send_header('Accept-Ranges','bytes')
        super().end_headers()
socketserver.ThreadingTCPServer.allow_reuse_address=True
with socketserver.ThreadingTCPServer(('127.0.0.1',int(sys.argv[1])),H) as httpd:
    httpd.serve_forever()
