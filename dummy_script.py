import matplotlib.pyplot as plt
from collections import Counter

# Your list of strings
data = ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple", "Apple", "Orange"]

# Count the frequency of each string
string_count = Counter(data)

# Extract the unique strings and their frequencies
labels = list(string_count.keys())
print(labels)
frequencies = list(string_count.values())

# Calculate the percentage for each string
total = sum(frequencies)
percentages = [(count / total) * 100 for count in frequencies]

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("String Frequency Pie Chart")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Display the chart
plt.show()