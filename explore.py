import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.float_format", lambda x: f"{x:.2f}")

df = pd.read_csv("austin_home_sales.csv")

print(df.shape)
print(df.describe())

plt.scatter(df["Sq_Footage"], df["Sale_Price"])
plt.xlabel("Sq_Footage")
plt.ylabel("Sale_Price")
plt.tight_layout()
plt.savefig("scatter.png")
