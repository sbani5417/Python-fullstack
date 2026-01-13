def simple_interest(p,r,t):
    return(p*r*t)/100
principal=3500
rate=5
time=2
interest=simple_interest(principal,rate,time)
print(f"The simple interest is:{interest}")
