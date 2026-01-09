Employee_name=input("Enter Employee Name:")
Salary=float(input("Enter Employee Salary:"))
performance_rating=int(input("Enter performance_rating(1to5):"))
if performance_rating==5:
    bonus=Salary*0.20
elif performance_rating==4:
    bonus=Salary*0.15
elif performance_rating==3:
    bonus=Salary*0.10
else:
    bonus=0
bonus_amount=Salary * bonus
Final_Salary=Salary + bonus_amount
print("Employee_name:",Employee_name)
print("performance_rating:",performance_rating)
print("bonus_amount:",bonus_amount)
print("Final_Salary:",Final_Salary)
