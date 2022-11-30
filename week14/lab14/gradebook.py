students = []
sections = []
assignments = []

class Student(object):
	""" class for single student object including their first name, last name, and ID """

	nextID = 1

	def __init__(self, firstname, lastname):
		""" constructor for student object given student's first and last names (strings) """
		self.firstname = firstname
		self.lastname = lastname
		self.studentID = Student.nextID
		Student.nextID += 1
		students.append(self)

	def __str__(self):
		return f"Name: {self.lastname}, {self.firstname}     ID: {self.studentID}"

	def gradeReport(self):
		""" Returns the student's average (float) and prints all of the student's
		 	assignments, including their names, points earned, max points, and final average """
		pass


class Section(object):
	""" class for an academic class section, including its name, the list of
		the students in it, and its ID """

	nextSectID = 1

	def __init__(self, studentList, courseName):
		""" constructor for the course class taking the student list (list of
			student objects) and the name of the course (string) """
		self.studentList = studentList
		self.courseName = courseName
		self.sectionID = Section.nextSectID
		Section.nextSectID += 1
		sections.append(self)

	def __str__(self):
		""" returns the course name and section id in a human-friendly format """
		return f"Course Name: {self.courseName}\nSection ID: {self.sectionID}"

	def classList(self):
		""" returns human-friendly list of students in a given class """
		studentsEnrolled = []
		for student in self.studentList:
			# studentsEnrolled.append(str(student))
			print(str(student))
		# return studentsEnrolled

	def addStudentByID(self):
		""" prints a list of all students in a section, then takes an input by
		 	user (integer) and adds the student with that ID to the section"""
		for student in students:
			print(student)
		addID = int(input("ID of the student to add: "))
		l = [student for student in students if student.studentID == addID]
		if l[0] not in self.studentList:
			self.studentList.append(l[0])

	def addStudentByName(self, firstname, lastname):
		""" takes the first and last names of a student and them adds them to the section """
		l = [student for student in students if student.firstname == firstname and student.lastname == lastname]
		if l[0] not in self.studentList:
			self.studentList.append(l[0])


class Assignment(object):
	""" class for an individual student's assignments and their grade for it """

	nextAssignmentID = 1

	def __init__(self, studentID, sectionID, title, grade, outOf):
		""" constructor taking the student's id number (int), section id number
			(int), the title of the assignment (str), the number of points the
			student received (int), and the total number of points in the
			assignment (int) """

		self.studentID = studentID
		self.sectionID = sectionID
		self.title = title
		self.grade = grade
		self.outOf = outOf
		self.assignmentID = Assignment.nextAssignmentID
		Assignment.nextAssignmentID += 1
		assignments.append(self)

	def __str__(self):
		sectName = [section for section in sections if section.sectionID == self.sectionID]
		studentInfo = [student for student in students if student.studentID == self.studentID]
		return f"Assignment ID: {self.assignmentID}\tTitle: {self.title}\tGrade: {self.grade}\tOut of: {self.outOf}\tCourse Name: {sectName[0].courseName}\n{studentInfo[0]}"

	@classmethod
	def enterGrade(cls, title, outOf):
		print("Available Sections:")
		for section in sections:
			print(f"{section}\n")
		sectionIDInput = int(input("Which section is the student in? "))
		print("Students in this section:")
		l = [section for section in sections if section.sectionID == sectionIDInput]
		for student in l[0].studentList:
			print(student)
		studentIDInput = int(input("What is the student ID of the student to give the assignment? "))
		gradeInput = int(input("How many points did the student get? "))
		return Assignment(studentIDInput, sectionIDInput, title, gradeInput, outOf)


if __name__ == '__main__':
	print("\n#--------Making Students--------#")
	student1 = Student("Kenini", "Kabobovic")
	student2 = Student("John", "Jearbear")
	student3 = Student("Janos", "Pfeffy")
	student4 = Student("Eric", "Chong")
	for student in students:
		print(student)

	print("\n\n#--------Making sections--------#")
	section1 = Section([student1, student2], "Honors Comp. Sci.")
	print(section1)
	classList1 = section1.classList()
	print(classList1)

	print("\n#--------Adding Student By ID--------#")
	section1.classList()
	section1.addStudentByID()
	for student in section1.classList():
		print(student)

	print("\n#--------Adding Student By Name--------#")
	section1.classList()
	section1.addStudentByName("Eric", "Chong")
	for student in section1.classList():
		print(student)

	print("\n\n#--------Making Assignment--------#")
	assignment1 = Assignment.enterGrade("Lab 37", 40)
	print(assignment1)
