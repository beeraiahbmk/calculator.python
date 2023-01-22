def addition(a,b):
    ans=a+b
    return ans
def substraction(a,b):
    ans=a-b
    return ans
def multiplication(a,b):
    ans=a*b
    return ans
def division(a,b):
    ans=a/b
    return ans
def floor_division(a,b):
    ans=a//b
    return ans
def modulus(a,b):
    ans=a%b
    return ans
def factorial(a):
    fact=1
    for i in range(2,a+1):
        fact*=i
    return fact
def prime_not(a):
    if a>1:
        for i in range(2,a):
            if a%i==0:
                return(f"{a} is not prime")
                break
        else:
            return(f"{a} is prime number")
    else:
        return(f"{a} is not a prime")
def square(a):
    ans=a*a
    return ans

print("select value for a method u want:")
print("1.addition")
print("2.substraction")
print("3.multiplication")
print("4.division")
print("5.fllor division")
print("6.modulus")
print("7.factorial")
print("8.prime or not")
print("9.square")
l=[1,2,3,4,5,6]
L=[7,8,9]
while(True):
    choice=int(input("what type method u want :choose no between 1 t0 9: " ))
    if choice in l:
        a=int(input("enter a first number:"))
        b=int(input("enter second number:"))
    elif choice in L:
        a=(int(input("enter a number :"))) 
    if choice ==1:
        print(f"the addition of {a} and {b} is :{addition(a,b)}")
    elif choice==2:
        print(f"the substraction {a} and {b} is :{substraction(a,b)}")
    elif choice==3:
        print(f"the multiplication of {a} and {b} :{multiplication(a,b)}")
    elif choice==4:
        print(f"the division of {a} and {b} is :{division(a,b)}")
    elif choice==5:
        print(f"the fllor division of{a} and {b} :{floor_division(a,b)}")
    elif choice==6:
        print(f"the modulus of {a} and {b} :{modulus(a,b)}")
    elif choice==7:
        print(f"the factorial of {a} :{factorial(a)}")
    elif choice==8:
        print(f"the number {a} is :{prime_not(a)}")
    elif choice==9:
        print(f"the square of {a} is :{square(a)}")
print()






    
