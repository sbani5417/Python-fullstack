Courses={
    "Python Programming":5000,
    "Data Analysist":8000,
    "AI&ML":12000
    }
Course_name=input("Enter a Course:")
is_student=input("Are you a student(yes\no):")
is_early_registration=input("Are you early registered(yes\no):")
if Course_name not in Courses:
    print("Course not found:")
else:
    Original_fees=Courses[Course_name]
    discount=0
if is_student=="yes":
    discount+=0.10
if is_early_registration=="yes":
    discount+=0.05
total_discount=Original_fees*discount
final_fees=Original_fees-total_discount
print("Course name:",Course_name)
print("Original fees:",Original_fees)
print("total_discount:",total_discount)

