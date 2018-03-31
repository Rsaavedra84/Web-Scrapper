from urllib import request
from PIL import Image

img1 = Image.open("_DSC0380.JPG")
img2 = Image.open("_DSC0381.JPG")

r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()

new_img = Image.merge("RGB", (r1, g2, b1))
new_img = Image.effect_mandelbrot(1, 1, 1)
new_img.show()