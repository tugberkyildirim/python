import socket
from datetime import datetime

class ClientServer:
    def __init__(self, host="127.0.0.1", port=8890, max_byte=1024):
        self.HOST = host
        self.PORT = port
        self.MAX_BYTE = max_byte
        self.CLIENT = None

    def connect(self):
        try:
            if self.CLIENT: return True
            
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            
            result = client_socket.connect_ex((self.HOST, self.PORT))
            
            if result == 0:
                self.CLIENT = client_socket
                print(f"[{datetime.now()}] >> Connected | IP: {self.CLIENT.getsockname()[0]} PORT: {self.PORT}")
                return True
            else:
                print(f"[{datetime.now()}] >> Connection Error (Error Code): {result})")
                self.CLIENT = None
                return False
        except Exception as ex: 
            print(f"Kritik Hata: {ex}")
            self.CLIENT = None
            return False

    def SendData(self, data="This is test message."):
        try:
            if not self.CLIENT:
                print("Connection Error! Socket isn't connect.")
                return

            self.CLIENT.sendall(data.encode("utf-8"))
            
            response = self.CLIENT.recv(self.MAX_BYTE)
            if response:
                print(f"[{datetime.now()}] >> Server: {response.decode('utf-8')}")
        except Exception as ex:
            print("Data Sending Error " + str(ex))
            self.close()

    def close(self):
        if self.CLIENT:
            self.CLIENT.close()
            self.CLIENT = None
            print(f"[{datetime.now()}] >>Disconnected.")