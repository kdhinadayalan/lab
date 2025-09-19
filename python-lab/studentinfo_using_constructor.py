class student:
    def __init__(self,name,rollo,marks):
        self.rollno=rollno
        self.name=name
        self.marks=marks
        self.result=""
        self.grade=""
    def check_the_info(self):
        if all(mark>=50 for mark in self.marks):
            self.result="Pass"
        else:
            self.result="Fail"
        self.total=sum(marks)
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
name=input(f"Enter your name:")
rollno=input(f"Enter your Roll no:")
marks=[]
for i in range(1,6):
    m=int(input(f"Enter your {i} mark:"))
    marks.append(m)
s=student(name,rollno,marks)
s.check_the_info()
s.display()
