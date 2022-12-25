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


def confirmExistence(checkLst, prompt):
	"""
		Purpose: Checks to make sure an object with a given ID exists within a
		given list
		Parameters: List of existing ID's (list of int's), the input prompt (str)
		Returns: The existing ID (int)
	"""
	while True:
		userInput = validateInt(prompt)
		if userInput in checkLst:
			return userInput
		else:
			print("Please enter a valid ID.")


def addStudent():
	"""
		Purpose: Takes a user's inputs and creates a new student object
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Adding Student--------#")
	firstname = input("First name: ")
	lastname = input("Last name: ")
	student = gradebook.Student(firstname, lastname)
	print(student)


def addSection():
	"""
		Purpose: Takes a user's inputs and creates a new section object
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Adding Section--------#")
	studLst = []
	studLstIdxs = []
	courseName = input("Course Name: ")
	print("Students: ")
	for student in gradebook.students.values():
		print(student)
	print("\n")
	ADDING_STUDENTS = True
	while ADDING_STUDENTS:
		studIdx = validateInt("ID of student to add (Enter '0' to quit): ")
		if studIdx == 0:
			ADDING_STUDENTS = False
		elif studIdx not in list(gradebook.students):
			print("Please enter a valid student ID.")
		else:
			studLstIdxs.append(studIdx)
			print(f"Added student of ID {studIdx}")
	if len(studLstIdxs) > 0:
		for index in studLstIdxs:
			studLst.append(gradebook.students[index])
		section = gradebook.Section(studLst, courseName)
		print(f"\n{section}\nClass List:{section.classList()}")


def modifyGrades():
	"""
		Purpose: Takes a user's inputs to add grades to an already existing assignment.
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Entering Grades--------#")
	while True:
		title = input("Assignment title: ")
		l = [assignment for assignment in gradebook.assignments.values() if assignment.title == title]
		if len(l) > 0:
			break
		else:
			print("Please enter an existing assignment title that belongs to an existing section")
	outOf = validateInt("How many points the assigment is out of: ")
	gradebook.Assignment.enterGrade(title, outOf)


def createAssignment():
	"""
		Purpose: Creates a new assignment
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Creating Assignment--------#")
	sectID = confirmExistence(list(gradebook.sections), "Section ID: ")
	sectsdict = gradebook.sections
	sects = list(sectsdict.values())
	sect = [section for section in sects if section.sectionID == sectID]
	print("Students in the section:")
	roster = sect[0].roster()
	idLst = []
	for stud in roster:
		print(stud)
		idLst.append(stud.studentID)
	studID = validateInt("Student ID (If you wish to exit, enter 0): ")
	if studID == 0:
		return
	else:
		l = [student for student in gradebook.students.values() if student.studentID == studID]
		if len(l) > 0:
			title = input("Title of Assignment: ")
			grade = validateInt("Grade: ")
			outOf = validateInt("Out of: ")
			assignment = gradebook.Assignment(studID, sectID, title, grade, outOf, None)


