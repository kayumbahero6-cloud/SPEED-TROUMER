import os, http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map={**http.server.SimpleHTTPRequestHandler.extensions_map,'.glb':'model/gltf-binary','.js':'text/javascript'}
    def end_headers(self):
        self.send_header('Cache-Control','public, max-age=3600'); super().end_headers()
port=int(os.environ.get('PORT',8000))
socketserver.ThreadingTCPServer.allow_reuse_address=True
with socketserver.ThreadingTCPServer(('',port),H) as s:
    print('Speed Crisis on port',port); s.serve_forever()
