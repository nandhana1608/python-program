#7. Write Python programs to perform operations on dictionaries and sets, including sorting,
#  merging, frequency counting, and identifying common or unique elements.
# DICTIONARY

d1 = {"a": 3, "b": 1, "c": 2}
d2 = {"d": 4, "e": 5}
print("Dictionary 1:", d1)
print("Dictionary 2:", d2)

# Sorting
print("Sorted dictionary:", dict(sorted(d1.items())))

# Merging
d1.update(d2)
print("Merged dictionary:", d1)

# Frequency counting
numbers = ["a", "b", "b", "c", "c", "c"]
frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1
print("Frequency:", frequency)

# SET

set1 = {4, 2, 1, 3}
set2 = {3, 4, 5, 6}
print("Set 1:", set1)
print("Set 2:", set2)

# Sorting
print("Sorted set:", sorted(set1))

# Merging
print("Merged set:", set1 | set2)

frequency_set = {}

for x in set1:
    frequency_set[x] = 1

print("Set frequency:", frequency_set)

# Common elements
print("Common set elements:", set1 & set2)

# Unique elements
print("Unique set elements:", set1 ^ set2)