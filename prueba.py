import cv2, time
import numpy as np
from juego import *


posicion_Inicial = 0 
video = cv2.VideoCapture(0)
amariBajo1 = np.array([25,70,120],np.uint8)
amariAlto1 = np.array([30,255,255],np.uint8)


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
def moverAzul(mascara,color):
    global posicion_Inicial
    contornos,_ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)         
    for c in contornos:
            are =cv2.contourArea(c)
            if are > 50:
                nvco = cv2.convexHull(c)
                cv2.drawContours(frame, [nvco], 0,color,2)
                x, y, _, _ = cv2.boundingRect(c) 
                if posicion_Inicial-x > 0:
                    move_leftBlue()
                if posicion_Inicial-x < 0:
                    move_rightBlue()
                posicion_Inicial = x 
def moveramarillo(mascara,color):
    global posicion_Inicial
    contornos,_ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)         
    for c in contornos:
            are =cv2.contourArea(c)
            if are > 50:
                nvco = cv2.convexHull(c)
                cv2.drawContours(frame, [nvco], 0,color,2)
                x, y, _, _ = cv2.boundingRect(c) 
                if posicion_Inicial-x > 0:
                    move_leftRed()
                if posicion_Inicial-x < 0:
                    move_rightRed()
                posicion_Inicial = x 
while (video.isOpened()):
    ret, frame = video.read()
    if ret == True:
        frameh = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mascara = cv2.inRange(frameh, ab, aa)
        maskRed1 = cv2.inRange(frameh,amariBajo1,amariAlto1)
        moverAzul(mascara,(255,0,0))
        moveramarillo(maskRed1,(0,0,255))
        cv2.imshow('sad',frame)
        interaccion()
    if (cv2.waitKey(1) & 0xFF == ord('s')):
        closeGame("JUEGO TERMINADO")
