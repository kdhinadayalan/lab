import pandas as pd
import numpy as np

# -------------------------------------------------------
# 1️⃣ Create a simple Series
# -------------------------------------------------------
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print("1. Simple Series:\n", s)

# -------------------------------------------------------
# 2️⃣ Series with custom index
# -------------------------------------------------------
s2 = pd.Series([100, 200, 300], index=["A", "B", "C"])
print("\n2. Series with custom index:\n", s2)

# -------------------------------------------------------
# 3️⃣ Series from dictionary
# -------------------------------------------------------
dict_data = {"a": 10, "b": 20, "c": 30}
s3 = pd.Series(dict_data)
print("\n3. Series from dictionary:\n", s3)

# 4️⃣ Accessing elements
s4 = pd.Series([10, 20, 30, 40, 50], index=["a", "b", "c", "d", "e"])
print("\n4. Accessing elements:")
print("First element (by position):", s4.iloc[0])   # safer version
print("Last two elements:\n", s4.iloc[-2:])
print("Access by label 'c':", s4.loc["c"])

# -------------------------------------------------------
# 5️⃣ Mathematical operations
# -------------------------------------------------------
print("\n5. Mathematical operations:")
print("Add 5:\n", s4 + 5)
print("Multiply by 2:\n", s4 * 2)
print("Square root:\n", s4 ** 0.5)

# -------------------------------------------------------
# 6️⃣ Statistical functions
# -------------------------------------------------------
print("\n6. Statistical functions:")
print("Sum:", s4.sum())
print("Mean:", s4.mean())
print("Max:", s4.max())
print("Min:", s4.min())
print("Standard Deviation:", s4.std())

# -------------------------------------------------------
# 7️⃣ Conditional selection
# -------------------------------------------------------
print("\n7. Conditional selection (values > 25):\n", s4[s4 > 25])

# -------------------------------------------------------
# 8️⃣ Change index and name
# -------------------------------------------------------
s4.index = ["one", "two", "three", "four", "five"]
s4.name = "MySeries"
print("\n8. After changing index and adding name:\n", s4)

# -------------------------------------------------------
# 9️⃣ Missing values (NaN) handling
# -------------------------------------------------------
s5 = pd.Series([10, np.nan, 30, 40])
print("\n9. Series with missing data:\n", s5)
print("\nCheck missing values:\n", s5.isnull())
print("\nFill missing with 0:\n", s5.fillna(0))

# -------------------------------------------------------
# 🔟 Conversion to list and dictionary
# -------------------------------------------------------
print("\n10. Conversion examples:")
print("As list:", s5.tolist())
print("As dictionary:", s5.to_dict())
