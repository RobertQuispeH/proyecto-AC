import cv2, time
import numpy as np
from juego import *


posicion_Inicial = 0 
video = cv2.VideoCapture(0)
ab = np.array([100,100,23],np.uint8)
aa = np.array([125,255,255],np.uint8)
def closeGame(fin):
    video.release()
    cv2.destroyAllWindows()
    wn.clear()
    turtle.write(fin, move=False, align="center", font=("Arial",24,"normal"))
    time.sleep(3)
    wn._delete("all")
    exit()

while (video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        frameh = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mascara = cv2.inRange(frameh, ab, aa)
        contornos,_ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for c in contornos:
            are =cv2.contourArea(c)
            if are > 50:
                nvco = cv2.convexHull(c)
                cv2.drawContours(frame, [nvco], 0, (255,0,0),2)
                x, y, _, _ = cv2.boundingRect(c) 
                if posicion_Inicial-x > 0:
                    move_left()
                if posicion_Inicial-x < 0:
                    move_right()
                posicion_Inicial = x          
        cv2.imshow('sad',frame)
        interaccion()
    if (cv2.waitKey(1) & 0xFF == ord('s')):
        closeGame("JUEGO TERMINADO")

