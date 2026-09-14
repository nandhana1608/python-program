#6. Develop Python programs using lists, list comprehensions, and built-in list methods to create, search,
#  update, filter, and manipulate collections of data
# Read list from user
numbers = list(map(int, input("Enter numbers: ").split()))

print("Original list:", numbers)

# Search
search = int(input("Enter number to search: "))

if search in numbers:
    print(search, "is present")
else:
    print(search, "is not present")

# Update
old = int(input("Enter number to update: "))
new = int(input("Enter new value: "))

if old in numbers:
    index = numbers.index(old)
    numbers[index] = new
    print("Updated list:", numbers)

else :
    print(old, "is not present")

# List comprehension - filter even numbers
even = [x for x in numbers if x % 2 == 0]
print("Even numbers:", even)

# Add
element = int(input("Enter element to add: "))
numbers.append(element)
print("After adding:", numbers)

# Remove
element = int(input("Enter element to remove: "))

if element in numbers:
    numbers.remove(element)
    print("After removing:", numbers)
else:
    print(element, "is not present")

# Sort
numbers.sort()
print("Sorted list:", numbers)

# Reverse
numbers.reverse()
print("Reversed list:", numbers)