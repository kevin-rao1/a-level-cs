from PIL import Image, ImageDraw

image = Image.new("RGB", (200,200))
draw = ImageDraw.Draw(image)

draw.line([(30, 90), (100, 180)], width=5, fill=(100,125,100))
#draw.ellipse([(100,50), (150)])

image.show()