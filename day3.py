integers_list = [1, 2, 3, 4, 5]
print("The list of integers is:", integers_list)


integers_list = [1, 2, 3, 4, 5]
print("The list of integers is:", integers_list)

# Calculate the sum of all elements in the list
sum_of_elements = sum(integers_list)
print("The sum of all elements in the list is:", sum_of_elements)


integers_list = [1, 2, 3, 4, 5]
print("The list of integers is:", integers_list)

# Calculate the sum of all elements in the list
sum_of_elements = sum(integers_list)
print("The sum of all elements in the list is:", sum_of_elements)

# Find the maximum and minimum values in the list
max_value = max(integers_list)
min_value = min(integers_list)

print("The maximum value in the list is:", max_value)
print("The minimum value in the list is:", min_value)



integers_list = [1, 2, 3, 4, 5, 3, 2, 1]
print("The original list of integers is:", integers_list)

# Remove duplicates by converting the list to a set and back to a list
unique_integers_list = list(set(integers_list))
print("The list of integers after removing duplicates is:", unique_integers_list)

integers_list = [1, 2, 3, 4, 5]
print("The original list of integers is:", integers_list)

# Reverse the list without using the reverse() method
reversed_list = integers_list[::-1]
print("The reversed list of integers is:", reversed_list)

# Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the matrix row by row
print("The matrix is:")
for row in matrix:
    print(row)


    # Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Calculate the sum of all elements in the 2D list
sum_of_elements = 0
for row in matrix:
    sum_of_elements += sum(row)

print("The sum of all elements in the 2D list is:", sum_of_elements)


squares = [x**2 for x in range(1, 11)]
print("The list of squares from 1 to 10 is:", squares)

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in original_list if x % 2 == 0]
print("The list of even numbers is:", even_numbers)

# Create a dictionary with student names as keys and their scores as values
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

# Print the dictionary
print("The dictionary of student scores is:", student_scores)

# Create a dictionary with student names as keys and their scores as values
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

# Check if a given key exists in the dictionary
key_to_check = "Charlie"

if key_to_check in student_scores:
    print(f"The key '{key_to_check}' exists in the dictionary.")
else:
    print(f"The key '{key_to_check}' does not exist in the dictionary.")
# Create two dictionaries
dict1 = {
    "Alice": 85,
    "Bob": 92
}

dict2 = {
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

# Merge the two dictionaries
merged_dict = {**dict1, **dict2}

# Print the merged dictionary
print("The merged dictionary is:", merged_dict)

# Create a nested dictionary with students' names and their marks in different subjects
students_marks = {
    "Alice": {"Math": 85, "Science": 90, "English": 88},
    "Bob": {"Math": 78, "Science": 82, "English": 80},
    "Charlie": {"Math": 92, "Science": 88, "English": 91},
    "David": {"Math": 75, "Science": 85, "English": 78},
    "Eve": {"Math": 89, "Science": 92, "English": 90}
}

# Print the nested dictionary
print("The nested dictionary of students' marks is:", students_marks)

squares_dict = {x: x**2 for x in range(1, 6)}
print("The dictionary of numbers and their squares is:", squares_dict)