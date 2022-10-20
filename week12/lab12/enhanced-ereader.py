from swindle import *

def newUser():
	print("\nSince this is the first time you used it,")
	print("let's customize your Swindle...")
	owner = str(input("\nPlease enter your name: "))
	print("\nWelcome to %s's Swindle v1.0!" % owner)
	return owner

def mainMenu():
	print("\n--------------------------------------------------\n")
	print("1) Buy/See available books\n2) See owned books\n3) Read a book\n4) Exit\n")
	while True:
		userInput = str(input("---> "))
		try:
			menuChoice = int(userInput)
			if 1 <= menuChoice <= 4:
				return menuChoice
			else:
				print("invalid number, try again")
		except ValueError:
			print("invalid input, try again")

def writeSettings(fileName):



	print("hello")
	openFile = open(fileName, "a")

	ownedList = []

	for book in Swindle.ownedBooks():
		bookList.append(Swindle.ownedBooks(book))

	availableList = []
	for book in Swindle.availableBooks():
		availableList = availableList.append(Swindle.availableBooks(book))

	for book in ownedList:
		openFile.write(book + "owned")

	for book in availableList:
		openFile.write(books + "available")

	openFile.write(getOwner())
	openFile.write(getBookmark())

	openFile.close()
	


def main():

	owner = newUser()                   # Display instructions and get user's name
	userSwindle = Swindle(owner)        # Create a new Swindle ereader for them

	while True:
		menuChoice = mainMenu()         # Display ereader's main menu
		if menuChoice == 1:
			userSwindle.buy()           # View available books with option to buy
		elif menuChoice == 2:
			userSwindle.showOwned()     # View owned books
		elif menuChoice == 3:
			userSwindle.read()          # Choose a book to read
		else:
			writeSettings("bookdb.txt")                       # Turn off ereader (quit the program)


main()
