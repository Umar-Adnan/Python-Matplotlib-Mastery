import matplotlib.pyplot as plt

regions = ["Pakistan", "India", "China", "Afghanistan"]
# Total historical terrorist attack incidents per country (GTD recorded data)
terror_attack_counts = [15400, 13000, 3500, 16000]
plt.pie(
    terror_attack_counts,
    labels=regions,
    autopct="%1.1f%%",
    colors=["green", "blue", "red", "yellow"]
    )
plt.title("Terror attacks Recorded in Asia")
plt.show()