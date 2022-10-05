from email.mime import image
from PIL import Image
  
img = Image.open(r'Image')
rgba = img.convert("RGBA")
datas = rgba.getdata()
  
newData = []
for item in datas:
    if item[0] == 255 and item[1] == 255 and item[2] == 255:  # finding black colour by its RGB value
        # storing a transparent value when we find a black colour
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)  # other colours remain unchanged
  
rgba.putdata(newData)
rgba.save(r"transparent_image_Right.png", "PNG")

olho = Image.open(r'C:\Users\mmotta\PycharmProjects\Curso\nitidez\test\018L_2.png')
olho = olho.convert("RGBA")
width, height = olho.size
rgba = rgba.resize((width,height))

olho.paste(rgba, (0,0), mask = rgba)
olho.show()