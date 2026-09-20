from PIL import Image
import sys

img = Image.open('src/assets/images/logo_new.png')
# Get a pixel from the background (e.g., top-right corner, avoiding the text)
# Top left is x=10, y=10
rgb = img.getpixel((10, 10))
if isinstance(rgb, int):
    # Sometimes it's indexed
    rgb = img.convert('RGB').getpixel((10, 10))
    
# Or find the most common color
colors = img.convert('RGB').getcolors(img.size[0]*img.size[1])
# Sort by count, descending
colors.sort(reverse=True)
# The background is likely the most common color
dominant_rgb = colors[0][1]

hex_color = '#%02x%02x%02x' % dominant_rgb
print("DOMINANT:", hex_color)

