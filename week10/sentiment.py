"""
	Author: Jonas Pfefferman '24
	Date: 8/30/22
	Description: Uses reviews from movieReviews.txt to associate the connotation
				 of a word with a certain review score
"""
def readFile():
	"""
		Purpose: Reads in the file and calls other functions to look at the lines
		Parameters: None
		Returns: None
	"""
	reviewsFile = open('movieReviews.txt', 'r')
	L = []
	for line in reviewFile:
		line = line.strip().lower()
		lineLst = line.split()
		score = int(lineLst[0]) - 2
		review = lineLst[1:]
		for word in review:
			if word not in

def main():
	readFile()


main()
