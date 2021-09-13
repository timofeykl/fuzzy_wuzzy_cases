import difflib

# make a key column to merge based on close matches
df2['Fuzzy_Key'] = df2.Unit_ID.map(lambda x: difflib.get_close_matches(x, df1.G_ID))

# since the values in our Fuzzy_Key column are lists, we have to convert them to strings
df2['Fuzzy_Key'] = df2.Fuzzy_Key.apply(lambda x: ''.join(map(str, x)))
