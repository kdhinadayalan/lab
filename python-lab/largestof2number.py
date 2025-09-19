
print("Largest of three numbers")

class largest:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def find_largest(self):
        if self.a>=self.b and self.a>=self.c:
            return self.a
        elif self.b>=self.c and self.b>=self.c:
            return self.b
        else:
            return self.c
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
l=largest(a,b,c)
print("Largest is ",l.find_largest())

print("\nfibonacci series")
#fibonacci series
class fibonacci:
    def __init__(self,term):
        self.term=term
    def generate(self):
        a,b=0,1
        series=[]
        for _ in range(self.term):
            series.append(a)
            a,b=b,a+b
        return series
n=int(input("Enter number of term:"))
fib=fibonacci(n)
print("Fibonacci series:",fib.generate())

print("\ncheck palindrome number")
#check palindrome number
class pali:
    def __init__(self,number):
        self.number=number
    def palindrome(self):
        if (str(self.number)==str(self.number)[::-1]):
            return True
        else:
            return False
num=(input("Enter a number:"))
p=pali(num)
print("palindronme",  p.palindrome())

print("\nArea of circle")
#area of circle
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

cho=0
while(cho<3):
    
    cho=int(input("Enter your choice:\n1.radius\n2.circumference\n3.exit\n"))
    n=int(input("Enter the radius:"))

    c=circle(n)

    if(cho==1):
       print("Area of circle:", c.area())
    elif(cho==2):
        print("Circumference:",c.circumference())
    else:
        print("Thankyou")
        exit(1)
    
print("\nArea of rectangle")
#Area of rectangle
class rect:
    def __init__(self,l,w):
        self.l=l
        self.w=w
    def area(self):
        return self.l*self.w
    def parimeter(self):
        return 2*self.l+self.w

cho=0
while(cho<3):
    l=int(input("Enter the length:"))
    w=int(input("Enter the width:"))
    c=rect(l,w)

    cho=int(input("Enter your choice:\n1.area\n2.parimeter\n3.exit\n"))
    
    if(cho==1):
       print("Area of Rectangle:", c.area())
    elif(cho==2):
        print("parimeter:",c.parimeter())
    else:
        print("Thankyou")
        break
print("\nArea of square")
#Area of square
class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side
s=square(6)
print("Area of square:",s.area())
print("perimeter of square:",s.perimeter())

print("\nArea of Triangle")
#Area of Triangle
class Triangle:
    
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        return 0.5*self.b*self.h
t=Triangle(3,9)
print("Area of Triangle:",t.area())
     
