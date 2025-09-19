print("welcome message")
#user define function
def greet(name):
    print("welcome",name)
value=input("Enter your name:")
greet(value)

print("\nfactorinal number")
#factorial
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
number=int(input("Enter a number:"))
print("factorial of ",number,"is",factorial(number))

print("\n Area of rectangle")
#Required function
def cal_area(length,width):
    area=length*width
    print("Area of rectangle:",area)

l=int(input("Enter length:"))
w=int(input("Enter width:"))
cal_area(l,w)

print("\n Return value function")
#check number in even number
def is_even(n):
    if n%2==0:
        return True
    else:
        return False

num=int(input("Enter a number:"))
if is_even(num):
    print(num,"is even number")
else:
    print(num,"is odd")

print("\nDefault function")
#power of the given value
def power(base=2,exponent=2):
    print(base,"raised to ",exponent,"is",base**exponent)

power(5,4)
power(5)

print("\nvariable lengthn function")
#product of numers
def multiply(*args):
    product=1
    for num in args:
        product*=num
    print("product is",product)
multiply(2,3,4,5,6,7)

print("\nLambda function")
#To find arithmetic operation
add=lambda a,b:a+b
sub=lambda a,b:a-b
mul=lambda a,b:a*b
div=lambda a,b:a/b

print("Addition:",add(5,2))
print("Subtraction:",sub(5,2))
print("Multiplication:",mul(5,2))
print("Division:",div(5,2))
