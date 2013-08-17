import Image
#!/usr/bin/env python
from numpy import *
from pprint import pprint
import ImageFilter
global ext
ext = ".jpg"
a=array(Image.open('pics.jpg').convert("L"))
pprint(a)
im=Image.open('pics.jpg')
#im.show()



#to CROP image 
#def imgCrop(im1):
    
    #box = (50, 50, 200, 300)
    #region = im.crop(box)
    #region.save("CROPPED" + ext)
#imgCrop(im) 
#im.show()


#Find edges
def filterFindEdges(im):
    
    im1 = im.filter(ImageFilter.FIND_EDGES)
    im1.save("EDGES" + ext)
filterFindEdges(im)
#im1.show()