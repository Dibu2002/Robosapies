import socket
import cv2 as cv
import json

ports = [1238, 1239, 1240, 1241]
s = []
for i in range(1):
    s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    s[i].bind(('0.0.0.0', ports[i]))
    s[i].listen(0)

while True:
    for i in range(1):

        client, addr = s[i].accept()
        client.settimeout(200)

        with open('data.json', 'r') as file:
            data = file.read()
            y = json.loads(data)
            client.send(bytes(['func']))
        client.close()