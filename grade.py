def average(marks):
    return sum(marks) / len(marks)

def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

def is_pass(marks):
    return all(mark >= 40 for mark in marks)

marks = []

n = int(input("Enter Number of Subjects: "))

for i in range(n):
    mark = int(input(f"Enter Marks {i + 1}: "))
    marks.append(mark)

avg = average(marks)

print("\n===== STUDENT RESULT =====")
print("Average:", round(avg, 2))
print("Grade:", grade(avg))
print("Status:", "PASS" if is_pass(marks) else "FAIL")