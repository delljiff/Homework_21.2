from http.server import BaseHTTPRequestHandler, HTTPServer


class ContactServer(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith(".css"):
            css_path = self.path.lstrip("/").replace("../", "")

            try:
                with open(css_path, "r", encoding="utf-8") as file:
                    css_content = file.read()

                self.send_response(200)
                self.send_header("Content-type", "text/css; charset=utf-8")
                self.end_headers()
                self.wfile.write(css_content.encode("utf-8"))
                return
            except FileNotFoundError:
                pass
        with open("src/contacts.html", "r", encoding="utf-8") as file:
            html_content = file.read()

        self.send_response(200)

        self.send_header("Content-type", "text/html; charset=utf-8")

        self.end_headers()

        self.wfile.write(html_content.encode("utf-8"))


if __name__ == "__main__":
    hostname = "localhost"
    port = 8000

    server = HTTPServer((hostname, port), ContactServer)
    print(f"Сервер запущен: http://{hostname}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nСервер остановлен")
        server.server_close()
