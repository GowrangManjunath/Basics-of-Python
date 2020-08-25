#This code represents to check whether the given number is a Odd or a Even Number
print ("Enter a number")
a=int(input())

if a%2 == 0 :               #if condition is used to check whether it gives remainder as 0
    print("Its even")
else :
    print("Its odd")



#This code checks whether the entered number is Prime or not
if a>1:                  
    for i in range(2,a):       #For loop checks from 2 which is the smallest prime number till the entered number
        if a %i==0:            #if the entered number is divisble by the entered number then its prime 
            print("Its not a prime number")
            break

        else :
            print("Its a prime number")
            break
else:                           #if the entered number is less than 1 it executes this else statement 
    print("Its not a prime number")
