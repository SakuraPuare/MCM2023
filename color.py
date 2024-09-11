import numpy
from PIL import Image

color = numpy.array(Image.open('color.png'))
color = color[0]
r = color[...,0]
g = color[...,1]
b = color[...,2]

print(r.tolist())
print(g.tolist())
print(b.tolist())


