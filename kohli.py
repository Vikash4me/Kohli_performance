import pandas as pd

df = pd.read_csv("Virat_Kohli.csv")

print(df.head(10))
# print(df.tail(10))

# df.info()
# print(df.shape)

# print(df["Opposition"].describe())

# run_frequency = df["Opposition"].value_counts()
# print(run_frequency)

new_df = df[["Runs", "SR", "Opposition"]]

# print(new_df)

# vs_aussies = df[df["Opposition"] == "v Australia"]

# print(vs_aussies)

# find all the matches where virat scored a century
# matches1 = df[df["Runs"] >= 100]
# print(matches1)
# # find all the matches where virat's strike rate was > 100
# matches2 = df[df["SR"] > 100]
# print(matches2)
# # find all the matches where virat played with srilanka and scored a century
# matches3 = (df (df["Opposition"] == "v Sri Lanka") & (df ["Runs"] >= 100))
# print(matches3)

def find_centuries(x):
    if x>=100:
        return "OG"
    else:
        return "NOOB"
df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))
