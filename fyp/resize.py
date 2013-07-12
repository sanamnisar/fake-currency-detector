#!/usr/bin/env python
from PIL import Image, ImageChops
im= Image.open('/home/sanum/fyp/picss.jpg')
 
def trim(im, border):
bg = Image.new(im.mode, im.size, border)
diff = ImageChops.difference(im, bg)
bbox = diff.getbbox()
if bbox:
return im.crop(bbox)
 
def create_thumbnail(path, size):
image = Image.open(path)
name, extension = path.split('.')
options = {}
if 'transparency' in image.info:
options['transparency'] = image.info["transparency"]
image.thumbnail((size, size), Image.ANTIALIAS)
image = trim(image, 255) ## Trim whitespace
image.save(name + '_new.' + extension, **options)
return image 
