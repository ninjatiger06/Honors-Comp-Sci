class Section(object):
	def __init__(self, studentList, courseName):
		""" initialize-er for the course class taking the student list (list of
			student objects) and the name of the course (string) """
		self.studentList = studentList
		self.courseName = courseName
		self.sectionID = 4

	def __str__(self):
		""" returns the course name and section id in a human-friendly format """
		return "Course Name: %s\nSection ID: %i\n" % (self.courseName, self.sectionID)

	def classList(self):
		""" returns human-friendly list of students in a given class """
		studentsEnrolled = []
		for student in studentList:
			studentsEnrolled.append(str(student))
		return studentsEnrolled
