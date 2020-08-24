#This program represents Arithemetic operations using switcher case

print("Enter the number 1 ")  #Taking input from the user
x = int(input())
print("Enter the number 2")   #Taking input from the user  
y = int(input())
print("Choose the operation 0-addition,1-subtraction,2-multiplication,3-Division")
i = int(input())              #Taking input for the switcher

def add():                    #function for additon 
    z = x + y
    return z                  #returning the value of z to func  


def sub():                    #function for subtraction
    z = x - y
    return z


def multi():                  #function for multiplication
    z = x * y
    return z

def div():                    #function for division
    z=x // y
    return z


switcher = {                 #switcher is used for selecting the operation
0 : add,
1 : sub,
2 : multi,
3 : div
}
func = switcher.get(i)        
print ("Result is " ,func())
