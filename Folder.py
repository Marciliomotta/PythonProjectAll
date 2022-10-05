import os
import PySimpleGUI as sg
from dom import DOM
import Show
import pickle
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

iqa = DOM()

filename = sg.popup_get_file('Anexe a imagem:')
#sg.popup('Selecionado', filename)


if filename != None:
    extensions = os.path.splitext(filename)

    if extensions[1] == '.jpeg' or extensions[1] == '.png' or extensions[1] == '.jpg':
        score = iqa.get_sharpness(filename)
        if score>0.80:
            Show.show(filename)
        else:
            print('A Imagem não possui uma boa qualidade')

    else:
        print('Permitido apenas imagem')
else:
    print('Bye!')






