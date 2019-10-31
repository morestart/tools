from socketserver import BaseRequestHandler, TCPServer
# import json


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        while True:
            msg = self.request.recv(1024)
            data = msg.decode('utf-8')
            # data = json.loads(data)
            print(data)
            if not msg:
                break
            self.request.send(bytes(msg))
            print(msg)


if __name__ == '__main__':
    print("waiting for connection..")
    serv = TCPServer(('', 8000), EchoHandler)
    serv.serve_forever()
