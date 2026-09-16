import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [10,20,30,40,60]

fig, ax = plt.subplots(1,2, figsize = (10,6))
ax[0].plot(x,y, color = "blue")
ax[0].set_title("Line Plot")

ax[1].bar(x,y, color = "Green")
ax[1].set_title("Bar Chart")
fig.suptitle("Comparison of Line & Bar Charts")
plt.tight_layout()
plt.show()