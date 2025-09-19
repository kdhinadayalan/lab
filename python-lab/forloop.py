#for loop
print("print even numbers 1 to 10")
for i in range(0,10,2):
    
    print(i)
#continue statement
print("continue statenments")
for i in range(1,6):
    
    if(i==3):
        continue
    print(i)
#Break statements
print("break statements")
for i in range(1,10):
    i+=1
    if(i==4):
        break
    print(i)
#iterating strings in for loop
names={"apple","orange","mango"}
for name in names:
    print(name)


#while loop
print("print numbers in 1 to 5")
i=0
while i<=5:
    print(i)
    i+=1

password=""
while password!="Dhina2005":
    password=input("Enter the password:")

print("Welcome")


