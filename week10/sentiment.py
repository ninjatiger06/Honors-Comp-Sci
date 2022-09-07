"""
	Author: Jonas Pfefferman '24
	Date: 8/30/22
	Description: Uses reviews from movieReviews.txt to associate the connotation
				 of a word with a certain review score
"""

from searches import *
from time import time

def readStopWords(fileName):
	"""
		Purpose: Reads in the stop words file
		Parameters: The file name/path of the filter list
		Returns: A List of all the stop words
	"""
	stopWordsFile = open(fileName, 'r')
	# create a list of all the stop words
	stopWordsLst = []
	for line in stopWordsFile:
		line = line.strip()
		stopWordsLst.append(line)
	return stopWordsLst

def readReviews(fileName, stopWords):
	"""
		Purpose: Reads in the reviews file and calls other functions to look at the lines
		Parameters: The file name for the reviews file and the list of stop words
		Returns: A list of filtered words and their scores
	"""
	reviewsFile = open(fileName, 'r')
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

		for word in review:
			# get rid of non-alpha characters and stop words
			if word.isalpha() == True and binarySearch(word, stopWords) == False:

				# check if the word is already in the list of allReviews and get the index
				WORD_PRESENT, wordIdx = isWordPresent(word, allReviews)

				# if the word is already in the list, add the scores
				if WORD_PRESENT == True:
					allReviews[wordIdx][0] += score

				# if the word isn't in the list, add it and its score
				else:
					allReviews.append([score, word])

	return allReviews


def isWordPresent(word, allReviews):
	"""
		Purpose: Checks if a given word is already present within the allReviews
				 list. If it is present the index is returned
		Parameters: The word being checked (string) and the list of words and
					their sentiments (list of lists)
		Returns: Whether or not the word is present (boolean) and if present,
				 its index
	"""
	WORD_PRESENT = False
	wordIdx = -1

	# Iterating through all the reviews to search
	for i in range(len(allReviews)):

		# Checking if the word is in the "word" index of the sentiment
		if word == allReviews[i][1]:
			WORD_PRESENT = True
			wordIdx = i
			break     # Don't need to keep searching once the word is found
	return WORD_PRESENT, wordIdx


def sortReviews(wordSentiments):
	"""
		Purpose: Sorts the list of review words by score and prints the top and
				 bottom 20
		Parameters: The list of words and their scores (list of lists)
		Returns: None
	"""
	# Sorting all the reviews by score (greatest to least)
	for i in range(1, len(wordSentiments)):
		marker = wordSentiments[i]
		j = i-1
		# If the marker is greater than the current index (because greatest --> least)
		while j >= 0 and marker > wordSentiments[j]:
			# Moving the sentiment
			wordSentiments[j+1] = wordSentiments[j]
			j -= 1
		wordSentiments[j+1] = marker

	return     # Nothing to return because the list has been edited


def printReviews(wordSentiments):
	"""
		Purpose: Formats and prints the top and bottom 20 reviews
		Parameters: List of all the reviews (list of lists)
		Returns: None
	"""
	# only printing the top and bottom 20 if the list is longer than 40
	if len(wordSentiments) > 40:
		# print the top 20 reviews
		for i in range(20):
			print(wordSentiments[i][0], wordSentiments[i][1])
		print("\n")
		# print the bottom 20 reviews
		for i in range(len(wordSentiments)-20, len(wordSentiments)):
			print(wordSentiments[i][0], wordSentiments[i][1])
	else:
		# print all the reviews
		for review in allReviews:
			print(review[0], review[1])


def main():
	# timing program
	t1 = time()
	stopWords = readStopWords("stopwords.txt")
	wordSentiments = readReviews("movieReviews.txt", stopWords)
	sortReviews(wordSentiments)
	printReviews(wordSentiments)
	t2 = time()
	print("\nTime: %8.4f" % (t2-t1))


main()
