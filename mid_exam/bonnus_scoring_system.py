import math

number_of_students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
list_of_bonus = []
student_attendance = {}

for _ in range(number_of_students):
    student_attendance[int(input())] = ''

for student in student_attendance:
    total_bonus = student / number_of_lectures * (5 + additional_bonus)
    student_attendance[student] = math.ceil(total_bonus)

if not student_attendance:
    max_bonus = 0
    student_attendance[max_bonus] = 0

max_bonus = max(student_attendance)

print(f'Max Bonus: {student_attendance[max_bonus]}.')
print(f'The student has attended {max_bonus} lectures.')

