import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df =pd.read_csv("Virat_Kohli.csv")

print(df.head())

# # total no of runs kohli has scored
# print("Total runs: ", df["Runs"].sum())

# # find out the total no balls he has faced

# print("Total balls faced: ", df["BF"].sum())
# # find out the average strike rate of kohli

# print("Average Strike Rate: ", df["SR"].mean())


print(df["Pos"].head(10))

positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: 'batting at 3',
    4.0: 'batting at 4',
    2.0: 'batting at 2',
    1.0: 'batting at 1',
    7.0: 'batting at 7',
    5.0: 'batting at 5',
    6.0: 'batting at 6'
})

print(df.head(10))
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))
# print(df[["Runs", "Pos"]])


# total runs scored in different positions
pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10, 7))
plt.pie(pos_counts_values, labels=pos_counts_labels)
plt.show()

def show_pie_plots(df, key):
    counts = df[key].value_counts()
    print(counts)
    count_values = counts.values
    count_labels = counts.index
    fig = plt.figure(figsize=(10, 7))
    plt.pie(count_values, labels = count_labels)
    plt.show()

# number of matches he has played at different  positions
show_pie_plots(df, "Opposition")

# number of matches he played at grounds
show_pie_plots(df, "Ground")

# total sixes scored in different positions
runs_at_pos = df.groupby("Pos")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))

runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

fig = plt.figure(figsize=(10, 7))
plt.bar(runs_at_pos_labels, runs_at_pos_values, color="black", width=0.5)
plt.show()

# total runs scored with different countries
runs_with_countries = df.groupby("Opposition")['Runs'].sum()
runs_with_countries_values = runs_with_countries.values
runs_with_countries_labels = runs_with_countries.index

plt.bar(runs_with_countries_labels, runs_with_countries_values, color="blue", width=0.5)
plt.show()

# number of centuries scored by him in 1st and 2nd innings
centuries = df.query("Runs >= 100")
print(centuries)

innings = centuries["Inns"].value_counts()
print(innings)
# tons = centuries["Runs"]

plt.bar(innings.values, labels =innings.index)
plt.show()

# calculate the dismissals of kohli


