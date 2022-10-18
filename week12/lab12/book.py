class Book(object):
	""" class for a single Book object """

	def __init__(self, title, author, publishYear, filePath):
		""" constructor for book object, given the title, the author, and the
		 	year the book was published"""
		self.title = title
		self.author = author
		self.publishYear = int(publishYear)
		self.filePath = filePath
		self.bookmark = 0

	def __str__(self):
		""" pretty-print info about this object """
		return ("Title: %s\nAuthor: %s\nPublished: %d\nPath: %s" % (self.title, self.author, self.publishYear, self.filePath))

	def toString(self):
		""" pretty printing for user side """
		return ("%25s by %20s (%4d)" % (self.title, self.author, self.publishYear))

	def getTitle(self):
		""" getter for the title """
		return self.title

	def getAuthor(self):
		""" getter for the author """
		return self.author

	def getPublished(self):
		""" getter for the year published """
		return self.publishYear

	def getFilename(self):
		""" getter for the file name """
		return self.filePath

	def getBookmark(self):
		""" getter for the bookmark """
		return self.bookmark

	def setBookmark(self, pageNum):
		""" setter for bookmark """
		self.bookmark = pageNum

	def getText(self):
		""" getter for the full text """
		bookLines = ""
		with open(self.filePath, 'r') as file:
			for line in file:
				if line[0] != "#":
					bookLines += line
		return bookLines


if __name__ == '__main__':

	print("Testing the Book class...")
	myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
	"book-database/gettysburg.txt")

	print("Testing print...")
	print(myBook)

	print("Testing toString...")
	print(myBook.toString())

	print("Testing getFilename...")
	print(myBook.getFilename())

	print("Testing getText...")
	text = myBook.getText()
	print(text[:105])                   # only print the first couple of lines

	print("bookmark is:", myBook.getBookmark())
	myBook.setBookmark(12)
	print("now bookmark is:", myBook.getBookmark())


