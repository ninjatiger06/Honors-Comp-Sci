class Student(object):
	""" class for single student object including their first name, last name, and ID """

	nextID = 1
	students = []

	def __init__(self, firstname, lastname):
		""" constructor for student object given student's first and last names (strings) """
		self.firstname = firstname
		self.lastname = lastname
		self.studentID = Student.nextID
		Student.nextID += 1
		self.students.append(self)


class Section(object):
	""" class for an academic class section, including its name, the list of
		the students in it, and its ID """

	nextSectID = 1

	def __init__(self, studentList, courseName):
		""" constructor for the course class taking the student list (list of
			student objects) and the name of the course (string) """
		self.studentList = studentList
		self.courseName = courseName
		self.sectionID = Student.nextSectID
		Student.nextSectID += 1

	def __str__(self):
		""" returns the course name and section id in a human-friendly format """
		return "Course Name: %s\nSection ID: %i\n" % (self.courseName, self.sectionID)

	def classList(self):
		""" returns human-friendly list of students in a given class """
		studentsEnrolled = []
		for student in studentList:
			studentsEnrolled.append(str(student))
		return studentsEnrolled


if __name__ == '__main__':
	newStudent = Student("janos", "bruh")
