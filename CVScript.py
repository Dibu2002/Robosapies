import cv2
import numpy as np
import imutils
import json


def angle(a, b, c):
    ang = degrees(atan2(c[1] - b[1], c[0] - b[0]) - atan2(a[1] - b[1], a[0] - b[0]))
    return ang


def displacement(x, y, a, b):
    disp = abs(((x - a) ** 2 + (y - b) ** 2) ** (1 / 2))
    return disp

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(3, 640)
cap.set(4, 480)
ports = [1234, 2005, 2002, 2003]
s = []
px = 725
py = 100
fx = 1156 

while True:
    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([120, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        area = cv2.contourArea(c)
        if area > 100:
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(cx, " ", cy)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "blue", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (255, 255, 255), 3)
            h = min(100, (cy - py) // 2)
            h = str(max(0, h))
            h = '0'*(3-len(h)) + h
            # print(cy - py, h)

            if cy > py:
                dictionary = {'func': f'1010{h}{h}'}
                # dictionary = {'func': 'HLHL100100'}
            else:
                dictionary = {'func': '0000000000'}


            json_object = json.dumps(dictionary, indent=4)
            print(json_object)
            with open("data.json", "w") as file:
                file.write(json_object)


    cv2.imshow("result", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
cv2.destroyAllWindows()
