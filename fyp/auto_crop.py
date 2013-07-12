#!/usr/bin/env python
 
import sys
import Image
def autocrop_image(image, border = 0):
    # Get the bounding box
    bbox = image.getbbox()
 
    # Crop the image to the contents of the bounding box
    image = image.crop(bbox)
 
    # Determine the width and height of the cropped image
    (width, height) = image.size
 
    # Add border
    width += border * 2
    height += border * 2
 
    # Create a new image object for the output image
    cropped_image = Image.new("RGBA", (width, height), (0,0,0,0))
 
    # Paste the cropped image onto the new image
    cropped_image.paste(image, (border, border))
 
    # Done!
    return cropped_image
    if len(sys.argv) < 3:
    # Not enough arguments -- show usage information and exit
    print "Usage: " + sys.argv[0] + " infile outfile [border]"
    exit(1)
 
# Get input and output file names
infile = sys.argv[1]
outfile = sys.argv[2]
 
# Check if border size was provided
if sys.argv[3]:
    border = int(sys.argv[3])
else:
    border = 0
 
# Open the input image
image = Image.open(infile)
 
# Do the cropping
image = autocrop_image(image, border)
 
# Save the output image
image.save(outfile)
