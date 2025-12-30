import socket
import threading
from datetime import datetime

class Server:
    HOST=""
    IP=""
    PORT=0
    MAX_BYTE=0
    def __init__(self,host="127.0.0.1", port=8890, max_byte=1024):
        self.HOST=host
        self.PORT = port
        self.MAX_BYTE = max_byte

        self.server_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_manager.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.server_manager.bind((self.HOST, self.PORT))
       
        self.server_manager.listen(5)

        print(f"[{datetime.now()}] >> Server Listening... {self.server_manager.getsockname()[0]}:{self.PORT}")

    def handle_client(self, conn, addr):
        
        with conn:
            while True:
                data = conn.recv(self.MAX_BYTE)
                if not data:
                    break
                message = data.decode("utf-8") 
                print(f"[{datetime.now()}] >> Received from {addr} : {message}")
                conn.sendall(data)

    def start(self):
        while True:
            conn, addr = self.server_manager.accept()

            thread = threading.Thread(
                target=self.handle_client,
                args=(conn, addr),
                daemon=True
            )
            thread.start()


# Çalıştır
server = Server()
server.start()