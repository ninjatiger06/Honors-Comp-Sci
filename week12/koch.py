from graphics import *
from zturtle import *

def koch(t, n, size):
	if n == 0:
		t.forward(size)
	else:
		for angle in [-60, 120, -60, 0]:
			koch(t, n - 1, size / 3)
			t.turn(angle)

def main():

	n = int(input("Value of n: "))

	gw = GraphWin("Koch Snowflake", 900, 600)
	gw.setBackground("black")

	t = ZTurtle(0, 300, gw)

	koch(t, n, 900)

	if gw.getMouse():
		gw.close()



main()
