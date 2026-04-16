n, x = map(int, input().split())
marks_by_subject = []
for _ in range(x):
    marks_by_subject.append(map(float, input().split()))
for student_marks in zip(*marks_by_subject):
    print(sum(student_marks) / x)
