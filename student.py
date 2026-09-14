#9. Develop a modular Python program for a Student Performance Analysis System using user-defined functions and
#  lambda expressions. The program should accept marks of students, compute the total, average, highest, and lowest
# marks using user-defined functions, determine the grade, and use lambda expressions to sort students based on the
# ir total marks.
# Student Performance Analysis System

def total_marks(marks):
    return sum(marks)

def average_marks(marks):
    return sum(marks) / len(marks)

def highest_marks(marks):
    return max(marks)

def lowest_marks(marks):
    return min(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input("Enter student name: ")

    marks = []

    for j in range(3):
        mark = int(input("Enter mark: "))
        marks.append(mark)

    total = total_marks(marks)
    average = average_marks(marks)
    highest = highest_marks(marks)
    lowest = lowest_marks(marks)
    g = grade(average)

    students.append((name, total, average, highest, lowest, g))


print("\nComplete Student Performance")

for student in students:
    print("Name:", student[0])
    print("Total:", student[1])
    print("Average:", student[2])
    print("Highest:", student[3])
    print("Lowest:", student[4])
    print("Grade:", student[5])
    print()


students.sort(key=lambda x: x[0])

print("Sort students name by Total marks")

for student in students:
    print(student[0], "-", student[1])