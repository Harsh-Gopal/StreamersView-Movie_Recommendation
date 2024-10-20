import pandas as pd

# Load the CSV file
movies = pd.read_csv('/Users/harshgopal/Code_Files/StreamersView-Movie_Recommendation/data/TMDB_5000_MOVIES.csv')
print(movies.columns)