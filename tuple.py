course=("Java",3,1200,1200)
print(course[1])
print(course[-1])
print(course[0:2])

print(course.count(1200))
print(course.index(3))
print(course)

cou=list(course)
cou.pop()
course=tuple(cou)
print(course)
