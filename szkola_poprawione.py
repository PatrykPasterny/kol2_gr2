def student_average(student):
	marks=[float(n) for n in student["marks"].split(",")]
	return float(sum(marks))/len(marks)
			
def student_attendance(student):
	attendance=[float(n) for n in student["attendance"].split(",")]
	return (sum(attendance)/len(attendance))*100
	
def class_average(school_class):
	average=0.
	for student in school_class:
		average+=student_average(school_class[student])
	return float(average)/len(school_class)
		
def class_attendance(school_class):
	attendance=0.
	for student in school_class:
		attendance+=student_attendance(school_class[student])
	return float(attendance)/len(school_class)
	
def total_average(highschool):
	average=0.
	for classes in highschool:
		for attributes in classes:
			if attributes=="students":
				average+=class_average(classes[attributes])
	return float(average)/len(highschool)
	
def total_attendance(highschool):	
	attendance=0.
	for classes in highschool:
		for attributes in classes:
			if attributes=="students":
				attendance+=class_attendance(classes[attributes])
	return float(attendance)/len(highschool)
	
def print_school(highschool,student_keys):
	for classes in highschool:
		for attributes in classes:
			if attributes=="students":
				print "KLASA: "	
				for student in classes[attributes]:
					for key in student_keys:
						print "\t%s: %s " %(key,classes[attributes][student][key]),
					print "\n",

def print_students_average_and_attendance(highschool):
	for classes in highschool:
		for attributes in classes:
			if attributes=="students":
				print "KLASA: "
				for student in classes[attributes]:
					print "\tUczen: %s %s." %(classes[attributes][student]["name"],classes[attributes][student]["surname"])
					print "Srednia jest rowna: %.2f. " %(student_average(classes[attributes][student])),
					print "Procent obecnosci jest rowny %.2f%%." %(student_attendance(classes[attributes][student]))
				print "\n"
				
def print_class_average_and_attendance(highschool):
	for classes in highschool:
		print "\tKLASA 1 uzyskala srednia: %.2f i procentowa obecnosc: %.2f%%." %(classes["class_average"],classes["class_attendance"])
				
def print_school_average_and_attendance(highschool):
	print "Srendia uczniow calej szkoly jest rowna: %.2f, a procentowa obecnosc: %.2f%%." %(total_average(highschool),total_attendance(highschool))

def fill_av_and_att_in_school(highschool):
	for classes in highschool:
		classes["class_average"]=class_average(classes["students"])
		classes["class_attendance"]=class_attendance(classes["students"])	
		
 

"""	
POPRAWA: 
NA SLOWNIKACH
ZADNEGO SUMOWANIA W PETLI
MAX 3 KLASY
MAX 3 METODY W KAZDEJ
MAX 4 LINIJKI NA METODE(6 Z NAZWA I RETURNEM, LAMANIE LINII SIE NIE LICZY
REQUIREMENTS.TXT - dane do wczytywania z pliku
SKRYPT URUCHOMIENIOWY
MAX 2 PLIKI Z KODEM(DANE DO ZAPISU I WCZYTU SIE NIE LICZA)"""





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
