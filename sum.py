#Develop a Python program to solve basic computational problems by accepting user input and performing 
# arithmetic and logical operations such as finding the area of a circle, checking leap years, and determining 
# the largest of three numbers.

r=int(input("Enter radius :"))
area=3.14*r*r
print("Area=",area)

year = int(input("Enter year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
c=int(input("Enter third number :"))

if a >= b and a >= c:
    print("Largest =", a)
elif b >= a and b >= c:
    print("Largest =", b)
else:
    print("Largest =", c)