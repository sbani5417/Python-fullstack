Items=[100,600,200,400]
Total_order_value=sum(Items)
if len(Items)>0:
    Average_price=Total_order_value/len(Items)
else:
    Average_price=0
print("total order value:",Total_order_value)
print("Average_price:",Average_price)
