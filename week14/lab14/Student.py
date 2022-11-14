class Student(object):
	""" class for single student object"""

	def __init__(self, firstname, lastname):
		"""constructor for student object given student's first and last names (strings)"""
		self.firstname = firstname
		self.lastname = lastname
		self.studentID = self.checkStudents("studentDB.json")

	def checkStudents(self, databaseName):
		""" Checks the student database for the most recent instance to get the
		 	student id. """
		databaseFile = open(databaseName, 'r')
		studentLst = []
		try:
			lastStudent = databaseFile[len(databaseFile)]
			return lastStudent["studentID"] + 1
		except "TypeError":
			return 000


if __name__ == '__main__':
	newStudent = Student("janos", "bruh")
