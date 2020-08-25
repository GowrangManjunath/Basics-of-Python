#this code uses function to check for palindrome of a string
s = input("Enter your word:")
def isPalindrome(s): 
    return s == s[::-1]   #This step revereses the string which is entered by the user and then checks if the entered string and reversed string is same or not
ans = isPalindrome(s) #Here we are returning the function and the resturned function is checked in the if and else statement
if ans: 
    print("Yes it is a plaindrome") 
else: 
    print("No it is not a plaindrome") 
