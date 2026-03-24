from PIL import Image
import math
image = Image.new('RGB', (200, 200))
pixels = image.load()

for y in range(200):
    for x in range(200):
        if abs(math.sqrt((x-100)**2+(y-100)**2)) < 100:
            pixels[x,y] = (x, y, 255)

image.show()