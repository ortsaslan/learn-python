student_scores = {
    "Harry": 82,
    "Ron": 71,
    "Hermione": 96,
    "Draco": 79,
    "Neville": 61
}

student_grades = dict()

for student in student_scores:
    score = student_scores[student]
    grade = ""

    if 91 <= score <= 100:
        grade = "Outstanding"
    elif 81 <= score <= 90:
        grade = "Exceeds Expectations"
    elif 71 <= score <= 80:
        grade = "Acceptable"
    elif score < 71:
        grade = "Fail"

    student_grades[student] = grade
    
for student in student_grades:
    print(f"{student}: {student_grades[student]}")