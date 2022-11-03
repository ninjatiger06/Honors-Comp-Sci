from book import *


def readBookDatabase(filename):
	""" read in book info from bookdb.txt, save each line as a Book object in list.
		This list will be returned and will serve as availableBooks. """
	infile = open(filename, 'r')
	availableBooks = []
	ownedBooks = []
	for book in infile:
		# books have their important data split by commas
		book = book.strip()
		book = book.split(",")
		title = book[0]
		author = book[1]
		publishYear = book[2]
		bookPath = book[3]
		bookmark = book[4]
		newBook = Book(title, author, publishYear, bookPath, bookmark)
		if book[5] == "owned":
			ownedBooks.append(newBook)
		else:
			availableBooks.append(newBook)
	return availableBooks, ownedBooks




class Swindle(object):
	""" class for a single Swindle object """

	def __init__(self, owner, pageLength):
		""" constructor for swindle object, given the owner, books for sales,
			owned books, and defautl page length """
		self.owner = owner
		self.availableBooks, self.ownedBooks = readBookDatabase("bookdb.txt")    # list of Book objects
		self.pageLength = pageLength

	def __str__(self):
		""" pretty-print info about this object """
		###  TO BE COMPLETED BY YOU  ###
		s = ""
		return s

	def getLetter(self):
		""" This method determines what the user wants to do next """
		validChoices = ['n', 'p', 'q']
		while True:
			readingChoice = str(input("\nn (next); p (previous); q (quit): "))
			if readingChoice in validChoices:
				return readingChoice
			print("invalid input, try again")

	def displayPage(self, book):
		""" This method displays a single page at a time (300 chars) """
		bookContents = book.getText()
		bookLinesList = bookContents.split("\n")
		numLines = len(bookLinesList)
		numPages = numLines // self.pageLength  # calculate total number of pages in book
		page = book.getBookmark()               # get current page (most recently read)
		pageStart = page * self.pageLength
		pageEnd = pageStart + self.pageLength   # display 20 lines per page
		if pageEnd > numLines:
			pageEnd = numLines                  # in case you're at the end of the book
		for i in range(pageStart, pageEnd):
			print(bookLinesList[i])
		if numPages == 1:                       # alter page numbers for 1-page books
			page = 1
		print("\nShowing page %d out of %d" % (page, numPages))
		return

	def displayText(self, book):
		""" This method allows the user to read one of their books.
			It calls displayPage() to show a single page at a time.
			It calls getLetter() to determine what the user wants to do next.
			When the user decides to quit reading a particular book, this method
			returns the (updated) Book object.
		"""
		while True:
			self.displayPage(book)
			currentPage = book.getBookmark()
			choice = self.getLetter()       # user chooses to quit or read the next/previous page
			if choice == "q":               # quit reading and return to ereader
				book.setBookmark(currentPage)
				return book
			elif choice == "n":                 # move on to the next page in the book
				bookContents = book.getText()   # unless user is on the last page
				numLines = bookContents.count("\n")
				currentLine = currentPage * self.pageLength
				if (currentLine + 1) < (numLines - self.pageLength):
					book.setBookmark(currentPage+1)
				else:
					print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
			else:                               # return to previous page in the book
				book.setBookmark(currentPage-1)
		return

	def buy(self):
		self.showAvailable()
		while True:
			buyNum = int(input("Which book would you like to buy? (0 to skip): "))
			if buyNum > 0:
				if buyNum <= len(self.availableBooks):
					boughtBook = self.availableBooks.pop(buyNum - 1)
					self.ownedBooks.append(boughtBook)
					print("Purchase successful, bought %s" % (boughtBook))
					break
				else:
					print("Invalid entry, try again")
			else:
				break

	def showOwned(self):
		"""This method allows the user to see which books they own"""
		print("Books you own:")
		for i in range(len(self.ownedBooks)):
			print("%d: %s" % (i+1, self.ownedBooks[i].toString()))


	def showAvailable(self):
		print("Available books:")
		for i in range(len(self.availableBooks)):
			print("%d: %s" % (i+1, self.availableBooks[i].toString()))


	def getOwner(self):
		return self.owner


	def read(self):
		self.showOwned()
		while True:
			readNum = int(input("which book would you like to read? (0 to skip): "))
			if readNum > 0:
				if readNum <= len(self.ownedBooks):
					self.displayText(self.ownedBooks[readNum - 1])
					break
				else:
					print("Invalid entry, try again")
			else:
				break


if __name__ == '__main__':
	print("Testing the Swindle class...")
	owner = "Lionel"
	myswindle = Swindle(owner, 20)

	print("Testing showAvailable...")
	myswindle.showAvailable()

	print("Testing showOwned...")
	myswindle.showOwned()

	################ Write additional tests below ###################

	print("Testing getOwner...")
	print(myswindle.getOwner())

	print("Testing buy...")
	myswindle.buy()

	print("Testing read...")
	myswindle.read()
