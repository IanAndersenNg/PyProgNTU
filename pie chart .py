import matplotlib.pyplot as plt

# Data for the pie chart
labels = ['Entertainment', 'Food and drinks', 'Transporation', 'Travel']
sizes = [15, 30, 45, 10]  # The corresponding values for each category
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']  # Optional: colors for each wedge
explode = (0.1, 0, 0, 0)  # Optional: "explode" the 1st slice (i.e., 'Category A')

# Create the pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Display the pie chart
plt.show()
