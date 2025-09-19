#tuple
#creating a tuple
num=(1,2,3,4,5,6,7)
num2=(1,2,5,7,8,11,12)
print("Concatination of tuple:",num+num2)
print("Repetation of tuple:",num*2)
print("Tuple:",num)
print("count of 5:",num.count(5))
print("Index of 8:",num.index(7))
#Build in functions
print("Length:",len(num))
print("max value:",max(num))
print("min value:",min(num))
print("sum :",sum(num))
#slicing
print("num[1:5]:",num[1:5])
print("num[:5]:",num[:5])
print("num[1:]:",num[1:])
print("num[:-1]:",num[:-1])
#convert into tuple
l1=[10,20,30]
new_tuple=tuple(l1)
print("list:",l1)
print("converted tuple:",new_tuple)
