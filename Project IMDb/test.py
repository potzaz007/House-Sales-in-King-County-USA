import pandas as pd
df = pd.read_csv('IMDb movies .csv')

movies_df = pd.read_csv('IMDb movies .csv', dtype={'year':int, 'budget':str})
new_movies_df = movies_df[movies_df['year'] >= 2015]
filtered_movies_df = new_movies_df[new_movies_df['budget'].notna() & new_movies_df['worlwide_gross_income'].notna()][['imdb_title_id', 'budget', 'worlwide_gross_income']]
filtered_movies_df = filtered_movies_df['budget'].apply(lambda m: m.split()[0]).unique()
a = filtered_movies_df[filtered_movies_df['budget'].str.slice(stop=1) == '$']
b = filtered_movies_df['profit'] = filtered_movies_df['worlwide_gross_income'].apply(lambda m : int(m.split()[1])) - filtered_movies_df['budget'].apply(lambda m : int(m.split()[1]))
c = selected_ids = filtered_movies_df[filtered_movies_df['profit'] > 0]

print(a.head(25))