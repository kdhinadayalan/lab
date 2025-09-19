#slicing
print("Slicing")
s = "Dhinadayalan"
print(s[0])
print(s[-1]) 
print(s[0:3])
print(s[::2])

#built in methods
print("\n\nBuilt in method")
print(s.lower())         
print(s.upper())        
print(s.strip())         
print(s.replace("World", "Python"))  
print(s.find("d"))      
print(s.count("a"))     
print(s.startswith("D"))  
print(s.endswith("n"))


#String Concatenation and Repetition
print("\n\nString Concatenation and Repetition")
a = "Hello"
b = "Python"
print(a + " " + b) 
print(a * 3)

#Splitting and Joining Strings
print("\n\nSplitting and Joining Strings")
text = "apple,banana,grape"
fruits = text.split(",")   
print(fruits)

joined = "-".join(fruits) 
print(joined)


# String Formatting
print("\nString Formatting")
s = "dhina2005"
name = "dhina"
age = 21

#  f-strings
print("f-strings")
print(f"My name is {name} and I am {age} years old.")

#  format()
print("format()")
print("My name is {} and I am {} years old.".format(name, age))

#  % formatting
print("% formatting")
print("My name is %s and I am %d years old." % (name, age))

#String Checks
print("\n\nString Checks")
print(s.isalpha())  
print(s.isdigit())  
print(s.isalnum())   
print("DHINA".islower())  
print("dhina".isupper())  
print("dhinadayalan".istitle())  

#Reversing a String
print("\n\nReversing a String")
s = "dhinadayalan"
print(s[::-1]) 
text = "My name is dhinadayalan"
print("Reversed:", text[::-1])


