
import matplotlib.pyplot as plt

# ----------------------------------------
# Example 1: Simple interactive chart
# ----------------------------------------
plt.plot([1, 2, 3, 4])
plt.show()

# ----------------------------------------
# Example 2: Simple plot with y values
# ----------------------------------------
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

# ----------------------------------------
# Example 3: Plot with red circles
# ----------------------------------------
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 4: Set axis range and title
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 5: Add labels to the axes
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot')
plt.xlabel('Counting')
plt.ylabel('Square values')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 6: Customize font, size, and color
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 7: Add text annotations
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 8: Add text with a math expression and a bounding box
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y = x^2$', fontsize=20,
         bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 9: Add grid lines
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, r'$y = x^2$', fontsize=20,
         bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.grid(True)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.show()

# ----------------------------------------
# Example 10: Add legend to the chart
# ----------------------------------------
plt.axis([0, 5, 0, 20])
plt.title('My first plot', fontsize=20, fontname='Times New Roman')
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
plt.text(1.1, 12, '$y = x^2$', fontsize=20,
         bbox={'facecolor': 'yellow', 'alpha': 0.2})
plt.grid(True)

# Multiple data series
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
plt.plot([1, 2, 3, 4], [0.8, 3.5, 8, 15], 'g^')
plt.plot([1, 2, 3, 4], [0.5, 2.5, 4, 12], 'b*')

# Add legend
plt.legend(['First series', 'Second series', 'Third series'], loc=2)
plt.show()