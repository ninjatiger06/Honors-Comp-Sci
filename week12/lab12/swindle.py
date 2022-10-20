from book import *


def readBookDatabase(filename):
	""" read in book info from bookdb.txt, save each line as a Book object in list.
		This list will be returned and will serve as availableBooks. """
	infile = open(filename, 'r')
	availableBooks = []
	for book in infile:
		# books have their important data split by commas
		book = book.strip()
		book = book.split(",")
		title = book[0]
		author = book[1]
		publishYear = book[2]
		bookPath = book[3]
		availableBooks.append(Book(title, author, publishYear, bookPath))
	infile.close()
	return availableBooks



class Swindle(object):
	""" class for a single Swindle object """

	def __init__(self, owner, ownedBooks, pageLength):
		""" constructor for swindle object, given the owner, books for sales,
			owned books, and default page length """
		self.owner = owner
		self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
		self.ownedBooks = ownedBooks
		self.pageLength = pageLength

	def __str__(self):
		""" pretty-print info about this object """
		###  TO BE COMPLETED BY YOU  ###
		s = "" #print owner's name, and number of owned/ available books
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
				book.setBookmark(currentPage - 1) #putsh this in read
		return

	def showOwned(self):
		"""This method allows the user to see which books they own"""
		print("\nBooks you own:")
		for i in range(len(self.ownedBooks)):
			print("%d: %s" % (i+1, self.ownedBooks[i].toString()))


	def showAvailable(self):
		print("\nAvailable books:")
		for i in range(len(self.availableBooks)):
			print("%d: %s" % (i+1, self.availableBooks[i].toString()))


	def getOwner(self):
		return self.owner


	def buy(self):
		#getValid Integer for buy fucntion as well
		self.showAvailable()
		while True:
			buyNum = int(input("\nWhich book would you like to buy? (0 to skip): "))
			if buyNum > 0:
				if buyNum <= len(self.availableBooks):
					boughtBook = self.availableBooks.pop(buyNum - 1)
					self.ownedBooks.append(boughtBook)
					print("Purchase successful, bought %s" % (boughtBook.toString()))
					break
				else:
					print("Invalid entry, try again")
			else:
				break

	def read(self):

		#make a get integer function (beetween 0 an length), pass the propmpt and low/high values for acccetable b=nums
		#we are missing a bookmark condition
		self.showOwned()
		getInteger("which book would you like to read? (0 to skip): ", 0, len(self.ownedBooks))

		if num >= 1:
			#user selected a book to read
			myBook = self.ownedBooks[readNum - 1]
			self.displayText(myBook)
			print("Setting bookmark in %s at page %i" %(myBook.getTitle(), myBook.getBookmark()))


			mybook.setBookmark()

		while True:
			readNum = int(input("which book would you like to read? (0 to skip): "))
			if readNum > 0:
				#make a
				#REMOVE
				myBook = self.ownedBooks[readNum - 1]


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
	books = [Book("Gettysburg Address", "Abe Lincoln", 1863, "book-database/gettysburg.txt"),
			 Book("Alice in Wonderland", "Lewis Carroll", 1865, "book-database/alice.txt")]
	myswindle = Swindle(owner, books, 20)

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