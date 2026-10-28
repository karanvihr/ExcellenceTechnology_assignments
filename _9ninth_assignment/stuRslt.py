


class StuRslt:

    _students = [ 
        ["harman1",4,[82,94,66,74,96]],
        ["karan",1,[90,95,82,75,87]],
        ["mohan",2,[89,78,72,65,90]],
        ["saransh",3,[78,97,88,81,79]],
        ["hamran",6,[10,20,30,40,50]],
        
    ]

    def __init__(self,name,rollno,*marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks


    def studentResult(self):
        """Adds all no.s and calculate student percentage"""
        for s in self._students:
            if s[0] == self.name and s[1] == self.rollno:
                rslt =  sum(s[2])/(len(s[2]))
                print("\nResult: ",end="")
                if rslt >= 90:
                    return f"A grade {rslt}\n"
                elif rslt >= 80:
                    return f"B grade {rslt}\n"
                elif rslt >= 70:
                    return f"C grade {rslt}\n"
                elif rslt >= 60:
                    return f"Pass {rslt}\n"
        if self.rollno not in self._students:
            return f"{self.name} does not exist."


    @classmethod
    def findTopper(cls):
        ss = list()
        mrkslist=[]
        ss = cls._students
        
        # finding the maximum marks
        for s in range(0,(len(ss))):
            mrkslist.append(sum(ss[s][2]))
        
        # finding the student
        for s in range(len(ss)):
            if max(mrkslist) == sum(ss[s][2]):
                return ss[s]
    

    
    def display(self):
        print(f"Name {self.name}, Rollno. {self.rollno}")
        print("Marks :",end=" ")
        for i in self.marks:
            print(i,end=", ")
        print()

    @classmethod
    def addStudent(cls):
        n = input("Enter name: ")
        r = int(input("Enter rollno.: "))
        m = input("enter marks separated by spaces: ").split()
        
        m = [int(x) for x in m ]
        cls._students.append([n,r,m])

    @classmethod
    def showStudents(cls):
        print(cls._students)

    @classmethod
    def classAvg(cls):
        total = 0
        for s in cls._students:
            total += sum(s[2])
        return (f"\nAverage Marks Obtained By a Student: {total/len(cls._students)}\n")


    @classmethod
    def passedStudent(cls):
         return filter(lambda x: sum(x[2])>=165,cls._students)


    @classmethod
    def failedStudent(cls):
        return filter(lambda x: sum(x[2])<=165,cls._students)






# user provides data to create an object then an object is passed to the class __init__
    def run():
        import time
        exit = True
        while(exit):

            print("\n\n1. Add Student\n\n2. Student Result\n\n3. Find Topper\n\n4. Class Average\n\n5. Passed Students\n\n6. Failed Students\n\n7. Exit")
            print("\nEnter The serial Number Of The Operation: ")
            val = int(input())
            if val == 1:
               StuRslt.addStudent()
               print("Student has been added succecfully.")
               time.sleep(2)
    
            elif val == 2:
                name = input("Enter your name: ")
                print()
                rollno = int(input("Enter your roll no.: "))
                print()
                s1 = StuRslt(name,rollno)
                print(s1.studentResult())
                time.sleep(2)


            elif val == 3:
                tp = StuRslt.findTopper()
                print(f"\nTopper in the class is: [{tp[0]} , {tp[1]}].\n")
                time.sleep(2)


            elif val == 4:
                clsavg = StuRslt.classAvg()
                print(clsavg)
                time.sleep(2)

            elif val == 5:
                print("\nList of Passed Students are:")
                for item in list(StuRslt.passedStudent()):
                    print(f"Name: {item[0]},\t Rollno.: {item[1]}")
                print()
                time.sleep(1)


            elif val == 6:
                print("\nList of Failed Studennts are:")
                StuRslt.failedStudent()
                print()
                time.sleep(2)


            elif val == 7:
                exit = False
                print("Thanks for your valuable time.")
                time.sleep(2)


            else:
                print("\nInvalid Input! \nEnter a valid number.\n")
                time.sleep(1)




























































# class StudentResult:

#     global students 
#     students = [("karanveer",22,445),("ravi",23,340),("kishan",24,430),]
#     exit = True
#     # def __init__():
#     rollno = int(input("enter your roll no."))
#     def addStudent(self,name,rollno,*marks):
#         self.name = name
#         self.rollno = rollno
#         self.marks = sum(marks)
#         students.append((self.name,self.rollno,self.marks))


#     def viewStudentResult(self,rollno):
        
        
#        print()


#     def findTopper():
#         #   rollno
#         pass

#     def failedStudents():

#         for student in students:
#             if student[2]<165:
#                 print(student)


#     def passedStudents():

#         for student in students:
#             if student[2]>165:
#                 return(student)

#     def classAverage():
#         total = 0
#         for student in students:
#             total = total + student[2]

#         return(total/len(students))





#     def userLogin():
#         rollno = input("enter your rollno.")

#          # checking if the student exist
#         for student in students:
#             if rollno == students[student][1]:
#                 print(f"welcome {student[0]} \nyou have logged in succesfully")
#             else:
#                 print("student does not exist")
#                 # StudentResult.addstudent()

# obj = StudentResult()
# while(exit):
#     print("Press 1 to add student.")
#     print("Press 2 to see find topper.")
#     print("Press 3 to see class average.")
#     print("press 4 to see Passed students.")
#     print("Press 5 to see Failed students.")
#     print("Press 6 to 'Exit'.")


#     usr_inpt  = int(input("Enter Number"))
#     if usr_inpt == 6:
#         exit = False
#     elif usr_inpt == 5:
#         obj.failedStudents()
#     elif usr_inpt == 4:
#         StudentResult.passedStudents()
#     elif usr_inpt == 3:
#         StudentResult.classAverage()
#     elif usr_inpt == 1:
#         obj.addStudent("ankita",1,459)