 IMDb Movie Rating Scraper Using Python

📌 Project Overview

The IMDb Movie Rating Scraper is a Python-based web scraping project that automatically collects movie information from the IMDb Top 250 website.

It uses Selenium WebDriver to automate Google Chrome and Pandas to organize, process, and store movie details in CSV format.

The project collects movie rankings, titles, release years, IMDb ratings, vote counts, and other available information.

🎯 Objectives

- Automate movie data collection from IMDb.
- Extract movie names and rankings.
- Collect movie release years and ratings.
- Organize movie information using Pandas.
- Store extracted data in CSV files.
- Reduce manual data collection.

🛠️ Technologies Used

Technology| Purpose
Python| Programming language
Selenium| Web scraping and browser automation
Google Chrome| Web browser
Pandas| Data processing and analysis
CSV| Data storage
IMDb Datasets| Movie information
VS Code| Code editor

📂 Project Structure

IMDb_Movie_Scraper/
│
├── imdb_scraper.py
├── imdb_dataset_scraper.py
├── view_imdb_results.py
│
├── imdb_movies.csv
├── imdb_top_movies.csv
│
├── title.basics.tsv
├── title.ratings.tsv
│
└── README.md

⚙️ Installation

Step 1: Install Python

Download Python from:
https://www.python.org/downloads/

Step 2: Install Required Libraries

Open the VS Code terminal and run:

pip install selenium pandas

Step 3: Download IMDb Datasets

Download the required dataset files:

https://datasets.imdbws.com/

Place "title.basics.tsv" and "title.ratings.tsv" inside the project folder.

▶️ How to Run the Project

Open the project folder in Visual Studio Code.

Run the following command:

python imdb_scraper.py

To process the IMDb dataset:

python imdb_dataset_scraper.py

📊 Output

The project generates CSV files containing movie information.

Output files:

- "imdb_movies.csv"
- "imdb_top_movies.csv"

The captured execution successfully processed 250 movies and saved the CSV output.

📸 Project Screenshots

The repository includes screenshots showing:

1. Python Selenium implementation.
2. Pandas movie sorting and processing.
3. Extracted movie information in CSV format.
4. Successful program execution in the terminal.

🚀 Future Enhancements

- Extract movie genres and directors.
- Collect actor and cast information.
- Add graphical data visualization.
- Develop a movie recommendation system.
- Store movie details in a database.
- Build a user-friendly web dashboard.

🎓 Applications

- Movie rating analysis.
- Movie comparison.
- Data visualization.
- Academic learning.
- Data science projects.

👩‍💻 Developer

Name: Kavitha P
Department: B.E. Cyber Security
Project: IMDb Movie Rating Scraper Using Python

📚 References

- IMDb: https://www.imdb.com/chart/top/
- Python: https://docs.python.org/3/
- Selenium: https://www.selenium.dev/documentation/
- Pandas: https://pandas.pydata.org/docs/
- IMDb Datasets: https://datasets.imdbws.com/

---

⭐ If you find this project useful, consider giving the repository a star!
