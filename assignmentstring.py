#question 1
word_num = 'I love my python class'
print(len(word_num))

"""Function to check if two strings are anagrams"""
def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for uniform comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Compare sorted versions of both strings
    return sorted(str1) == sorted(str2)

# Input strings from the user
string1 = input("Enter the first string\n ")
string2 = input("Enter the second string\n")

# Check and display result
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')


#question 2

import string
"""function to check if string is a palindrome"""

def is_palindrome(s):
    # Remove punctuation and spaces, and convert to lowercase
    translator = str.maketrans('', '', string.punctuation + " ")
    cleaned = s.translate(translator).lower()
    
    # Check if cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Take input from the user
user_input = input("Enter a string\n ")

# Check and display result
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')



#Question 6
# open file in read mode
#input name of the file

fname = input('Enter the file name\n')

file = open(fname)

# Iterate through each line in the file
for line in file:
    print(line.strip())
file.close()

#Question5
#take input from the user
fname = input('Enter the file name\n')

# Open the existing file in read mode
with open(fname, "r") as file1:
    content = file1.read()

# Create a new file and write the copied content
with open("copied.txt", "w") as file2:
    file2.write(content)

print("copied successfully.")
