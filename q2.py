"""Exercise: List Comprehension Mastery
Practice Problem: Write a single-line list comprehension that takes a list of strings, filters out strings shorter than 4 characters, and converts the remaining strings to uppercase.

Exercise Purpose: List comprehensions are a hallmark of Pythonic code. They allow you to replace verbose for loops and .append() calls with a readable, optimized single line. This exercise teaches you how to combine transformation (uppercase) and filtering (length check) in one expression.

Given Input: words = ["apple", "bat", "cherry", "dog", "elderberry"]

Expected Output: ['APPLE', 'CHERRY', 'ELDERBERRY']"""

words = ["apple", "bat", "cherry", "dog", "elderberry"]
new = []

new = [i.upper() for i in words if len(i) >= 4]


print(new)
