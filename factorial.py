#Develop a Python program to generate the factorial of a given number using looping statements.
n=int(input("Enter n:"))
factorial=1
for i in range(1,n+1):
  factorial= factorial*i
print("factorial=",factorial)