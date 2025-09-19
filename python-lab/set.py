#set
#set creation
a={1,2,3,4,5,6,7}
b={2,7,8,2,4,6,5}
print("set A:",a)
print("set B:",b)
#Adding and removing
a.add(7)
a.update([8,9])
print("After adding:",a)
a.remove(2)
a.discard(5)
print("After removed:",a)
#operation
print("Union :",a.union(b))
print("Intersection:",a.intersection(b))
print("Difference(a-b):",a.difference(b))

#build in function
print("Length of A:",len(a))
print("max value in B:",max(b))
print("min value in A:",min(a))
print("sum of A:",sum(a))
