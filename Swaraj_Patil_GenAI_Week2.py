import pandas as pd
import numpy as np
import random

# Task 1: Python Basics & Operators

# 1. Accept two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# 2. Perform all basic arithmetic operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
modulus = num1 % num2 if num2 != 0 else "Undefined (modulus by zero)"
power = num1 ** num2

# 3. Demonstrate comparison and logical operators
greater = num1 > num2
less = num1 < num2
equal = num1 == num2
not_equal = num1 != num2

# Logical operations
and_op = (num1 > 0) and (num2 > 0)
or_op = (num1 > 0) or (num2 > 0)
not_op = not (num1 > num2)

# 4. Print results using formatted output
print("\n--- Arithmetic Operations ---")
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
print(f"{num1} % {num2} = {modulus}")
print(f"{num1} ** {num2} = {power}")

print("\n--- Comparison Operators ---")
print(f"{num1} > {num2}  → {greater}")
print(f"{num1} < {num2}  → {less}")
print(f"{num1} == {num2} → {equal}")
print(f"{num1} != {num2} → {not_equal}")

print("\n--- Logical Operators ---")
print(f"({num1} > 0) and ({num2} > 0) → {and_op}")
print(f"({num1} > 0) or ({num2} > 0)  → {or_op}")
print(f"not ({num1} > {num2}) → {not_op}")





# Task 2: Lists and Arrays

# 1. Create a list of 10 random integers (between 1 and 100)
numbers = [random.randint(1, 100) for _ in range(10)]
print("Original list:", numbers)

# 2. Perform list operations

# Add an element
numbers.append(55)
print("\nAfter adding 55:", numbers)

# Remove an element (example: remove first element)
removed_value = numbers.pop(0)
print(f"After removing first element ({removed_value}):", numbers)

# Find maximum and minimum values
max_value = max(numbers)
min_value = min(numbers)
print(f"\nMaximum value: {max_value}")
print(f"Minimum value: {min_value}")

# Sort the list
numbers.sort()
print("Sorted list:", numbers)

# 3. Convert the list into a NumPy array
arr = np.array(numbers)
print("\nNumPy Array:", arr)

# Calculate Mean, Median, and Standard Deviation
mean_val = np.mean(arr)
median_val = np.median(arr)
std_val = np.std(arr)

print(f"\nMean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Standard Deviation: {std_val:.2f}")





# Task 3: Dictionaries and Sets

# 1. Create a dictionary named student with keys: name, course, marks
student = {
    "name": "Swaraj",
    "course": "Artificial Intelligence",
    "marks": 85
}

# 2. Add a new key 'grade' based on marks
if student["marks"] >= 90:
    student["grade"] = "A"
elif student["marks"] >= 75:
    student["grade"] = "B"
elif student["marks"] >= 60:
    student["grade"] = "C"
else:
    student["grade"] = "D"

# 3. Print all keys and values using a loop
print("--- Student Details ---")
for key, value in student.items():
    print(f"{key}: {value}")

# 4. Create two sets of AI tools
set1 = {"Bard", "Claude", "Copilot"}
set2 = {"Gemini", "Copilot", "Perplexity"}

# Display both sets
print("\nSet 1 (AI Tools):", set1)
print("Set 2 (AI Tools):", set2)

# Perform common set operations
print("\n--- Set Operations ---")
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference (Set1 - Set2):", set1.difference(set2))
print("Symmetric Difference:", set1.symmetric_difference(set2))





# Task 4: File Handling

# 1. Create a text file named ai_students.txt and write details of 5 students
students = [
    {"name": "Swaraj", "marks": 85, "grade": "A"},
    {"name": "Ananya", "marks": 72, "grade": "B"},
    {"name": "Rohit", "marks": 91, "grade": "A"},
    {"name": "Meera", "marks": 68, "grade": "C"},
    {"name": "Aarav", "marks": 78, "grade": "B"}
]

# Write student details into the file
with open("ai_students.txt", "w") as file:
    for s in students:
        file.write(f"{s['name']}, {s['marks']}, {s['grade']}\n")

print("Data written to ai_students.txt successfully!")

# 2. Read the file and display students who scored above 75 marks
print("\n--- Students with Marks > 75 ---")
with open("ai_students.txt", "r") as file:
    for line in file:
        name, marks, grade = line.strip().split(", ")
        marks = int(marks)
        if marks > 75:
            print(f"Name: {name}, Marks: {marks}, Grade: {grade}")





# Task 5: Real-World Mini Project
# File: ai_prompt_logger.py

from datetime import datetime

# 1. Accept user input (simulating an AI prompt)
prompt = input("Enter your AI prompt: ")

# 2. Prepare log entry with timestamp
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{timestamp}] {prompt}\n"

# 3. Append the prompt to 'prompt_history.txt'
with open("prompt_history.txt", "a") as file:
    file.write(log_entry)

print("\nPrompt saved successfully in 'prompt_history.txt'!")            