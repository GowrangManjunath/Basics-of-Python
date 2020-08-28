#to calcualte emi for 1000000 for a period of two years at 8% interest
p = 1000000 #loan ampunt
n = 2       #time period
r = 0.08    #interest rate
d = ((p*r*pow(1+r,n))/ (pow (1+r,n-1))) #this is the formula to calculate EMI
print("the emi for", p ,"is", d)
#using functions to calcualte emi for 1000000 for a period of two years at 8% interest
def emi_payment(): 
	emi = (p*r*(1+n)*r)//((1+r)*n-1)
	print(emi)
p = 1000000
n = 2
r = 0.08
d = emi_payment()
