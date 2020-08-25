# to perform exponential calculation

a=int(input("Enter the number:")) # denominator value
b=int(input("Enter the power:"))  # power of freedom
c=1                               # intialize a not null value
for i in range( 0, b, 1):         # for loop for multiplying the power
    c=c*a                         # multiplying the denominator number
    print("Exp value of ",a,"^",i+1,"=",c) #printing the value