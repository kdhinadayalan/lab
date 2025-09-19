print("\t\tData encryption")
name="dhinadayalan"
for ch in name:
    print("Encrypted message:",ch,":",ord(ch))

print("\n\n\t\tData decryption")
a=[100,104,105,110,97,100,97,121,121,97,108,97,110]
de=" ".join(chr(num) for num in a)
print(a,"Decryted message:",de)
