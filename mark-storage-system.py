StudentName = []
StudentMarks = []

def teacher():
   print("\n" + "To add marks,type 'add'"+ "\n"+"To remove marks,type 'remove'"+ "\n"+
                           "To search marks,type 'search'" + "\n"+ "To exit,type 'exit'")

   teacherInput = input()
   if teacherInput.lower()=="add":
       add()
       teacher()
   elif teacherInput.lower() == "remove":
       remove()
       teacher()
   elif teacherInput.lower() == "search":
       search()
       teacher()
   elif teacherInput.lower() == "exit":
       studentMarkSystem()
   else:
       teacher()

def add():
   name = input("\n" + "Enter student's name for add")
   mark = input("Enter" + name + "'s marks(1-10)")
   studentName.append(name)
   studentMarks.append(mark)

   print(name + "'s marks" + mark + "is added")

def remove():
   nameToRemove = input("\n" + "Enter student's name to remove")
   k=0
   for i in studentName:
       if i == nameToRemove:
           print(nameToRemove + "'s Marks removed.")
           studentName.remove(i)
           studentMarks.remove(studentMarks[k])
           break

       k+=1

      else:

           print(nameToRemove+"does not exist")
           remove()

def search():
   nameToSearch = input("\n" + "Enter student's name to search")

   k=0
   for i in studentName:
       if i==nameToSearch:
           print(nameToSearch + "'s marks:",studentMarks[k])
           break
       k+=1
   else:
       print(nameToSearch + "cannot be found.")

def student():
   user_input3 = input("\n" + "To search marks,type 'search'" + "\n" + "To exit,type 'exit'")
   if user_input3 == "search":
       search()
       student()
   elif user_input3 == "exit":
       studentMarkSystem()
   else:
       student()

def studentMarkSystem():
   print("\n"+"If you are a teacher,type'T'" + "\n"+"If you a student,type 'S'" + "\n" +"If you are a parent,type'P'"
               "\n" + "To exit, type 'E'")
   user_input = input()

   if user_input.lower() == 't':
       teacher()

   elif user_input.lower() == 's':
       student()

   elif user_input.lower() == 'e':
       print("Good Bye User:")
       exit()
   else:
       print("please choose a valid option")
       studentMarkSystem()

studentMarkSystem()

def parents():
   user_input3 = input("\n" + "To search marks,type 'search'" + "\n" + "To exit,type 'exit'")
   if user_input3 == "search":
       search()
       student()
   elif user_input3 == "exit":
       parentMarkSystem()
   else:
       parent()

def parentsMarkSystem():
   print("\n"+"If you are a teacher,type'T'" + "\n"+"If you a student,type 'S'" + "\n" +"If you are a parent,type'P'"
               "\n" + "To exit, type 'E'")
   user_input = input()

   if user_input.lower() == 't':
       teacher()

   elif user_input.lower() == 's':
       student()

   elif user_input.lower() == 'p':
       parents()

   elif user_input.lower() == 'e':
       print("Good Bye User:")
       exit()
   else:
       print("please choose a valid option")
       parentsMarkSystem()

parentsMarkSystem()
