intername=input("enter name:")
age=int(input("enter age:"))
email=input("enter email:")
contact=input("enter contact:")
grad=float(input("enter grad:"))
if age>=18:
   if grad>=60:
     if len(contact)==10:
       print("intern eligible for internship")
     else:
       print("contact number must be 10 digit")
   else:
     print("grad must be greater than 0")
else:
  print("age must be greater than 18")
