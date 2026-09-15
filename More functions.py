import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [6544, 1258, 3620, 2598, 2598, 4568, 9512, 5648, 2598, 2547, 6598, 1145]

# Set figure size
plt.figure(figsize=(9, 5))

# Plot data
plt.plot(
    months, sales,
    color="Red",
    linestyle='-.',
    linewidth=2,
    marker="o",
    label="Sales Data Stats"
)

# Labels and Title
plt.title("Yearly Sales Stats")
plt.xlabel("Months")
plt.ylabel("Sales per Month")

# 1. Show ticks for ALL 12 months with custom text labels
plt.xticks(ticks=months, labels=month_names)

# 2. Set Y-axis limits correctly
plt.ylim(0, 10000)

plt.legend(loc='upper left', fontsize=8)
plt.grid(color="Black", linestyle='-.', linewidth=0.25)

plt.tight_layout()
plt.show()