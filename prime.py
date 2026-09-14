#Develop a Python program to check whether a given number is a prime number or not using loops.

n = int(input("Enter number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")