def studentReport():
	"""
		Purpose: Prints all assignments and their grades for a given student, as
				 well as the student's average grade
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Student Grade Report--------#")
	studID = validateInt("Student ID: ")
	stud = [student for student in gradebook.students if student == studID]
	stud[0].gradeReport()


def calculateAverage(assigns):
	"""
		Purpose: Calculates the average grade given a list of assignments
		Parameters: List of assignments (list of assignment objects)
		Returns: The average grade (float)
	"""
	gradeTotal = 0
	outOfTotal = 0
	for assignment in assigns:
		gradeTotal += assignment.grade
		outOfTotal += assignment.outOf
	return round(gradeTotal / outOfTotal * 100, 2)


def assignmentReport():
	"""
		Purpose: Prints all the assignments for an assignment of a specific
				 title in one section and the average grade
		Parameters: None
		Returns: None
	"""
	print("\n\n#--------Assignment Report--------#")
	CHECKING_ASSIGNMENT = True
	while CHECKING_ASSIGNMENT:
		title = input("Assignment Title: ")
		sectID = validateInt("Section ID: ")
		assigns = [assignment for assignment in gradebook.assignments.values() if assignment.title == title and assignment.sectionID == sectID]
		if len(assigns) > 0:
			break
		else:
			print("Please enter a valid assignment that belongs to a valid section.")
	print("\nAssignments: ")
	for assignment in assigns:
		print(assignment)
	avg = calculateAverage(assigns)
	print(f"\nAverage Grade: {avg}%\n")


def saveAndQuit():
	"""
		Purpose: Saves all information to a file
		Parameters: None
		Returns: None
	"""
	print("\nSaving your data.")
	gradebook.saveGradebook({"students": gradebook.students, "sections": gradebook.sections, "assignments": gradebook.assignments})
	f = open("gradebook.txt", "w")
	students = []
	for student in gradebook.students.values():
		students.append(str(student))
	sections = []
	for section in gradebook.sections.values():
		sections.append(str(section))
	assignments = []
	for assignment in gradebook.assignments.values():
		assignments.append(str(assignment))
	f.write(str({"students": students, "sections": sections, "assignments": assignments}))
	f.close()


def justQuit():
	"""
		Purpose: Checks to see if the user really wants to quit. If so, quits
				 without saving
		Parameters: None
		Returns: None
	"""
	print("\n\n⚠WARNING⚠\nQuitting without saving changes may cause you to lose them!")
	CHECKING_QUIT = True
	while CHECKING_QUIT:
		WANT_QUIT = input("Are you sure you want to quit (y/n)? ")
		if WANT_QUIT == "y":
			return True
		elif WANT_QUIT == "n":
			return False
		else:
			print("Please input either 'y' or 'n'.")


def main():
	students, sections, assignments = gradebook.loadGradebook("gradebook.dat")
	print("Welcome, teacher.")
	RUNNING = True
	while RUNNING:
		if len(gradebook.students) <= 0:
			print("\nThere are no students yet.\nPlease Choose from the Following Options: \n1. Add a student\n7. Save and Quit\n8. Quit")
			CHOOSING_OPTION = True
			while CHOOSING_OPTION:
				userOption = validateInt("--> ")
				if userOption == 1 or userOption == 7 or userOption == 8:
					CHOOSING_OPTION = False
				else:
					print("Please select one of the options.\n")
		elif len(gradebook.sections) <= 0:
			print("\nThere are no sections yet.\nPlease Choose from the Following Options: \n1. Add a student\n2. Add a section\n7. Save and Quit\n8. Quit")
			CHOOSING_OPTION = True
			while CHOOSING_OPTION:
				userOption = validateInt("--> ")
				if userOption >= 1 and userOption <= 2 or userOption == 7 or userOption == 8:
					CHOOSING_OPTION = False
				else:
					print("Please select one of the options.\n")
		elif len(gradebook.assignments) <= 0:
			print("\nThere are no assignments yet.\nPlease Choose from the Following Options: \n1. Add a student\n2. Add a section\n3. Create a new assignment and enter grades\n7. Save and Quit\n8. Quit")
			CHOOSING_OPTION = True
			while CHOOSING_OPTION:
				userOption = validateInt("--> ")
				if userOption >= 1 and userOption <= 3 or userOption == 7 or userOption == 8:
					CHOOSING_OPTION = False
				else:
					print("Please select one of the options.\n")
		else:
			print("\nPlease Choose from the Following Options:\n1. Add a student\n2. Add a section\n3. Create a new assignment and enter grades\n4. Get a student grade report\n5. Get report of all grades from one section on one assignment\n6. Modify a preexisting grade\n7. Save and Quit\n8. Quit")
			CHOOSING_OPTION = True
			while CHOOSING_OPTION:
				userOption = validateInt("--> ")
				if userOption >= 1 and userOption <= 8:
					CHOOSING_OPTION = False
				else:
					print("Please select one of the options.\n")
		if userOption == 1:
			addStudent()
		elif userOption == 2:
			addSection()
		elif userOption == 3:
			createAssignment()
		elif userOption == 4:
			studentReport()
		elif userOption == 5:
			assignmentReport()
		elif userOption == 6:
			modifyGrades()
		elif userOption == 7:
			saveAndQuit()
			break
		else:
			QUIT = justQuit()
			if QUIT:
				break



main()
