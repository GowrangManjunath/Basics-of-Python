#Program to print Multiplication table between the user inputted range
print("Enter the first number")
num = int(input())
print("Enter the second number")
num1 = int(input())
for j in range(num,num1+1):   #for loop for first and second input
    for i in range(1, 11):    #multiplication range  
        print("% -5d X % -5d = %5d" % (j,i,j*i))  #Printing the output
        
