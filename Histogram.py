import matplotlib.pyplot as plt

marks = [78, 42, 89, 55, 91, 63, 34, 72, 85, 49, 96, 68, 51, 77, 83, 60, 41, 90, 67, 74]
plt.hist(
    marks,
    bins=6,
    color="Blue",
    edgecolor="Black"
)
plt.xlabel("Marks")
plt.ylabel("No. of Students")
plt.title("Score Distribution of Students")
plt.show()