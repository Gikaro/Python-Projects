# class Student:
#     def __init__(self,firstname, secondname, age, subject=0):
#         self.firstname = firstname
#         self.secondname = secondname
#         self.age = age
#         self.subject = subject
#
#
#     def add30(self):
#         return self.age + 30
#
#     def fullname(self):
#         return self.firstname + " " + self.secondname
# i = 0
# mylist = []
# number = int(input("Please enter the number of student: "))
# for i in range(number):
#     x = input("Please enter firstname, secondname, age, seperated by comas: ").split(",")
#     x = Student(x[0], x[1], x[2])
#     mylist.append(x)
#
#
#
# def addage(list):
#
#     k = 0
#     for i in mylist:
#         k += int(i.age)
#         return(i)
#
# for i in mylist:
#     print(i.secondname)

class Department:
    def __init__(self, Department_name, students):
        self.Department_name = Department_name
        self.students = students

class Students:
    def __init__(self, firstname, secondname, course, year):
        self.firstname = firstname
        self.secondname = secondname
        self.course = course
        self.year = year

#The Python return can be use inside a function or method to send the function's result back to the caller.

Departmentlist = []

number = int(input("Enter the number of department: "))

for i in range(number):
    d = input("Enter name of department" + str(i) + ": " )
    s = int(input ("Enter the number of students in this department: "))

    students = []

    for k in range(s):
        print("###Student " +str(k)+" details##### ")
        f = input("Enter firstname: ")
        s = input("Enter secondname: ")
        c = input("Enter course: ")
        ys = input("Enter year of study: ")

        j = Students(f,s,c,ys)
        students.append(j)

    h = Department(d,students)
    Departmentlist.append(h)
for n in Departmentlist:
    print(n.Department_name)
    for l in n.students:
        print(l.secondname)
