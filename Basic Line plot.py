import matplotlib.pyplot as plt
x = ["Mon", "Tue", "Wed", "Thur", "Fri"]
y = [25, 65, 85, 29, 65]
plt.plot(x,y)
plt.title("Sales this Week")
plt.xlabel("Days of the Week")
plt.ylabel("Items Sold per Day")
plt.show()