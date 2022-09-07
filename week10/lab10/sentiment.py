"""
	Description: Imports movie reviews and their scores to understand the
				 sentiment behind each word. By totalling the scores for each
				 word, the program can show which words relate to the highest
				 opinions and which to the lowest.
	Author: Jonas Pfefferman '24
	Date: 8/30/22
"""

from searches import *
from time import time

#------------------------------------------------------------------------------#
def readStopWords(fileName):
	"""
	Purpose: Reads in the file with stop words (words that can be ignored)
	Parameters: The file name (str) of the filter list in .txt format
	Return Val: A List of all the stop words (strings)
	"""
	stopWordsFile = open(fileName, 'r')
	stopWordsLst = []     # create a list of all the stop words
	for line in stopWordsFile:
		word = line.strip()
		stopWordsLst.append(word)
	stopWordsFile.close()
	return stopWordsLst


#------------------------------------------------------------------------------#
def readReviews(fileName, stopWords):
	"""
	Purpose: Reads in the reviews file and calls other functions to look at the lines
	Parameters: The file name for the reviews file (str) and the list of stop
				words (list of strings)
	Return Val: A list of filtered words and their scores (list of lists)
	"""
	reviewsFile = open(fileName, 'r')
	allReviews = []
	for line in reviewsFile:
		line = line.strip().lower()
		lineLst = line.split()
		score = int(lineLst[0]) - 2     # get and alter the score
		review = lineLst[1:]     # get rest of words in review
		for word in review:
			if word.isalpha():     # ignoring non-alpha characters
				if binarySearch(word, stopWords) == False:
					WORD_PRESENT, wordIdx = isWordPresent(allReviews, word)
					if WORD_PRESENT:
						allReviews[wordIdx][0] += score
					else:
						allReviews.append([score, word])

	reviewsFile.close()
	return allReviews

#------------------------------------------------------------------------------#
def isWordPresent(allReviews, word):
	"""
	Purpose: Checks if a given word is already present within the allReviews
			 list. If it is present the index is returned
	Parameters: The word being checked (string) and the list of words and
				their sentiments (list of lists)
	Return Val: Whether or not the word is present (boolean) and if present,
				its index (integer). If it's not present, and index of -1 is returned
	"""
	WORD_PRESENT = False
	# Iterating through all the reviews to search
	for i in range(len(allReviews)):
		seenWord = allReviews[i][1]
		if word == seenWord:     # checking if the word is in the mini-lists of allReviews
			WORD_PRESENT = True
			wordIdx = i
			return WORD_PRESENT, wordIdx
	return WORD_PRESENT, -1


#------------------------------------------------------------------------------#
def sortReviews(wordSentiments):
	"""
	Purpose: Sorts the list of review words by score and prints the top and
			 bottom 20
	Parameters: The list of words and their scores (list of lists)
	Return Val: None
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


#------------------------------------------------------------------------------#
def printReviews(wordSentiments):
	"""
	Purpose: Formats and prints the top and bottom 20 reviews
	Parameters: List of all the reviews (list of lists)
	Return Val: None
	"""
	for lst in wordSentiments:
		word = lst[1]
		score = lst[0]
		print("%3i %s" % (score, word))

	"""# only printing the top and bottom 20 if the list is longer than 40
	if len(wordSentiments) > 40:
		print("Top 20:")
		# print the top 20 reviews
		for i in range(20):
			print(wordSentiments[i][0], wordSentiments[i][1])
		print("\nBottom 20:")
		# print the bottom 20 reviews
		for i in range(len(wordSentiments)-20, len(wordSentiments)):
			print(wordSentiments[i][0], wordSentiments[i][1])
	else:
		print("All Reviews:")
		# print all the reviews
		for review in wordSentiments:
			print(review[0], review[1])"""


#------------------------------------------------------------------------------#
def main():
	# timing program
	t1 = time()

	# read in the stop words
	stopWords = readStopWords("stopwords.txt")

	# read in the rotten tomatoes reviews
	wordSentiments = readReviews("movieReviews.txt", stopWords)

	sortReviews(wordSentiments)

	# printing the results
	print("Top 20:")
	printReviews(wordSentiments[:20])
	print("\nBottom 20:")
	printReviews(wordSentiments[-20:])

	t2 = time()
	print("\nTime: %8.4f" % (t2-t1))


main()
