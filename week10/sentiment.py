"""
	Author: Jonas Pfefferman '24
	Date: 8/30/22
	Description: Uses reviews from movieReviews.txt to associate the connotation
				 of a word with a certain review score
"""

from searches import *

def readStopWords():
	"""
		Purpose: reads in the stop words file
		Parameters: None
		Returns: A List of all the stop words
	"""
	stopWordsFile = open("stopwords.txt", 'r')
	stopWordsLst = []
	for line in stopWordsFile:
		stopWordsLst.append(line)

	return stopWordsLst

def readReviews():
	"""
		Purpose: Reads in the reviews file and calls other functions to look at the lines
		Parameters: None
		Returns: None
	"""
	reviewsFile = open('smallReviews.txt', 'r')
	allReviews = []

	# read in each review
	for line in reviewsFile:

		# clean up the review
		line = line.strip().lower()
		lineLst = line.split()

		# get and alter the score
		score = int(lineLst[0]) - 2

		# get the rest of the words in the review
		review = lineLst[1:]

		# read in the stop words
		stopWords = readStopWords()

		for word in review:
			# get rid of non-alpha characters
			if word.isalpha() == False:
				review.remove(word)

			# if the word is a stop words, remove it from the review
			if binarySearch(word, stopWords):
				review.remove(word)
			else:
				if word not in allReviews:
					allReviews.append([score, word])

	print(allReviews)
def main():
	readReviews()


main()
