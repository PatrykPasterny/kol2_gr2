import random

class Highschool(object):
	amount_of_classes=0
	classes=[]
			
	def init_classes(self,*args):
		for number, c in enumerate(args):
			self.classes.append(c)
			self.amount_of_classes=number+1
		
	def school_average(self):
		total=0
		for c in self.classes:
			total+=c.total_average()
		return total/float(self.amount_of_classes)	
	
class HighschoolClass(object):
	
	amount_of_students = 3
	students=[]
	
	def __repr__(self):
		output=""
		for s in self.students:
			output+="Student: " + s.name + " " + s.surname + "\nGrades: "
			for grade in s.scores:
				output+="%d" %grade + ", "
			output+="\nAverage: %2.f" %s.average()
			output+="\nAttendance: "
			for att in s.attendance:
				if att == 1:
					output+="+, "
				else:
					output+="-, "
			output+="\nAll student's attendances: %2.f" %s.sum_of_attendance() + "\n"
		return output
		
	def init_students(self):
		
		for x in range(self.amount_of_students):
			self.students.append(Student(raw_input("Wpisz imie ucznia do dziennika: "),raw_input("Wpisz nazwisko ucznia do dziennika: ")))
		
		for s in self.students:
			s.init_scores()
			s.init_attendance()
	
	def total_average(self):
		total=0
		for s in self.students:
			total+=s.average()
		return total/float(len(self.students))
	
	def total_attendance(self):
		total=0
		for s in self.students:
			total+=s.sum_of_attendance()
		output=total/(float(s.amount_of_classes)*self.amount_of_students)
		return 100*output
			
class Student(object):
	
	amount_of_grades=5
	amount_of_classes=10
	
	def __init__(self,name,surname):
		self.name=name
		self.surname=surname
		self.scores=[]
		self.attendance=[]
			
	def init_scores(self):
		for x in range(self.amount_of_grades): 
			self.scores.append(random.randint(1,5))
		
	def init_attendance(self):
		for x in range(self.amount_of_classes):
			self.attendance.append(random.randint(0,1))
		
	def average(self):
		av=sum(self.scores)
		output = av/float(len(self.scores))
		return output
		
	def sum_of_attendance(self):
		att=sum(self.attendance)
		return att		

class1A=HighschoolClass()
class1A.init_students()
print class1A
print "Average score in class 1A: %2.f" %class1A.total_average()
print "Total class 1A attendance in percent: %2.f%%" %class1A.total_attendance()
class1B=HighschoolClass()
class1B.init_students()
highschool=Highschool()
highschool.init_classes(class1A,class1B)
print "Average score in school: %f" %highschool.school_average()

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
