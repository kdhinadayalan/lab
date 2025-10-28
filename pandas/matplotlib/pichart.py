import matplotlib.pyplot as plt

# Data
products = ['A', 'B', 'C', 'D']
sales = [40, 30, 20, 10]

# Define custom colors
colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99']  # Hex color codes

# Plot
plt.pie(
    sales,
    labels=products,
    autopct='%1.1f%%',   
    startangle=90,       
    colors=colors,       
    shadow=True,         
    explode=(0.05, 0, 0, 0)  # Slightly separate first slice
)

plt.title('Monthly Sales Distribution', fontsize=14)
plt.show()
