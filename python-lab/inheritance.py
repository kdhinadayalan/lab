#single inheritance
class A:
    def __init__(self):
        self.a=int(input("Enter a value:"))
        self.b=int(input("Enter b value:"))
class B(A):
    def operation(self):
        print("Addition:",self.a+self.b)
        print("Sutraction:",self.a-self.b)
        print("multiplication:",self.a*self.b)
        print("Division:",self.a/self.b)

obj=B()
obj.operation()
       

#multi level inheritance
class A:
    def input(self):
        self.name=input(f"Enter your name:")
        self.rollno=input(f"Enter your Roll no:")
        self.marks=[]
        for i in range(1,6):
            m=int(input(f"Enter your {i} mark:"))
            self.marks.append(m)

class B(A):
    def check_the_info(self):
        if all(mark>=50 for mark in self.marks):
            self.result="Pass"
        else:
            self.result="Fail"
class C(B):
    def check_total_grade(self):
        
            self.total=sum(self.marks)
            self.average=self.total/5
            
            if self.average>=90:
                self.grade="A"
            elif self.average>=70:
                self.grade="B"
            elif self.average>=50:
                self.grade="C"
            else:
                self.grade="D"
class D(C):
    def display(self):
        print("\n\n\t Student Information")
        print(f"Name      :{self.name}")
        print(f"Rollno    :{self.rollno}")
        print(f"Marks     :{self.marks}")
        print(f"Total     :{self.total}")
        print(f"Average   :{self.average}")
        print(f"Result    :{self.result}")
        print(f"Grade     :{self.grade}")

s=D()
s.input()
s.check_the_info()
s.check_total_grade()
s.display()

#multiple inheritance

class A:
    def input(self):
        self.name=input(f"Enter your name:")
        self.rollno=input(f"Enter your Roll no:")
        self.marks=[]
        for i in range(1,6):
            m=int(input(f"Enter your {i} mark:"))
            self.marks.append(m)

class B:
    def check_the_info(self):
        if all(mark>=50 for mark in self.marks):
            self.result="Pass"
        else:
            self.result="Fail"
class C:
    def check_total_grade(self):
        
            self.total=sum(self.marks)
            self.average=self.total/5
            
            if self.average>=90:
                self.grade="A"
            elif self.average>=70:
                self.grade="B"
            elif self.average>=50:
                self.grade="C"
            else:
                self.grade="D"



class D(C,B,A):
    def display(self):
        print("\n\n\t Student Information")
        print(f"Name      :{self.name}")
        print(f"Rollno    :{self.rollno}")
        print(f"Marks     :{self.marks}")
        print(f"Total     :{self.total}")
        print(f"Average   :{self.average}")
        print(f"Result    :{self.result}")
        print(f"Grade     :{self.grade}")

s=D()
s.input()
s.check_the_info()
s.check_total_grade()
s.display()

#hierarchical inheritance
class A:
    def input(self):
        self.name=input(f"Enter your name:")
        self.rollno=input(f"Enter your Roll no:")
        self.marks=[]
        for i in range(1,6):
            m=int(input(f"Enter your {i} mark:"))
            self.marks.append(m)

class B(A):
    def Result_info(self):
        
        if all(mark>=50 for mark in self.marks):
            self.result="Pass"
        else:
            self.result="Fail"

class C(A):
    def check_total_grade(self):
        self.total=sum(self.marks)
        self.average=self.total/5
        if self.average>=90:
            self.grade="A"
        elif self.average>=70:
            self.grade="B"
        elif self.average>=50:
            self.grade="C"
        else:
            self.grade="D"


    def display(self):
        print("\n\n\t Student Information")
        print(f"Name      :{self.name}")
        print(f"Rollno    :{self.rollno}")
        print(f"Marks     :{self.marks}")
        print(f"Total     :{self.total}")
        print(f"Average   :{self.average}")
        print(f"Result    :{self.result}")
        print(f"Grade     :{self.grade}")

a = B()
a.input()
a.Result_info()

b = C()
b.name = a.name
b.rollno = a.rollno
b.marks = a.marks
b.result = a.result  
b.check_total_grade()
b.display()

