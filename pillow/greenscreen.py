from PIL import Image
image0 = Image.open("image.png")
image1 = Image.open("shia_labeouf_wants_you_to_get_motivated.jpg") 
image1 = image1.resize(image0.size)
pixels0 = image0.load()
pixels1 = image1.load()

# attempt 1: complete guess
greeness_threshold = 10 # anything below is too aggressive

for x in range(image0.size[0]):
    for y in range(image0.size[1]):
        try:
            image1_pixel = pixels1[x,y]
        except:
            print(x,y)
        greenness = (image1_pixel[1])-((image1_pixel[0]+image1_pixel[1]+image1_pixel[2])//3)
        if greenness < greeness_threshold:
            pixels0[x,y] = image1_pixel

image0.show()


# attempt 2: the "proper" way
# i feel scammed
image0 = Image.open("image.png")
pixels0 = image0.load()

image1_hsv = image1.convert("HSV")
pixels1_hsv = image1_hsv.load()

for x in range(image0.size[0]):
    for y in range(image0.size[1]):
        if not ((60 < pixels1_hsv[x,y][0] < 110) and (pixels1_hsv[x,y][1] > 50)):
            pixels0[x,y] = pixels1[x,y]

image0.show()