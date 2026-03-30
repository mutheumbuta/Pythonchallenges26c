#question 3

l1 = [10, 20, 30, 40, 50]
print(sum(l1))

#queation 2
l1 = [43, 89, 67, 56, 12]
print(max(l1))

#question 1
""" this is a function that creates a list of words and sorts list in ascending order """
words = ['cat', 'dog','mouse', 'zebra', 'antelope']
#user to input words needed to be sorted in ascending
words.sort()
print('ascending order:', words)

#descending order

words.sort(reverse=True)
print('Descending order:', words)

#question 4
list2 = [23, 45, 67, -10, 23, 50, -10]

ammended_list =[]

for num in list2:
    if num not in ammended_list:
        ammended_list.append(num)
print('The new list will be:', ammended_list)

#question 5

#create a list of numbers
numbers = [3214, 6534, 65, 876, 54]
# return each element with index
for element, index in enumerate(numbers):
    print('Element:', element, 'index:', index)

#Question 6
student = ('Nancy Mutheu','16','A')
print('The student record is:', student)

#question 7
# Tuple 
operators = ('+', '-', '*', '/')

# user to input values
num1 = float(input("Enter the first number: " ))
num2 = float(input("Enter the second number: " ))

# Display available operators
print("Available operators:", operators)

# Ask the user to choose an operator
op = input("Choose an operator from the tuple: ")

# Perform calculation based on chosen operator
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operator!"

# Display the result
print("Result:", result)
