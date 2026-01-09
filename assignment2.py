Intern_name=input("Employee name:")
Employee_id=int(input("Enter id:"))
Basic_salary=float(input("Basic_salary:"))
HRA=0.20*Basic_salary
DA=0.10*Basic_salary
PF=0.12*Basic_salary
Net_salary=Basic_salary+HRA+DA-PF
print("HRA is:",HRA)
print("DA is:",DA)
print("PF is:",PF)
print("Netsalary is:",Net_salary)
