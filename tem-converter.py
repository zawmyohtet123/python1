city=input("Enter the name of city:")
c=input("Enter the temperature of the "+city+" in Celcius:")
def convert(x):
   f=int(c)+32
   return f
ff=convert(c)
print("Temperature of the",city," in Fahrenheit is ", ff)
