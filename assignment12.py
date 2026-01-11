distance=float(input("Enter the delivery distance in km:"))
if distance<=5:
    print("category is Local")
elif 6<= distance<=20:
    print("category is City")
else:
    print("category is Outstation")

