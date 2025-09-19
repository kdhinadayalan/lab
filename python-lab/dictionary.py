#dictionary
student={"Name":"Dhina",
         "Age":21,
         "Mark":89}
#print the dictionary
print(" Original Dictionary",student)
#clear the dictionary
copy_dict=student.copy()
copy_dict.clear()
print("\n Clear()               :",copy_dict)
#copy the dictionary
new_dict=student.copy()
print(" Copy the dictionary     :",new_dict)
print("\n get('age')            :",student.get("Age"))
print("\n get('grade',notfound'):",student.get("grade","notFound"))
print("\n items                 :",student.items())
print("\n key                   :",student.keys())
print("\n values                :",student.values())
removed_value=student.pop('Mark')
print("\n pop('mark')           :",removed_value)
last_item=student.popitem()
print("\n popitem               :",last_item)
print("\n setdefault            :",student.setdefault("gender","male"))
print("\n After setdefault      :",student)
student.update({"age":21,"cource":"MCA"})
print("\n After updation        :",student)
new_dict2=dict.fromkeys(['a','b','c'],0)
print("\n Fromkeys              :",new_dict2)
print("\n Length of the dictionary:",len(student))
print("\n str for the dictionary  :",str(student))
print("\n print the type          :",type(student))
print("\n sorted dictionary       :",sorted(student))
print("\n Return the dict is empty:",any(student))
print("\n Checks truthiness in dictionary:",all(student))
