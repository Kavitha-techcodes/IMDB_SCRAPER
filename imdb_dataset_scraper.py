import pandas as pd
import os

print("IMDb Movie Rating Dataset Scraper")
print("Project Started Successfully!")

# Get project folder path
folder = os.path.dirname(os.path.abspath(__file__))

basics_file = os.path.join(folder, "title.basics.tsv")
ratings_file = os.path.join(folder, "title.ratings.tsv")

# Check files
if not os.path.exists(basics_file):
    print("Error: title.basics.tsv file not found!")
    exit()

if not os.path.exists(ratings_file):
    print("Error: title.ratings.tsv file not found!")
    exit()

# Read IMDb basics dataset
print("\nLoading Movie Details...")

basics = pd.read_csv(
    basics_file,
    sep="\t",
    na_values="\\N",
    usecols=[
        "tconst",
        "titleType",
        "primaryTitle",
        "startYear",
        "runtimeMinutes",
        "genres"
    ],
    low_memory=False
)

# Read IMDb ratings dataset
print("Loading Movie Ratings...")

ratings = pd.read_csv(
    ratings_file,
    sep="\t",
    na_values="\\N"
)

# Select movies only
movies = basics[basics["titleType"] == "movie"].copy()

# Merge movie details and ratings
movie_data = pd.merge(
    movies,
    ratings,
    on="tconst",
    how="inner"
)

# Sort by rating
movie_data = movie_data.sort_values(
    by=["averageRating", "numVotes"],
    ascending=False
)

# Display total movies
print("\nTotal Movies Found:", len(movie_data))

# Display Top 10 movies
print("\nIMDb Top 10 Movies:")

top_movies = movie_data.head(10)

for index, movie in enumerate(
    top_movies.itertuples(),
    start=1
):
    print("\nRank:", index)
    print("Movie:", movie.primaryTitle)
    print("Year:", movie.startYear)
    print("Rating:", movie.averageRating)
    print("Votes:", movie.numVotes)
    print("Genre:", movie.genres)

# Save results
output_file = os.path.join(folder, "imdb_top_movies.csv")

top_movies.to_csv(output_file, index=False)

print("\nTop Movies Saved Successfully!")
print("Output File:", output_file)

print("\nProject Completed Successfully!")