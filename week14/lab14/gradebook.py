import pickle

students = {}
sections = {}
assignments = {}
gradeBook = {}


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


def enterGrades(title, outOf):
	"""
		Purpose: Repeatedly calls Assignment.enterGrade() with the same outOf
				 value until sectionID entered is 0
		Parameters: Title of the assignment (string) and how many total points
					the assignment is worth (integer)
		Returns: None
	"""
	ENTERING_GRADES = True
	while ENTERING_GRADES:
		newAssignment = Assignment.enterGrade(title, outOf)
		if newAssignment == None:
			ENTERING_GRADES = False
		else:
			assignments.update({newAssignment.assignmentID: newAssignment})


def showGrades(title):
	"""
		Purpose: Prints a list of all assignments and their grades whose titles
				 match the title input
		Parameters: The title of the assignemnt (string)
		Returns: None
	"""
	l = [assignment for assignment in list(assignments.values()) if assignment.title == title]
	l.sort(key=lambda assignment: students[assignment.sectionID].lastname)
	# m = []
	# for assignment in l:
	# 	m.append(students[assignment.studentID])
	# m.sort(key=lambda student: student.lastname)
	for i in range(len(l)-1, -1, -1):
		print(f"{l[i]}\n")


def adjustGrade(title):
	"""
		Purpose: Change the grade of a given student in a specific class
		Inputs: The title of the assignment (string)
		Returns: None
	"""
	ASSIGNMENT_EXISTS = False
	for assignment in assignments.values():
		if title == assignment.title:
			ASSIGNMENT_EXISTS = True
	showGrades(title)
	GRADE_EXISTS = False
	while GRADE_EXISTS == False:
		sectID = validateInt("Section ID: ")
		studID = validateInt("Student ID: ")
		# l = [section for section in sections.values() if section.sectionID == sectID]
		# m = [student for student in l[0].studentList if student.studentID == studID]
		assign = [assignment for assignment in assignments.values() if assignment.sectionID == sectID and assignment.studentID == studID]
		if len(assign) == 1:
			GRADE_EXISTS = True
		else:
			print("Please input a student in an existing section\n")
	newGrade = validateInt("New Grade: ")
	assign[0].grade = newGrade
	print(assign[0])



class Student(object):
	""" class for single student object including their first name, last name, and ID """

	nextID = 1

	def __init__(self, firstname, lastname):
		""" constructor for student object given student's first and last names (strings) """
		self.firstname = firstname
		self.lastname = lastname
		if len(students) >= 1:
			self.studentID = len(students) + 1
			Student.nextID = self.studentID + 1
		else:
			self.studentID = Student.nextID
			Student.nextID += 1
		students.update({self.studentID: self})

	def __str__(self):
		return f"Name: {self.lastname}, {self.firstname}     ID: {self.studentID}"

	def gradeReport(self):
		""" Returns the student's average (float) and prints all of the student's
		 	assignments, including their names, points earned, max points, and final average """
		studentAssignments = [assignment for assignment in list(assignments.values()) if assignment.studentID == self.studentID]
		if len(studentAssignments) > 0:
			gradeTotal = 0
			outOfTotal = 0
			for assignment in studentAssignments:
				print(assignment)
				gradeTotal += assignment.grade
				outOfTotal += assignment.outOf
			avg = round(gradeTotal / outOfTotal * 100, 2)
			print(f"\nAverage Grade: {avg}%\n")
		else:
			print("This student has no assignments.")


class Section(object):
	""" class for an academic class section, including its name, the list of
		the students in it, and its ID """

	nextSectID = 1

	def __init__(self, studentList, courseName):
		""" constructor for the course class taking the student list (list of
			student objects) and the name of the course (string) """
		self.studentList = studentList
		self.courseName = courseName

		print(len(sections))
		if len(sections) >= 1:
			self.sectionID = len(sections) + 1
			Section.nextSectID = self.sectionID + 1
		else:
			self.sectionID = Section.nextSectID
			Section.nextSectID += 1
		sections.update({self.sectionID: self})

	def __str__(self):
		""" returns the course name and section id in a human-friendly format """
		return f"Course Name: {self.courseName}\nSection ID: {self.sectionID}"

	def classList(self):
		""" returns human-friendly list of students in a given class """
		studentsEnrolled = []
		for student in self.studentList:
			studentsEnrolled.append(str(student))
			print(str(student))
		return studentsEnrolled

	def roster(self):
		""" returns a list of all student objects in a given section"""
		studentsEnrolled = []
		for student in self.studentList:
			studentsEnrolled.append(student)
		return studentsEnrolled

	def addStudentByID(self):
		""" prints a list of all students in a section, then takes an input by
		 	user (integer) and adds the student with that ID to the section"""
		print("\nAll Students:")
		for student in students.values():
			print(student)
		addID = int(input("ID of the student to add: "))
		l = [student for student in students.values() if student.studentID == addID]
		if l[0] not in self.studentList:
			self.studentList.append(l[0])

	def addStudentByName(self, firstname, lastname):
		""" takes the first and last names of a student and them adds them to the section """
		l = [student for student in students.values() if student.firstname == firstname and student.lastname == lastname]
		if l[0] not in self.studentList:
			self.studentList.append(l[0])


