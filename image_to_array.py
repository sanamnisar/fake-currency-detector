import Image
from numpy import *
from pprint import pprint

a = array(Image.open('very_small.png').convert("L"))
pprint(a)

