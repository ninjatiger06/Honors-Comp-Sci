"""
	Author: Jonas Pfefferman '24
	Date: 8/30/22
	Description: Uses reviews from movieReviews.txt to associate the connotation
				 of a word with a certain review score
"""

from searches import *
from time import time

def readStopWords():
	"""
		Purpose: Reads in the stop words file
		Parameters: None
		Returns: A List of all the stop words
	"""
	stopWordsFile = open("stopwords.txt", 'r')
	stopWordsLst = []
	for line in stopWordsFile:
		line = line.strip()
		stopWordsLst.append(line)
	return stopWordsLst

def readReviews():
	"""
		Purpose: Reads in the reviews file and calls other functions to look at the lines
		Parameters: None
		Returns: None
	"""
	reviewsFile = open('movieReviews.txt', 'r')
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
			# get rid of non-alpha characters and stop words
			if word.isalpha() == True and binarySearch(word, stopWords) == False:
				WORD_PRESENT = False
				i = 0
				for i in range(len(allReviews)):
					if word == allReviews[i][1]:
						WORD_PRESENT = True
						break

				if WORD_PRESENT == True:
					allReviews[i][0] += score

				else:
					allReviews.append([score, word])

	# for review in allReviews:
	# 	print(review[0], review[1])
	sortReviews(allReviews)


def sortReviews(allReviews):
	"""
		Purpose: Sorts the list of review words by score and prints the top and
				 bottom 20
		Parameters: The list of words and their scores (list of lists)
		Returns: None
	"""
	# for i in range(1, len(allReviews)):
	# 	marker = allReviews[i][1][0]
	# 	j = i-1
	# 	while j >= 0 and marker > allReviews[j][1][0]:
	# 		allReviews[j+1] = allReviews[j]
	# 		j -= 1
	# 	allReviews[j+1] = marker

	for i in range(1, len(allReviews)):
		marker = allReviews[i]
		j = i-1
		while j >= 0 and marker > allReviews[j]:
			allReviews[j+1] = allReviews[j]
			j -= 1
		allReviews[j+1] = marker

	if len(allReviews) > 20:
		for i in range(20):
			print(allReviews[i][0], allReviews[i][1])

		for i in range(len(allReviews)-21, len(allReviews)-1):
			print(allReviews[i][0], allReviews[i][1])
	else:
		for review in allReviews:
			print(review[0], review[1])


def main():
	t1 = time()
	readReviews()
	t2 = time()
	print("\nTime: %8.4f" % (t2-t1))


main()
