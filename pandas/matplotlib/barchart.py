import matplotlib.pyplot as plt

# Data
products = ['A', 'B', 'C', 'D']
sales = [40, 30, 20, 10]

# Create Bar Chart
plt.bar(products, sales, color=['#FF9999', '#66B2FF', '#99FF99', '#FFCC99'])

# Add Labels and Title
plt.title('Monthly Sales Comparison', fontsize=14)
plt.xlabel('Products')
plt.ylabel('Sales')

# Show chart
plt.show()
