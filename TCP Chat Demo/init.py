from client import ClientServer


client_server=ClientServer()
while client_server.connect():
    try:
        msg = input("message >> ")
        if msg.lower() == 'exit': break
        client_server.SendData(msg)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
        break

client_server.close()