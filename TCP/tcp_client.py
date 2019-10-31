import socket
import json
import time


data = ["forward"]

def send():
    for d in data:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.4.1', 8000))
        if d != "stop":
            content = {
                "action": d,
                "theLast": 0
            }
        else:
            content = {
                "action": d,
                "theLast": 1
            }
        content = json.dumps(content)

        s.send(content.encode())

        recv = s.recv(1024)
        print(recv)
        time.sleep(5)

while True:
    send()
    time.sleep(2)
    break

