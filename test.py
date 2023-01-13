import pandas as pd

data = {
    'apples':[4,3,6,1],
    "oranges":[3,7,4,1]
}

index_titles = [
    "Aaron","shaun","James", "wilson"
]
df = pd.DataFrame(data, index=index_titles)
print(df)
print(type(df))
print(df.loc['Aaron'])
print(df["oranges"].iloc[0:])
