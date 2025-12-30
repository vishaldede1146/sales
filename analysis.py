import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [2000, 2500, 3000, 2800]
}

df = pd.DataFrame(data)

print(df)

plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


import seaborn as sns

sns.barplot(x="Month", y="Sales", data=df)
plt.show()
