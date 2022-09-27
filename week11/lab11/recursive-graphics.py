"""
Description: Recursively draws a special shape to a given number of levels
Date: 9/25/22
Author: Jonas Pfefferman '24
"""

from graphics import *
import sys

def drawShape(gw, centerPoint, size):
	"""
		Description: Draws the shape
		Parameters: The window to draw into (graphics window), the center point
					(point made of integers), the size of the "size" or length
					of the shape (integer)
		Returns: None
	"""
	# create the top triangle
	p1 = Point(centerPoint.getX(), centerPoint.getY() - size * 1.5)
	p2 = Point(p1.getX() - size/2, centerPoint.getY() - size/2)
	p3 = Point(p1.getX() + size/2, p2.getY())
	tri1 = Polygon(p1, p2, p3)
	tri1.setFill("lightGreen")
	tri1.draw(gw)

	# create the bottom triangle
	p4 = Point(centerPoint.getX(), centerPoint.getY() + size * 1.5)
	p5 = Point(p4.getX() - size/2, centerPoint.getY() + size/2)
	p6 = Point(p4.getX() + size/2, p5.getY())
	tri2 = Polygon(p4, p5, p6)
	tri2.setFill("lightGreen")
	tri2.draw(gw)

	# create the left triangle (can copy some values from other triangles)
	p7 = p5
	p8 = p2
	p9 = Point(p7.getX() - size, centerPoint.getY())
	tri3 = Polygon(p7, p8, p9)
	tri3.setFill("lightGreen")
	tri3.draw(gw)

	# create the right triangle (can copy some values from other triangles)
	p10 = p6
	p11 = p3
	p12 = Point(p10.getX() + size, centerPoint.getY())
	tri4 = Polygon(p10, p11, p12)
	tri4.setFill("lightGreen")
	tri4.draw(gw)

	# create the square in the center
	centerRect = Rectangle(p2, p6)
	centerRect.setFill("lightBlue")
	centerRect.draw(gw)

	return

def recurseShape(gw, centerPoint, size, recurseNum):
	"""
		Description: Calls the drawShape function at least once or recursively
					 if needed
		Parameters: Graphics window (GraphWin), the center point (point), the
					size (int), and the number of times to recurse (int)
		Returns: None
	"""

	# have to draw the shape at least once no matter what
	drawShape(gw, centerPoint, size)

	# only draw the shapes if the function was meant to be called
	if recurseNum >= 1:

		# recursively draw another "shape" to each corner of the current shape but half the size
		recurseShape(gw, Point(centerPoint.getX() - size*1.5, centerPoint.getY() - size*1.5), size/2, recurseNum -1)
		recurseShape(gw, Point(centerPoint.getX() + size*1.5, centerPoint.getY() - size*1.5), size/2, recurseNum -1)
		recurseShape(gw, Point(centerPoint.getX() - size*1.5, centerPoint.getY() + size*1.5), size/2, recurseNum -1)
		recurseShape(gw, Point(centerPoint.getX() + size*1.5, centerPoint.getY() + size*1.5), size/2, recurseNum -1)

def main():

	# width = int(input("window width: "))
	# height = int(input("window height: "))
	# size = int(input("size: "))
	# recurseNum = int(input("number of times to recurse: "))

	# simplified inputs
	width = int(sys.argv[1])
	height = int(sys.argv[2])
	size = int(sys.argv[3])
	recurseNum = int(sys.argv[4])

	gw = GraphWin("Recursive Shape", width, height)

	recurseShape(gw, Point(width/2, height/2), size, recurseNum)

	print("Click the draw window to close")
	# close the window on mouse click
	click = gw.getMouse()
	gw.close()


main()
