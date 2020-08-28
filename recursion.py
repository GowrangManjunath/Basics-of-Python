##Sum of consecutive numbers using recursive function 

def number(n): ##recursion function
  if n == 1 :
     return n  ## If number is 1 will return 1
  else:
     return n + number(n-1) ## else will call the recursive function to add until it is decremented

n= int(input())
print (number(n))
