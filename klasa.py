import random

class HighschoolClass(object):
	students=[]
	def init_students(self):
		self.students.append(Student("Patryk","Pasterny"))
		self.students.append(Student("Marcin","Pasterny"))
		self.students.append(Student("Krzysiek","Pasterny"))
		self.students.append(Student("Robert","Pasterny"))
		self.students.append(Student("Maciek","Pasterny"))
		for s in self.students:
			s.init_scores()
			s.init_attendance()
	
	def total_average(self):
		total=0
		for s in self.students:
			total+=s.average()
		return total/len(self.students)
			
class Student(object):
		scores=[]
		attendance=[]
		name=""
		surname=""
		def __init__(self,name,surname):
			self.name=name
			self.surname=surname
		
		def init_scores(self):
			for x in range(5):
				self.scores.append(random.randint(1,6))
		
		def init_attendance(self):
			for x in range(10):
				self.attendance.append(random.randint(0,1))
		
		def average(self):
			av=sum(self.scores)
			output = av/len(self.scores)
			return output
		
		def sum_of_attendance(self):
			att=sum(self.attendance)
			return att
		

class1A=HighschoolClass()
class1A.init_students()
print class1A.total_average()


# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
