#5. Write Python programs to perform string processing operations, including character replacement,
#string reversal, checking palindromes, and counting character and word frequencies.
s = input("Enter a string: ")

# Character replacement
old = input("Enter character to replace: ")
new = input("Enter new character: ")
print("Replaced string:", s.replace(old, new))

# String reversal
print("Reversed string:", s[::-1])

# Palindrome checking
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Character frequency
print("Character frequency:")
for ch in set(s):
    print(ch, ":", s.count(ch))

# Word frequency
print("Word frequency:")
words = s.split()
for word in set(words):
    print(word, ":", words.count(word))