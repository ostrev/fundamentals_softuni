first_employ = int(input())
second_employ = int(input())
third_employ = int(input())
student = int(input())
total_student_per_hour = first_employ + second_employ + third_employ

hours = 0

while not student <= 0:
    hours += 1
    student -= total_student_per_hour
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