class Assignment(object):
	""" class for an individual student's assignments and their grade for it """

	nextAssignmentID = 1

	def __init__(self, studentID, sectionID, title, grade, outOf, assignID):
		""" constructor taking the student's id number (int), section id number
			(int), the title of the assignment (str), the number of points the
			student received (int), the total number of points in the
			assignment (int), and, if it's an already existing assignment being
			modified, takes that assignment's id (int) """

		self.studentID = studentID
		self.sectionID = sectionID
		self.title = title
		self.grade = grade
		self.outOf = outOf

		if assignID == None:
			if len(assignments) >= 1:
				self.assignmentID = len(assignments) + 1
				Assignment.nextAssignmentID = self.assignmentID + 1
			else:
				self.assignmentID = Assignment.nextAssignmentID
				Assignment.nextAssignmentID += 1
			assignments.update({self.assignmentID: self})
		else:
			self.assignmentID = assignID
			assignments.update({self.assignmentID: self})

	def __str__(self):
		sectName = [section for section in list(sections.values()) if section.sectionID == self.sectionID]
		studentInfo = [student for student in list(students.values()) if student.studentID == self.studentID]
		return f"Assignment ID: {self.assignmentID}\tTitle: {self.title}\tGrade: {self.grade}\tOut of: {self.outOf}\tCourse Name: {sectName[0].courseName}\n{studentInfo[0]}"

	@classmethod
	def enterGrade(cls, title, outOf):
		"""
			Purpose: Allows the user to enter a grade into an already existing assigment
			Parameters: The title of the assignment (str) how many points it's out of (int)
			Returns: The new assignment
		"""
		print("Available Sections:")
		for section in sections:
			print(f"{section}\n")
		while True:
			sectionIDInput = validateInt("Which section is the student in? ")
			if sectionIDInput == 0:
				print("Cancelling grade entering")
				return None
			elif sectionIDInput in list(sections):
				break
			else:
				print("Please enter a valid section.")
		print("Students in this section:")
		l = [section for section in list(sections.values()) if section.sectionID == sectionIDInput]
		for student in l[0].studentList:
			print(student)
		studentIDInput = validateInt("What is the student's ID? ")
		gradeInput = validateInt("How many points did the student get? ")
		assign = [assignment for assignment in list(assignments.values()) if assignment.title == title]
		assignID = assign[0].assignmentID
		assignments.pop(assignID)
		return Assignment(studentIDInput, sectionIDInput, title, gradeInput, outOf, assignID)


def loadGradebook(filename):
	"""
		Purpose: Loads an existing instance of a gradebook from an inputted file
		Parameters: Name of file of gradebook (string)
		Returns: students, sections, and assignments dictionaries
	"""
	# filename = input("Name of the file to load: ")
	try:
		with open(filename, 'rb') as infile:
			instance = pickle.load(infile)
			students = instance["students"]
			sections = instance["sections"]
			assignments = instance["assignments"]
		return students, assignments, sections
	except FileNotFoundError:
		Student.nextID = 1
		Assignment.nextID = 1
		Section.nextID = 1
		students = {}
		sections = {}
		assignments = {}
		return students, assignments, sections


def saveGradebook(instance):
	"""
		Purpose: Saves the gradebook as a pickle
		Paramters: Instance of all the stuudents, sections, and assignments dictionaries
		Returns: None
	"""
	# filename = input("Name of the file to save data to: ")
	with open("gradebook.dat", 'wb') as outfile:
		pickle.dump(instance, outfile)


students, sections, assignments = loadGradebook("gradebook.dat")


if __name__ == '__main__':
	print("\n#--------Making Students--------#")
	student1 = Student("Kenini", "Kabobovic")
	student2 = Student("John", "Jearbear")
	student3 = Student("Janos", "Pfeffy")
	student4 = Student("Eric", "Chong")
	for student in students.values():
		print(student)

	print("\n\n#--------Making sections--------#")
	section1 = Section([student1, student2], "P1 Honors Comp. Sci.")
	print(section1)
	classList1 = section1.classList()
	print(classList1)
	section2 = Section([student3, student4], "P2 Honors Comp. Sci.")
	print(section2)
	classList2 = section2.classList()
	print(classList2)

	# print("\n#--------Adding Student By ID--------#")
	# print("Old Class List:")
	# section1.classList()
	# section1.addStudentByID()
	# print('\nUpdated Class List')
	# section1.classList()

	# print("\n#--------Adding Student By Name--------#")
	# print("Original Class List:")
	# section1.classList()
	# section1.addStudentByName("Eric", "Chong")
	# print("\nNew Class List:")
	# section1.classList()

	print("\n\n#--------Class Lists--------#")
	for section in list(sections.values()):
		print("#-----Section Break-----#")
		print(section.classList())

	print("\n\n#--------Making Assignment--------#")
	assignment2 = Assignment(1, 1, "Lab 84", 24, 40, None)
	assignment3 = Assignment(2, 1, "Lab 84", 40, 40, None)
	assignment6 = Assignment(3, 2, "Lab 84", 18, 40, None)
	assignment7 = Assignment(4, 2, "Lab 84", 36, 40, None)
	# assignment4 = Assignment(3, 2, "Reading Quiz #1", 4, 5)
	# assignment5 = Assignment(4, 2, "Reading Quiz #1", 2, 5)

	# print("\n\n#--------Entering Assignment Grade--------#")
	# assignment1 = Assignment.enterGrade("Lab 84", 40)
	# for assignment in assignments.values():
	# 	print(assignment)

	# print("\n\n#--------Global enterGrades()--------#")
	# enterGrades("Lab 84", 38)
	# for assignment in list(assignments.values()):
	# 	print(assignment)


	print("\n\n#--------Showing Grades--------#")
	showGrades("Lab 84")

	# print("\n\n#--------Adjusting Grades--------#")
	# adjustGrade("Lab 84")

	print("\n\n#--------Loading Gradebook--------#")
	studs, sects, assigns = loadGradebook("gradebook.dat")
	for stud in studs.values():
		print(stud)
	for sect in sects.values():
		print(sect)
	for assign in assigns.values():
		print(assign)

	# print("\n\n#--------Saving Grades--------#")
	# saveGradebook({"students": students, "assignments": assignments, "sections": sections})
