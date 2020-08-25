s = input("Enter your word:")
def isPalindrome(s): 
    return s == s[::-1] 
ans = isPalindrome(s) 
if ans: 
    print("Yes it is a plaindrome") 
else: 
    print("No it is not a plaindrome") 
