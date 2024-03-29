from enhancedSwindle import *

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

def writeSettings(userSwindle, fileName, owner):
	openFile = open(fileName, "w")
	openFile.write(owner)
	
	for ownedBook in userSwindle.getOwned():
		 bookText = ownedBook.toString()
		 
		 openFile.write("%s,%s,%s,%s,%s,%s" % (ownedBook.title, ownedBook.author, ownedBook.publishYear, ownedBook.filePath, ownedBook.bookmark,"owned\n"))

	for availableBooks in userSwindle.getOwned():
		Booktext = availableBooks.toString()
		openFile.write("%s,%s,%s,%s,%s,%s" % (availableBooks.title, availableBooks.author, availableBooks.publishYear, availableBooks.filePath, availableBooks.bookmark, "available\n"))


	openFile.close()



def main():

	owner = newUser()                   # Display instructions and get user's name
	userSwindle = Swindle(owner, 20)        # Create a new Swindle ereader for them

	while True:
		menuChoice = mainMenu()         # Display ereader's main menu
		if menuChoice == 1:
			userSwindle.buy()           # View available books with option to buy
		elif menuChoice == 2:
			userSwindle.showOwned()     # View owned books
		elif menuChoice == 3:
			userSwindle.read()           # Choose a book to read
		elif menuChoice == 4:
			writeSettings(userSwindle, "bookdb.txt", userSwindle.owner)
			break
			                   # Turn off ereader (quit the program)


main()
