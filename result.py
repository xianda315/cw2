import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import parallel_coordinates

# Read data
file_path = "Results_21Mar2022.csv"
df = pd.read_csv(file_path)

# Select the column of environmental impact indicators
cols_of_interest = [
    "diet_group", "mean_ghgs", "mean_land", "mean_watscar",
    "mean_eut", "mean_ghgs_ch4", "mean_ghgs_n2o", "mean_bio", "mean_acid"
]

# Group the data by diet_group and calculate the mean value
df_grouped = df[cols_of_interest].groupby("diet_group").mean().reset_index()

# Make sure that the "diet_group" column is of string type
df_grouped["diet_group"] = df_grouped["diet_group"].astype(str)

# Draw the parallel coordinate graph
plt.figure(figsize=(12, 6))
parallel_coordinates(df_grouped, class_column="diet_group", colormap="Set2")
plt.title("Environmental Impacts by Diet Type (Parallel Coordinates Plot)")
plt.xlabel("Environmental Indicators")
plt.ylabel("Mean Values (Standardized Units)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()