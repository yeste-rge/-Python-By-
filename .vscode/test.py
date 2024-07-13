# x=round(123,-2)
# y=str(x)
# z=y[-2]
# print(z)
import matplotlib.pyplot as plt

# Given data
x_values = [40, 50, 60, 70]
y_values = [0.5, 0.66, 0.83, 1.02]

# Create the plot
plt.plot(x_values, y_values, marker='o')

# Add titles and labels
plt.title('Sample Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
