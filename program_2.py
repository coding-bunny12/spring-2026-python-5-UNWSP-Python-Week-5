# Abrielle Nyei
# 2/21/26
# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247
# +   129
# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.

import random

# Function to check the student's answer
def check_answer(num1, num2, student_answer):
    correct_answer = num1 + num2
    if student_answer == correct_answer:
        print("Congratulations! That is correct.")
    else:
        print("Sorry, that is incorrect.")
        print("The correct answer is:", correct_answer)

# Main function
def main():
    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    print(f"    {num1}")
    print(f"+   {num2}")
    print("------")

    student_answer = int(input("Enter your answer: "))
    check_answer(num1, num2, student_answer)

main()
