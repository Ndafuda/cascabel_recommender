import pandas as pd

# movie, ratings by users
R = pd.read_csv('../most_watched_user.csv', index_col=0) ##input data no missing values
films = R.columns.tolist() #movies
users = R.index.tolist() #users
