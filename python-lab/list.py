#list
num=[1,2,3,4,5,6,7]
print("original list",num)
#list slicng
print("num[1:5]:",num[1:5])
print("num[:5]:",num[:5])
print("num[1:]:",num[1:])
print("num[:-1]:",num[:-1])

#adding elements
num.append(10)
num.insert(2,7)
num.extend([3,8])
print("After adding :",num)
#Removing elements
num.remove(2)
popped=num.pop()
print("After removed :",num)
print("popped element:",popped)
#conting
print("Index of 7:",num.index(7))
print("count of 2:",num.count(2))
#sorting
num.sort()
print("Sorted list:",num)
num.reverse()
print("Reversed :",num)
#copying
copy_num=num.copy()
print("copy of the list:",copy_num)
#Bulid in function
print("Length:",len(num))
print("max value:",max(num))
print("min value:",min(num))
print("sum :",sum(num))





