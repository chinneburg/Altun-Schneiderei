from PIL import Image
import sys

img = Image.open('src/assets/images/logo_bag.jpg')
w, h = img.size
# Crop just the scissors, "Änderungsschneiderei" and "ALTUN"
# The logo is centered in the upper half of the bag image.
box = (int(w*0.1), int(h*0.15), int(w*0.9), int(h*0.5))
logo = img.crop(box)
logo.save('src/assets/images/logo.jpg')
