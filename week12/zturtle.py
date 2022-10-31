"""
	Description: turtle class using Zelle graphics (only partially complete).
	Author: Mr. Bloom
	Date: Spring 2020
"""

from graphics import *
from math import *
from time import sleep

###############################################################

class ZTurtle(object):
	""" Zelle Graphics Turtle """
	def __init__ (self, xCord, yCord, graphWin):
		""" constructor for the ZTurtle class, with its x-coordinate, y-coordinate,
			and the graphics window """
		self.x = xCord
		self.y = yCord
		self.window = graphWin
		self.heading = 0
		self.tailup = False
		self.color = "white"

	def __str__ (self):
		s = "Position: (%i,%i), Heading %i, Tailup: %s" % (self.x, self.y, self.heading, self.tailup)
		return s

	def setColor(self, newColor):
		self.color = newColor

	def setHeading(self, newHeading):
		self.heading = newHeading

	def turn(self, angle):
		self.heading += angle

	def down(self):
		self.tailup = False

	def up(self):
		self.tailup = True

	def moveTo(self, newX, newY):
		self.currTail = self.tailup
		self.tailup = True
		self.x = newX
		self.y = newY
		self.tailup = self.currTail

	def dot(self):
		self.point = Point(self.x, self.y)
		self.point.setFill(self.color)
		self.point.draw(self.window)


	# you need to write:
	#
	# __init__    construct new turtle, given x,y coords and graphics win
	#             hint...use these instance variables:
	#
	#             self.x          current x position
	#             self.y          current y position
	#             self.heading    current heading (0 means East,90 North)
	#             self.tailup     True if tail is up, False if down
	#             self.window     the graphics window for drawing
	#             self.color      color used for drawing
	#
	# __str__     return string with x,y,heading, and tail up or down
	# setColor    change color of pen
	# setHeading  set turtle direction
	# turn        alter turtle direction by certain angle
	# down        put tail down
	# up          lift tail up
	# moveto      magically move turtle to location x,y (no drawing)
	# dot         drop a visible marker at current location


	def forward(self, ds):
		""" move forward a distance ds, draw if tail is down """
		curr_pt = Point(self.x, self.y)
		theta = radians(self.heading)
		dx = ds * cos(theta)
		dy = ds * sin(theta)
		nx = self.x + dx
		ny = self.y + dy
		new_pt = Point(nx, ny)
		if not self.tailup:
			L = Line(curr_pt, new_pt)
			L.draw(self.window)
			L.setFill(self.color)
			sleep(0.1)
		self.x = nx
		self.y = ny


#------------------------------------------------------------------------------#

if __name__ == "__main__":
	gw = GraphWin("zturtle test", 500, 500)
	gw.setBackground("gray")
	t = ZTurtle(100,100,gw)
	print(t)
	t.down()
	t.forward(100)
	gw.getMouse()
