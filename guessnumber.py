import random
n = random.randint(1,10)
for i in range(0,3):
   user=int(input("guess the number:"))
   if user == n:
       print("hurray!!")
       print(f"you guessed number is right it is {n}")
       break
   elif user > n:
       print("you guessed number is too high")
   elif user < n:
       print("you guesses number is too low ")
else:
   print(f"Nice try!,but the number is {n}")
