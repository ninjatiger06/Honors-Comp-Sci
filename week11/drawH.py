from graphics import *
import sys

def drawH(win, pt, size):
	p1 = pt.clone()
	p1.move(-size,-size)
	p2 = pt.clone()
	p2.move(-size,size)
	leftedge = Line(p1,p2)   			# create left edge of the H
	leftedge.draw(win)

	p3 = pt.clone()
	p3.move(size, size)
	p4 = pt.clone()
	p4.move(size, -size)
	rightedge = Line(p3, p4)
	rightedge.draw(win)

	p5 = p1.clone()
	p5.move(0, size)
	p6 = p4.clone()
	p6.move(0, size)
	middle = Line(p5, p6)
	middle.draw(win)

	return

def drawRecursive(win, location, size, levels):

	drawH(win, location, size)

	if levels > 0:
		topLeft = Point(location.getX()-size, location.getY()-size)
		bottomLeft = Point(location.getX()-size, location.getY()+size)
		topRight = Point(location.getX()+size, location.getY()-size)
		bottomRight = Point(location.getX()+size, location.getY()+size)

		win = drawRecursive(win, topLeft, size/2, levels-1)
		win = drawRecursive(win, bottomLeft, size/2, levels-1)
		win = drawRecursive(win, topRight, size/2, levels-1)
		win = drawRecursive(win, bottomRight, size/2, levels-1)

def main():
	win = GraphWin("Letter H", 600,600)
	pt = Point(win.getWidth()/2, win.getHeight()/2)      			# assume we are given these
	size = 50                				# assume we are given these

	levels = int(sys.argv[1])

	drawRecursive(win, pt, size, levels)

	win.getMouse()
	win.close()
main()
