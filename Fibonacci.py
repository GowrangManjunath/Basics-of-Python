n = int(input("Enter the value of 'n': ")) # take the value from the user (eg n=3)
a = 0                                      # declaring the first value to 0
b = 1                                     # declaring second value to 1 for the fibonacci series
sum = 0                                     # initializing the value of sum to 0 ( to flush the junk value)
count = 1                                   # Count is initialized to 0 for iteration purpose
print("Fibonacci Series: ")                 # print disclaimer
while(count <= n):                        # when count is less than equal to the n value given by the user (eg 1<=3)
  print(sum)                              # print sum first such that even 0 is printed
  count+= 1                               # increment count to +1 for iteration
  a = b                                   # swap value of a with b (eg a=1)
  b = sum                                 # swap value of b with sum (eg b=0)
  sum = a + b                             # add a and b store in sum (eg sum=1)
                                          # and so on for the second iteration
  # if n=3 output would be 0,1,1