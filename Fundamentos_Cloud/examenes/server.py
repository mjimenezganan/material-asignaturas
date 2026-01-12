ALUMNO = "Nombre del Alumno"

from http.server import BaseHTTPRequestHandler, HTTPServer

class MiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        contenido = f"""
        <html>
            <head>
                <title>Práctica</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f9;
                        color: #333;
                        margin: 0;
                        padding: 0;
                    }}
                    .contenedor {{
                        max-width: 600px;
                        margin: 80px auto;
                        background: #ffffff;
                        padding: 20px 30px;
                        border-radius: 8px;
                        box-shadow: 0 2px 6px rgba(0,0,0,0.1);
                        text-align: center;
                    }}
                    h1 {{
                        color: #2c3e50;
                    }}
                    .nota {{
                        margin-top: 10px;
                        font-size: 0.9rem;
                        color: #666;
                    }}
                </style>
            </head>
            <body>
                <div class="contenedor">
                    <h1>Ésta es la práctica de {ALUMNO}</h1>
                    <p class="nota">Servidor HTTP sencillo en Python, escuchando en el puerto 8080.</p>
                </div>
            </body>
        </html>
        """
        contenido_bytes = contenido.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(contenido_bytes)))
        self.end_headers()
        self.wfile.write(contenido_bytes)

if __name__ == "__main__":
    puerto = 8080
    servidor = HTTPServer(("0.0.0.0", puerto), MiHandler)
    print(f"Servidor arrancado en http://localhost:{puerto}")
    servidor.serve_forever()

