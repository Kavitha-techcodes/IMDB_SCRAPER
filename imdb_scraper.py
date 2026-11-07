import csv
import os
import time
import gzip
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

folder = os.path.dirname(os.path.abspath(__file__))

basics_file = os.path.join(folder, "title.basics.tsv")
ratings_file = os.path.join(folder, "title.ratings.tsv")

print("Opening Chrome...")

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

try:
    # Open IMDb website in Chrome
    driver.get("https://www.imdb.com/chart/top/")

    print("IMDb website opened in Chrome!")

    time.sleep(5)

    ratings = {}

    print("Loading IMDb ratings...")

    with open(ratings_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")

        for row in reader:
            if row["numVotes"] != "\\N":
                if int(row["numVotes"]) >= 100000:
                    ratings[row["tconst"]] = float(row["averageRating"])

    movies = []

    print("Extracting movie details...")

    with open(basics_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter="\t")

        for row in reader:
            movie_id = row["tconst"]

            if row["titleType"] == "movie" and movie_id in ratings:
                if row["startYear"] != "\\N":
                    movies.append({
                        "Rank": 0,
                        "Movie Name": row["primaryTitle"],
                        "Year": row["startYear"],
                        "Rating": ratings[movie_id]
                    })

    movies.sort(key=lambda x: x["Rating"], reverse=True)
    movies = movies[:250]

    for index, movie in enumerate(movies, start=1):
        movie["Rank"] = index

    output = os.path.join(folder, "imdb_movies.csv")

    with open(output, "w", newline="", encoding="utf-8-sig") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Rank", "Movie Name", "Year", "Rating"]
        )
        writer.writeheader()
        writer.writerows(movies)

    print("Total Movies:", len(movies))
    print("CSV file saved successfully!")

    input("Press ENTER to close Chrome...")

finally:
    driver.quit()