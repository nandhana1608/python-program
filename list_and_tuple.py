#8. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a 
#tuple which contains every number. Suppose the following input is supplied to the program: 34, 67, 55, 33, 12, 98.
#Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34','67', '55','33', '12', '98'). Write a
#  Python program that accepts a sequence of comma-separated numbers from the console and generates a list and a
#  tuple containing every number. Display the generated list and tuple, the total number of elements, the first
#  and last elements, and the list in reverse order.

# Input
numbers = input("Enter comma-separated numbers: ")

# Create list
num_list = numbers.split(',')

# Create tuple
num_tuple = tuple(num_list)

# Display results
print("Generated List:", num_list)
print("Generated Tuple:", num_tuple)
print("Total number of elements:", len(num_list))
print("First element:", num_list[0])
print("Last element:", num_list[-1])
print("List in reverse order:", num_list[::-1])