#Conditional Statement
#if
#Odd number
print("\t\tOdd number")
n=int(input("\nEnter a number:"))
if n%2 != 0:
    print("Odd number")

#Even number
print("\n\n\t\tEven number")   
n=int(input("\nEnter a number:"))
if n%2 == 0:
    print("Even number")
    
#Eligiable for voting
print("\n\n\t\tEligiable for voting")
age=int(input("\n\nEnter your age:"))
if age>=18:
    print("Elidiable for voting")


#if...else
#smallest number
print("\n\n\t\tsmallest number")
a=int(input("\nEnter a value:"))
b=int(input("Enter b value:"))
if(a<b):
    print(a,"is smallest number")
else:
    print(b,"is smallest number")


#Biggest number
print("\n\n\t\tBiggest number")
a=int(input("\nEnter a value:"))
b=int(input("Enter b value:"))
if(a>b):
    print(a,"is Biggest number")
else:
    print(b,"is Biggest number")

#find leap year
print("\n\n\t\tfind leap year")
n=int(input("\nEnter a year:"))
if n%4 == 0:
    print("leap year")
else:

    print("Not a leap year")

#elif
#Check Arithmetic operator or not
print("\n\n\t\tCheck Arithmetic operator or not")
opr=input("\nEnter the operator:")
if(opr=='+'):
    print("Addition")
elif(opr=='-'):
    print("Subtraction")
elif(opr=='*'):
    print("Multiplication")
elif(opr == '/'):
    print("Division")
else:
    print("enter the correct operator")


#check you speed
print("\n\n\t\tcheck you speed")
speed=int(input("\nEnter your speed:"))
if(speed>=120):
    print("Over speed")
elif(speed>=60):
    print("Normal speed")
else:
    print("slow speed")

#Check the weekend
print("\n\n\t\tCheck the weekend")
day=input("\nEnter a day:")
if(day=="saturday"):
    print("Weekend")
elif(day=="sunday"):
    print("Weekend")
else:
    print("Weekday")

#Nested if
#check pass or fail
print("\n\n\t\tcheck pass or fail")
mark=int(input("\nEnter your mark:"))
if(mark>=40):
    if(mark>=75):
        print("Pass with Distinction")
    else:
        print("Pass")
else:
    print("Fail")

#Check Temperature
print("\n\n\t\tCheck Temperature")
temp=float(input("Enter the Temperature:"))
if(temp>=0):
    if(temp>30):
        print("It's hot")
    else:
        print("It's warm")
else:
    print("It's cold")

    
#Check the Admission
print("\n\n\t\tCheck the Admission")
mark=float(input("\nEnter your mark:"))
if(mark>=50):
    if(mark>=80):
        print("Direct Admission")
    else:
        print("Admission with interview")
else:
    print("Not Eligible")

