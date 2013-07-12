import Image
import numpy
im=Image.open('/home/sanum/fyp/pics.jpg')
#for reading the pixels of pics image
pixelMap=im.load()
#returns the starting pixels of image
pixel=pixelMap(0,0)
#array returns all the pixels values in array format
a= Array(Image.open('/home/sanum/fyp/pics.jpg').convert('L'))
#resizing the image 
width , height= (160,160)
size = (width,height)
im= img.resize(size)
im.show()
out path ='/home/sanum/fyp/resized_image.jpg'
im.save(outpath)
left=0
right=0
upper=0
lower=0
bbox=(left,upper,right,lower)
im=im.crop(bbox)
im.show()
