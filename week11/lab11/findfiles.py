from os import listdir
from os.path import isdir, expanduser

def findFiles(path, pattern):
	contents = listdir(path)
	for item in contents:
		print(item)
		if isdir(item):
			print("here")
			newPath = path + "/" + item
			findFiles(newPath, pattern)
		else:
			if pattern in item:
				print(path + "/" + item)

def main():

	path = input("path: ")
	pattern = input("pattern: ")

	findFiles(expanduser(path), pattern)


main()
