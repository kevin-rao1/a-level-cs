from PIL import Image
old_image = Image.open("image.png")
print(old_image.size)
new_image = Image.new("RGB", old_image.size)
pixels_old = old_image.load()
pixels_new = new_image.load()
old_image.show()

#red
for y in range(old_image.size[1]):
    for x in range(old_image.size[0]):
        pixels_new[x,y] = (pixels_old[x,y][0],0,0)
new_image.show()

# greyscale
for y in range(old_image.size[1]):
    for x in range(old_image.size[0]):
        value = (pixels_old[x,y][0]+pixels_old[x,y][1]+pixels_old[x,y][2])//3
        pixels_new[x,y] = (value,value,value)
new_image.show()

# flipped
for y in range(old_image.size[1]):
    for x in range(old_image.size[0]):
        try:
            pixels_new[x,y] = pixels_old[(old_image.size[0]-1-x),y]
        except:
            print(x,y)
new_image.show()