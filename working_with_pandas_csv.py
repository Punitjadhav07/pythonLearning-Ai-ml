import pandas as pd

# Load CSV file and set Name as index
df = pd.read_csv(
    '/Users/punitjadhav/Documents/Ai ML /Python Basics/pythonLearning-Ai-ml/FILES/data.csv',
    index_col='Name'
)

# -------------------------------
# Displaying data
# -------------------------------

print("Single row using loc:")
print(df.loc["Pikachu"].to_string())
print()

print("Multiple rows using loc:")
print(df.loc[["Pikachu", "Bulbasaur"]].to_string())
print()

print("Single value using loc:")
print(df.loc["Pikachu", "Height"])
print()

print("Multiple rows and columns using loc:")
print(df.loc[["Pikachu", "Bulbasaur"], ["Height", "Weight"]].to_string())
print()

print("Rows and columns using iloc:")
print(df.iloc[0:11:2, 0:3])
print()

# -------------------------------
# User input search
# -------------------------------

pokemon = input("Enter the name of the pokemon: ").strip()

try:
    print("\nPokemon details:")
    print(df.loc[pokemon].to_string())
except KeyError:
    print("Pokemon not found in the dataset.")

print()

# -------------------------------
# Filtering data
# -------------------------------

print("Tall pokemon (Height > 2.0):")
tall_pokemon = df[df["Height"] > 2.0]
print(tall_pokemon)
print()

print("Water type pokemon:")
water_pokemon = df[(df["Type1"] == "Water") | (df["Type2"] == "Water")]
print(water_pokemon)
print()

# -------------------------------
# Aggregate functions
# -------------------------------

print("Mean of numeric columns:")
print(df.mean(numeric_only=True))
print()

print("Sum of numeric columns:")
print(df.sum(numeric_only=True))
print()

print("Minimum values of numeric columns:")
print(df.min(numeric_only=True))
print()

print("Maximum values of numeric columns:")
print(df.max(numeric_only=True))
print()

print("Count of numeric columns:")
print(df.count(numeric_only=True))
print()

print("Average Height:")
print(df["Height"].mean())
print()

# -------------------------------
# GroupBy
# -------------------------------

print("Average Height by Type1:")
group = df.groupby("Type1")
print(group["Height"].mean())
print(group["Height"].count())

