from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Make the CSV path work no matter where the repo is located.
DATA_PATH = Path(__file__).resolve().parents[1] / "FILES" / "data.csv"
df = pd.read_csv(DATA_PATH)

type_counts =df["Type1"].value_counts(ascending= True)

plt.barh(type_counts.index, type_counts.values)
plt.title("Distribution of Pokemon Types", fontsize=16, fontweight="bold")
plt.xlabel("Count", fontsize=12)
plt.ylabel("Pokemon Type", fontsize=12)
plt.tight_layout()
plt.show()