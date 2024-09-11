import numpy
from PIL import Image
import pathlib

for folder in pathlib.Path('download').iterdir():
    if not folder.is_dir():
        continue
    data_list = []
    with open(folder.name + '.csv', 'w') as f:
        f.write('filename, \n')
        for file in folder.iterdir():
            img = Image.open(file)
            img = img.resize((1, 1))
            pixel = img.getpixel((0, 0))
            g = (pixel[0]/1.5 + pixel[1] * 2 + pixel[2] / 1.5) / 3
            f.write(file.name + ',' +str(g) +'\n')
            img.resize((100, 100)).save('resized/' + folder.name + '/' + file.name)
