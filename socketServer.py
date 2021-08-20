import socket
import cv2 as cv
import time

ports = [2004, 2005, 2002, 2003]
s = []
for i in range(2):
    s.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
    s[i].bind(('0.0.0.0', ports[i]))
    s[i].listen(0)

hello = [True, True, True, True]
while True:
    for i in range(2):
        client, addr = s[i].accept()
        client.settimeout(200)
        if hello[i]:
            client.send(b'H')
            hello[i] = False
        else:
            client.send(b'L')
            hello[i] = True
        client.close()