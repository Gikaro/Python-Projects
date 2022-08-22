#
# class Department:
#     def __init__(self, Department_name, students):
#         self.Department_name = Department_name
#         self.students = students

#class Students:
    # def __init__(self, firstname, secondname, course, year):
    #     self.firstname = firstname
    #     self.secondname = secondname
    #     self.course = course
    #     self.year = year

#return fxn can be use inside a function or method to send the function's result back to the caller.

# Departmentlist = []
#
# number = int(input("Enter the number of department: "))
#
# for i in range(number):
#     d = input("Enter name of department" + str(i) + ": " )
#     s = int(input ("Enter the number of students in this department: "))
#
#     students = []
#
#     for k in range(s):
#         print("###Student " +str(k)+" details##### ")
#         f = input("Enter firstname: ")
#         s = input("Enter secondname: ")
#         c = input("Enter course: ")
#         ys = input("Enter year of study: ")
#
#         j = Students(f,s,c,ys)
#         students.append(j)
#
#     h = Department(d,students)
#     Departmentlist.append(h)
# for n in Departmentlist:
#     print(n.Department_name)
#     for l in n.students:
#         print(l.secondname)

###School project demo

print("Welcome to self set school system")
# PSW = "Caleb123"
# password = input("Please enter the password: ")
# i = 0
# if password == PSW:
#     print("Welcome")

    class Schools:
        def __init__(self, School_name, department):
            self.School_name = School_name
            self.department = department

    class Department:
        def __init__(self, department_name, Students):
            self.department_name = department_name
            self.Students = Students

    class Students:
        def __init__(self,admision_no, first_name, last_name, year_of_study, course):
            self.admision_no = admision_no
            self.first_name = first_name
            self.last_name = last_name
            self.year_of_study = year_of_study
            self.course = course

    m = input("Enter the name of your school: ")
    print("Welcome to " +str(m)+ " ***" )
    Schoollist = []

    Nums = int(input("Enter the number of schools in "+str(m)+ " : "))
    for s in range(Nums):
        l_school = input("Enter the name of school " +str(s)+ ": " )
        n_depat = int(input("How many departmts are in this school: "))
        for k in range(n_depat):

            Departmentlist = []
            l_department = input("Enter the name of deparment " + str(k)+ ": ")
            n_students = int(input("How many students are in this department: "))
            for c in range(n_students):

                Studentlist = []
                print("Please enter the details of student "+str(c)+" ##")
                adm = input("admision number: ")
                fn = input("First name: ")
                ln = input("Last name: ")
                ys = input("Year of study: ")
                cs = input("course of study: ")

                b = Students(adm, fn, ln,ys,cs)
                Studentlist = Studentlist.append(b)

            d =  Department(l_department, Students)
            Departmentlist = Departmentlist.append(d)

        s = Schools(l_school, Department)
        Schoollist = Schoollist.append(s)

    for z in Schoollist:
        print(z.School_name)

# elif password != PSW:
#     for i in range(2):
#         print("Incorrect password!")
#         password = input("Please enter the password: ")
#     print(" Sorry! Run the program again")
