import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
company_A = [50, 65, 70, 80, 85, 90]
company_B = [40, 60, 75, 70, 95, 100]

# Create Line Chart
plt.plot(months, company_A, color='blue', marker='o', linestyle='-', linewidth=2, markersize=8, label='Company A')
plt.plot(months, company_B, color='green', marker='s', linestyle='--', linewidth=2, markersize=8, label='Company B')

# Add chart details
plt.title('Sales Comparison Between Company A and Company B', fontsize=14)
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()  # Show company labels
plt.grid(True, linestyle='--', alpha=0.7)  # Light grid lines

# Show chart
plt.show()
