import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee_data.csv")

plt.figure(figsize=(12,8))

# Bar Chart
plt.subplot(2,2,1)
df["City"].value_counts().plot(kind="bar")
plt.title("Bar Chart")

# Pie Chart
plt.subplot(2,2,2)
df["City"].value_counts().plot(kind="pie", autopct="%1.1f%%")
plt.title("Pie Chart")
plt.ylabel("")

# Histogram
plt.subplot(2,2,3)
plt.hist(df["Salary"], bins=5)
plt.title("Histogram")

# Line Chart
plt.subplot(2,2,4)
plt.plot(df["ID"], df["Salary"], marker="o")
plt.title("Line Chart")

plt.tight_layout()
plt.show()