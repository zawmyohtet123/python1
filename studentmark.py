class calculator:
   def __init__(self,number1,number2):
       self.number_1 = number_1
       self.number_2 = number_2

   def add(self):
       return self.number_1 + self.number_2

   def substract(self):
       return self.number_1 - self.number_2

   def multiple(self):
       return self.number_1 * self.number_2

   def divide(self):
       return self.number_1 / self.number_2

   def decision(self,user_decision):
       if user_decision == "+":
           return self.add()
       elif user_decision == "-":
           return  self.substract()
       elif user_decision == "*":
           return self.multiple()
       elif user_decision == "/":
           return self.divide()

   while True:
       user_input = input("please type your calculation:")
       user_input = user_input.strip().split(" ")

       user_number_1 = int(user_input[0])
       user_number_2 = int(user_input[2])
       decision = user_input[1]

       calc = calculator(user_number_1,user_number_2)
       result = calc.decision(decision)
       print(result)

       furture_calculation = input("do u want to make my furtur calculation: ")
       if furture_calculation.lower()[0] == "y":
           continue
       else:
           break
