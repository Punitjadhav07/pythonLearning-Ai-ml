import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df=pd.read_csv(
    '/Users/punitjadhav/Documents/Ai ML /Python Basics/pythonLearning-Ai-ml/FILES/data.csv',
    
)

type_counts =df["Type1"].value_counts(ascending= True)

plt.barh(type_counts.index, type_counts.values)
plt.title("Distribution of Pokemon Types", fontsize=16, fontweight="bold")
plt.xlabel("Count", fontsize=12)
plt.ylabel("Pokemon Type", fontsize=12)
plt.tight_layout()
plt.show()