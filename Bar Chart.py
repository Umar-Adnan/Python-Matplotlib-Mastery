import matplotlib.pyplot as plt
product = ["Phones", "Guns", "Moterbikes", "Dumbells"]
sales = [50000, 26000, 98000, 64000]
plt.barh(
    product,
    sales,
    color = "Blue",
    label = "Sales 2026"
    )
plt.xlabel("Products")
plt.ylabel("Sales of each Product")
plt.title("Sales 2026")
plt.legend( fontsize = 7)
plt.show()