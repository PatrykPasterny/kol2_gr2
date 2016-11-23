from szkola_poprawione import *
def main():
	class1A={"students":{},"class_average":0,"class_attendance":0.}
	class1B={"students":{},"class_average":0,"class_attendance":0.}
	highschool=[class1A,class1B]
	class_students={}
	amount_of_students=0
	amount_of_classes=0
	student={"name":"", "surname":"", "marks":[],"attendance":[]}
	student_keys=["name","surname","marks","attendance"]
	infile=file('uczniowie.txt','r')
	for line in infile:
		line=line.strip('\n').split(" ")

		if line[0]=="KLASA" or line[0]=="KONIEC":
			if amount_of_students!=0 or amount_of_classes!=0:
				highschool[amount_of_classes]["students"]=class_students
				class_students={}
				amount_of_students=0
				amount_of_classes+=1

		else:
			N=len(line)
			for x in range(N):
				student[student_keys[x]]=line[x]
			class_students[amount_of_students]=student

			amount_of_students+=1
			student={"name":"", "surname":"", "marks":[],"attendance":[]}
	"WSZYSTKIE KLASY"
	print_school(highschool,student_keys)
	print "SREDNIE I OBECNOSCI POSZCZEGOLNYCH UCZNIOW"
	print_students_average_and_attendance(highschool)
	print "SREDNIE I OBECNOSCI POSZCZEGOLNYCH KLAS"
	fill_av_and_att_in_school(highschool)
	print_class_average_and_attendance(highschool)
	print "\n"
	print "SREDNIE I OBECNOSCI WSZYSTKICH KLAS: "

	print_school_average_and_attendance(highschool)

if __name__=="__main__":
	main()
