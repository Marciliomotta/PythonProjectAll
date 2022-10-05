import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import os
import PySimpleGUI as sg

def DeteccaoPupila(masked, img):
    ret, binaria = cv.threshold(masked, 30, 255, cv.THRESH_BINARY)

    binaria = np.array(binaria, dtype=np.uint8)

    kernel = np.ones([2, 2])
    fechamento = cv.morphologyEx(binaria, cv.MORPH_CLOSE, kernel)

    fechamento = np.array(fechamento, dtype=np.uint8)

    edges = cv.Canny(fechamento, 100, 100)

    contours, hierarchy = cv.findContours(edges, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    areas = [[cv.arcLength(c, False)] for c in contours]
    max_index = np.argmax(areas)
    cnt = contours[max_index]

    ellipse = cv.fitEllipse(cnt)
    eli = cv.ellipse(img.copy(), ellipse, (255, 255, 0), 1)
    cv.circle(eli, (int(ellipse[0][0]), int(ellipse[0][1])), 2, (0, 255, 0), 1)

    return eli

def pupila(folder):
    img = cv.imread(folder)
    gray = cv.cvtColor (img, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (7, 7), 0)
    (T, threshInv) = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    masked = cv.bitwise_and(img, img, mask=threshInv)
    edges = cv.Canny(threshInv,40,50)
    image = DeteccaoPupila(threshInv, img)
    cv.imshow('Imagem', threshInv)
    cv.waitKey(0) 
    cv.destroyAllWindows() 


def contour(folder):
    img = cv.imread(folder)
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(imgray,127,255,0)
    contours,hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]

    epsilon = 0.1*cv.arcLength(cnt,True)
    approx = cv.approxPolyDP(cnt,epsilon,True)

    cv.imshow('Imagem', approx)
    cv.waitKey(0) 
    cv.destroyAllWindows() 

def circulo(folder):
    img = cv.imread(folder, cv.IMREAD_COLOR) 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    gray_blurred = cv.blur(gray, (3, 3)) 
    blurred = cv.GaussianBlur(gray, (7, 7), 0)
    (T, threshInv) = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    detected_circles = cv.HoughCircles(threshInv,  
                    cv.HOUGH_GRADIENT, 2, minDist=100, param1 = 200, 
                param2 = 40, minRadius = 25, maxRadius = 70) 
    if detected_circles is not None: 
    
        
        detected_circles = np.uint16(np.around(detected_circles)) 
    
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            cv.circle(img, (a, b), r, (0, 255, 0), 2) 
            cv.circle(img, (a, b), 1, (0, 0, 255), 3) 
            cv.imshow("Detected Circle", img) 
            cv.waitKey(0) 

def cornea(folder):
    img = cv.imread(folder, cv.IMREAD_COLOR) 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) 
    blurred = cv.GaussianBlur(gray, (7, 7), 0)
    (T, threshInv) = cv.threshold(blurred, 150, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)
    detected_circles = cv.HoughCircles(threshInv,  
                    cv.HOUGH_GRADIENT, 2, minDist=100, param1 = 200, 
                param2 = 40, minRadius = 150, maxRadius = 0) 
    if detected_circles is not None: 
        for c in detected_circles:
            Area= None
            Area[c] = (int(detected_circles[c][3]) * int(detected_circles[c][3])) * 3.14
        Area.sort(reverse = True)
        
        detected_circles = np.uint16(np.around(detected_circles)) 
        cv.circle(img, (detected_circles[1][0], detected_circles[1][1]), detected_circles[1][2], (0, 255, 0), 2)
        cv.imshow("Detected Circle", img) 
        cv.waitKey(0) 

filename = sg.popup_get_file('Anexe a imagem:')

if filename != None:
    extensions = os.path.splitext(filename)

    if extensions[1] == '.jpeg' or extensions[1] == '.png' or extensions[1] == '.jpg':
            cornea(filename)
    else:
        print('Permitido apenas imagem')
else:
    print('Bye!')



