"""
Description: Takes a given file path and a pattern and recursively searches
			 the given directory and subdirectory to print out all files that
			 have a match with the pattern
Date: 9/22/22
Author: Jonas Pfefferman '24
"""

from os import listdir
from os.path import isdir, expanduser

def fullPath(path):
	"""
		Description: Replaces a '~/' input from the user with their home directory
		Parameters: File path (str)
		Returns: Expanded file path (str)
	"""
	# replacing the "~/" with the user's home directory
	return expanduser(path[:1]) + "/" + path[2:]


def findFiles(path, pattern):
	"""
		Description: Searches through all files and subfolders in a given path
					 and prints the paths of files that match the given patter
		Parameters: File path (str) character pattern (str)
		Returns: None
	"""

	contents = listdir(path)     # get a list of everything in the file
	for item in contents:     # iterate through said list
		if isdir(path + "/" + item):     # check if there's child directory to search through
			newPath = path + "/" + item
			findFiles(newPath, pattern)     # recursively search through the child directory
		else:
			if pattern in item:
				print(path + "/" + item)

def main():

	path = input("path: ")
	pattern = input("pattern: ")

	# if the user uses the linux "home" shortcut, the path needs to be expanded
	if "~/" in path:
		path = fullPath(path)

	findFiles(path, pattern)


main()
