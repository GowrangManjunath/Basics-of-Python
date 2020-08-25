#This program is a simple way to check the entered word is a palindrome
print("Enter the string")
str1=str(input())
rev=reversed(str1)       #Reversed function is used to reverse the string
if list(str1)==list(rev):
    print("Palindrome")
else:
    print("Not a palindrome")


#This program is used to check whether the entered number is palindrome
print("Enter the number ")
num=int(input())
temp=num                #temporary variable is used to store the original value
b=0
while(num>0):           #while loop for executing the statements
    d=num%10            #d is storing the remainder of the entered number
    b=b*10 + d          #b will store the result of the remainder(d) 
    num=num//10
if(temp==b):            #if loop is used to compare the temp and the result(b)
    print("The number is palindrome")
else:
    print("The number is not palindrome")

    
