"""
	Description: Imports movie reviews and their scores to understand the
				 sentiment behind each word. By totalling the scores for each
				 word, the program can show which words relate to the highest
				 opinions and which to the lowest.
	Author: Jonas Pfefferman '24
	Date: 11/2/22
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
	allReviews = {}
	for line in reviewsFile:
		line = line.strip().lower()
		lineLst = line.split()
		score = int(lineLst[0]) - 2     # get and alter the score
		review = lineLst[1:]     # get rest of words in review
		for word in review:
			processWordScore(word, score, allReviews, stopWords)

	reviewsFile.close()
	return allReviews

#------------------------------------------------------------------------------#
def processWordScore(word, score, allReviews, stopWords):
	"""
	Purpose: Check if word is a valid word in the dictionary and not a stop word
	Parameters: word (str) that is to be assigned a score, current score of the
				word (int), dictionary of each word and its score (dictionary of
				integers with str key values), list of stop words (list of str)
	Returns: None
	"""
	if word.isalpha():     # ignoring non-alpha characters
		if binarySearch(word, stopWords) == False:
			try:
				allReviews[word] += int(score)
			except KeyError:
				allReviews.update({word : int(score)})
	return


#------------------------------------------------------------------------------#
def sortReviews(wordSentiments):
	"""
	Purpose: Sorts the list of review words by score
	Parameters: The list of words and their scores (list of lists)
	Return Val: Sorted list of lists
	"""
	# Sorting all the reviews by score (greatest to least)
	for i in range(1, len(wordSentiments)):
		marker = wordSentiments[i]
		j = i-1
		# If the marker is greater than the current index (because greatest --> least)
		while j >= 0 and marker[1] > wordSentiments[j][1]:
			# Moving the sentiment
			wordSentiments[j+1] = wordSentiments[j]
			j -= 1
		wordSentiments[j+1] = marker

	return wordSentiments


#------------------------------------------------------------------------------#
def printReviews(sortedSentiments):
	"""
	Purpose: Formats and prints the top and bottom 20 reviews
	Parameters: List of all the reviews (list of lists)
	Return Val: None
	"""
	for lst in sortedSentiments:
		word = lst[0]
		score = lst[1]
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

	sortedSentiments = sortReviews(list(wordSentiments.items()))

	# printing the results
	print("Top 20:")
	printReviews(sortedSentiments[:20])
	print("\nBottom 20:")
	printReviews(sortedSentiments[-20:])

	t2 = time()
	print("\nTime: %8.4f" % (t2-t1))


main()
