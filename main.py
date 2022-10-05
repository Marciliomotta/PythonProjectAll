from dom import DOM
from scipy import ndimage
import PySimpleGUI as sg

iqa = DOM()
filename = sg.popup_get_file('Anexe sua imagem')

score = iqa.get_sharpness(filename)
print("Sharpness:", score)



