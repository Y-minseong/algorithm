students = set(range(1, 31))

submitted = {int(input()) for _ in range(28)}

not_submitted = sorted(students - submitted)

for student in not_submitted:
    print(student)
