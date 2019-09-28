students = {'name': 'Jon', 'age': 25, 'courses': ['Math', 'Comp Sci']}

for key, value in students.items():
    print(key, value)


# looping without key, value

for i in students:
    print(i, students[i])