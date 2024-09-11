import imagehash
import os
import pathlib
from PIL import Image

path = pathlib.Path('download')

for folder in path.iterdir():
    file_list = list(folder.iterdir())
    l = len(file_list)
    try:
        for i in range(l):
            hasha = imagehash.average_hash(Image.open(file_list[i]))
            for j in range(i+1, l):
                hashb = imagehash.average_hash(Image.open(file_list[j]))
                if hasha - hashb < 5:
                    print(file_list[i], file_list[j])
                    if file_list[i].name < file_list[j].name:
                        os.remove(file_list[j])
                    else:
                        os.remove(file_list[i])
    except FileNotFoundError:
        pass


