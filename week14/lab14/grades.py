import gradebook

def validateInt(prompt):
	"""
		Purpose: Checks to make sure a given input is an integer
		Paramters: The prompt of the question to ask the user (string)
		Returns: The user's input (int)
	"""
	while True:
		userInput = input(prompt)
		try:
			return int(userInput)
		except ValueError:
			print("Please enter a valid integer")


def addStudent():
	print("\n\n#--------Adding Student--------#")
	firstname = input("First name: ")
	lastname = input("Last name: ")
	student = gradebook.Student(firstname, lastname)


def addSection():
	studLst = []
	studLstIdxs = []
	while True:
		studIdx = validateInt("ID of student to add. Enter '0' to quit")
		if studIdx == 0:
			break
		else:
			studLstIdxs.append(studIdx)
	for index in studLstIdxs:
		pass



def main():
	students, sections, assignments = gradebook.loadGradebook("gradebook.dat")
	print("Welcome, teacher.")
	while True:
		print("\nPlease Choose from the Following Options:\n1. Add a student\n2. Add a section\n3. Enter grades for assignment\n4. Get a student grade report\n5. Get report of all grades from one section on one assignment\n6. Modify a preexisting grade\n7. Save and Quit\n8. Quit witout saving")
		while True:
			userOption = validateInt("--> ")
			if userOption >= 1 and userOption <= 8:
				break
		if userOption == 1:
			addStudent()
		elif userOption == 2:
			addSection()
		elif userOption == 7:
			gradebook.saveGradebook({"students": gradebook.students, "assignments": gradebook.assignments, "sections": gradebook.sections})
			break



main()
