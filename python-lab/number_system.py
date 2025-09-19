# Number System Demonstration in Python

# Decimal 
decimal_num = 100
print("Decimal:", decimal_num)

# Binary
binary_num = 0b1100100
print("Binary (0b1100100):", binary_num)

# Octal 
octal_num = 0o144
print("Octal (0o144):", octal_num)

# Hexadecimal 
hex_num = 0x64
print("Hexadecimal (0x64):", hex_num)

print("\n--- Conversions ---")

# Convert decimal to other systems
print("Decimal to Binary:", bin(decimal_num))
print("Decimal to Octal:", oct(decimal_num))
print("Decimal to Hexadecimal:", hex(decimal_num))

# Convert other systems to decimal using int()
print("Binary to Decimal:", int("1100100", 2))
print("Octal to Decimal:", int("144", 8))
print("Hexadecimal to Decimal:", int("64", 16))

print("\n--- Data Types ---")

# int
i = 42
print("Integer:", i, "| Type:", type(i))

# float
f = 3.14
print("Float:", f, "| Type:", type(f))

# complex
c = 2 + 3j
print("Complex:", c, "| Type:", type(c))
