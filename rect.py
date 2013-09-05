import Image, math

def find_centroid(im):
    width, height = im.size
    XX, YY, count = 0, 0, 0
    for x in xrange(0, width, 1):
        for y in xrange(0, height, 1):
            if im.getpixel((x, y)) == 0:
                XX += x
                YY += y
                count += 1
    return XX/count, YY/count
#Top Left Vertex
def find_vertex1(im):
    width, height = im.size
    for y in xrange(0, height, 1):
        for x in xrange (0, width, 1):
            if im.getpixel((x, y)) == 0:
                X1=x
                Y1=y
                return X1, Y1

#Bottom Left Vertex
def find_vertex2(im):
    width, height = im.size
    for x in xrange(0, width, 1):
        for y in xrange (height-1, 0, -1):
            if im.getpixel((x, y)) == 0:
                X2=x
                Y2=y
                return X2, Y2

#Top Right Vertex
def find_vertex3(im):
    width, height = im.size
    for x in xrange(width-1, 0, -1):
        for y in xrange (0, height, 1):
            if im.getpixel((x, y)) == 0:
                X3=x
                Y3=y
                return X3, Y3

#Bottom Right Vertex
def find_vertex4 (im):
    width, height = im.size
    for y in xrange(height-1, 0, -1):
        for x in xrange (width-1, 0, -1):
            if im.getpixel((x, y)) == 0:
                X4=x
                Y4=y
                return X4, Y4

def find_angle (V1, V2, direction):
    side1=math.sqrt(((V1[0]-V2[0])**2))
    side2=math.sqrt(((V1[1]-V2[1])**2))
    if direction == 0:
        return math.degrees(math.atan(side2/side1)), 'Clockwise'
    return 90-math.degrees(math.atan(side2/side1)), 'Counter Clockwise'

#Find direction of Rotation; 0 = CW, 1 = CCW
def find_direction (vertices, C):
    high=480
    for i in range (0,4):
        if vertices[i][1]<high:
            high = vertices[i][1]
            index = i
    if vertices[index][0]<C[0]:
        return 0
    return 1
def main():
    im = Image.open('rect.png')
    im = im.convert('1') # convert image to black and white
    print 'Centroid ', find_centroid(im)
    print 'Top Left ', find_vertex1 (im)
    print 'Bottom Left ', find_vertex2 (im)
    print 'Top Right', find_vertex3 (im)
    print 'Bottom Right ', find_vertex4 (im)
    C = find_centroid (im)
    V1 = find_vertex1 (im)
    V2 = find_vertex3 (im)
    V3 = find_vertex2 (im)
    V4 = find_vertex4 (im)
    vertices = [V1,V2,V3,V4]
    direction = find_direction(vertices, C)
    print 'angle: ', find_angle(V1,V2,direction)

if __name__ == '__main__':
  main()