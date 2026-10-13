def display_header():
    print("STUDENT PERFORMANCE EVALUATOR")
display_header()

student_info = input("Enter student name: ")

def get_student_info():
    get_student_info()

a1 = int(input("Enter your score in Assessment 1: "))
a2 = int(input("Enter your score in Assessment 2: "))
a3 = int(input("Enter your score in Assessment 3: "))
avg = (a1 + a2 + a3) / 3

def evaluate_performance():
    avg = (a1 + a2 + a3) / 3
    print(f"Average score: {avg}")

print(f"Student Name: {student_info}")
print(f"Assessment Scores: {a1},{a2},{a3}")
evaluate_performance()

if avg >= 90 and avg <= 100:
    print("Performance Level: Outstanding")
elif 85 <= avg < 90:
    print("Performance Level: Very Satisfactory")
elif 80 <= avg < 85:
    print("Performance Level: Satisfactory")
elif 75 <= avg < 80:
    print("Performance Level: Fairly Satisfactory")
elif 75 < avg:
    print("Performance Level: Needs Improvement")
