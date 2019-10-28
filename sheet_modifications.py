import pandas as pd

df = pd.read_csv('/Users/cmason/Desktop/PycharmProjects/did_exercise_final.csv')

df.fillna(0, inplace=True)
for cells in df:
    df.replace('x', 0, inplace=True)


print(df['Day 1 DC2 Final'])

df['Day 1 V I/F'] = list(zip(df['Day 1 Initial'], df['Day 1 Final']))
df['Day 1 DC1 I/F'] = list(zip(df['Day 1 DC1 Initial'], df['Day 1 DC1 Final']))
df['Day 1 DC2 I/F'] = list(zip(df['Day 1 DC2 Initial'], df['Day 1 DC2 Final']))
df['Day 2 V I/F'] = list(zip(df['Day 2 Initial'], df['Day 2 Final']))
df['Day 2 DC1 I/F'] = list(zip(df['Day 2 DC1 Initial'], df['Day 2 DC1 Final']))
df['Day 2 DC2 I/F'] = list(zip(df['Day 2 DC2 Initial'], df['Day 2 DC2 Final']))
df['Day 3 V I/F'] = list(zip(df['Day 3 Initial'], df['Day 3 Final']))
df['Day 3 DC1 I/F'] = list(zip(df['Day 3 DC1 Initial'], df['Day 3 DC1 Final']))
df['Day 3 DC2 I/F'] = list(zip(df['Day 3 DC2 Initial'], df['Day 3 DC2 Final']))
df['Day 4 V I/F'] = list(zip(df['Day 4 Initial'], df['Day 4 Final']))
df['Day 4 DC1 I/F'] = list(zip(df['Day 4 DC1 Initial'], df['Day 4 DC1 Final']))
df['Day 4 DC2 I/F'] = list(zip(df['Day 4 DC2 Initial'], df['Day 4 DC2 Final']))

df1 = df[['Mouse Number', 'Weight', 'Day 1 V I/F', 'Day 1 DC1 I/F', 'Day 1 DC2 I/F', 'Day 2 V I/F',
          'Day 2 DC1 I/F', 'Day 2 DC2 I/F', 'Day 3 V I/F', 'Day 3 DC1 I/F', 'Day 3 DC2 I/F',
          'Day 4 V I/F', 'Day 4 DC1 I/F', 'Day 4 DC2 I/F']]

df1.to_csv('/Users/cmason/Desktop/PycharmProjects/tupled_list_v5.csv')
