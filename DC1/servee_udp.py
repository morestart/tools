from socketserver import BaseRequestHandler, UDPServer
import time


class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        # Get message and client socket
        msg, sock = self.request
        resp = time.ctime()
        sock.sendto(resp.encode('ascii'), self.client_address)
        print(msg.decode("utf-8"))


if __name__ == '__main__':
    serv = UDPServer(('', 7550), TimeHandler)
    print("udp server is started...")
    serv.serve_forever()
