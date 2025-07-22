"""
Task 01: Build a Web Scraper
Develop a web scraper that extracts
specific data from websites using libraries
like BeautifulSoup or Scrapy. This task will
improve their knowledge of web scraping
techniques and handling HTML/XML data.

"""

# Description:
# This script scrapes the IMDb Top 250 movies page, extracts details for each movie 
# (such as rank, title, release year, duration, parental rating, IMDb rating, and IMDb ID), 
# and saves the results in a pandas DataFrame. It uses requests to fetch the HTML, BeautifulSoup 
# to parse and extract data, and pandas for tabular representation.

import requests
from bs4 import BeautifulSoup

def fetch_and_save_html(url, path):
    """
    Fetches the HTML content from the specified URL and saves it to a file.
    Args:
        url (str): The URL of the webpage to fetch.
        path (str): The file path where the HTML content will be saved.
    """
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers)

    with open(path, "w", encoding="utf-8") as file:
        file.write(response.text)


def extract_movie_details(movie):
    """
    Extracts detailed information about a movie from a BeautifulSoup element.
    Parameters:
        movie (bs4.element.Tag): A BeautifulSoup Tag object representing a movie entry.
    Returns:
        list: A list containing the following movie details:
            - movie_rank (int): The rank of the movie.
            - movie_title (str): The title of the movie.
            - release_year (int): The year the movie was released.
            - duration (str): The duration of the movie.
            - parental_rating (str): The parental guidance rating of the movie.
            - imdb_rating (float): The IMDb rating of the movie.
            - imdb_id (str): The IMDb ID of the movie.
    """
    
    # Extract the index and title from the movie header
    title_block = movie.h3.text.strip()
    movie_rank = int(title_block.split(".")[0].strip())
    movie_title = title_block.split(".")[1].strip()

    # Extract year, duration, and parental guidance rating
    metadata_items = movie.select("span.sc-29531a57-8.cxFOWT.cli-title-metadata-item")
    release_year = int(metadata_items[0].text.strip())
    duration = metadata_items[1].text.strip()
    parental_rating = metadata_items[2].text.strip()

    # Get IMDb rating
    imdb_rating = float(movie.select_one("span.ipc-rating-star--rating").text.strip())

    # Extract IMDb ID from URL
    imdb_href = movie.select_one("a.ipc-lockup-overlay.ipc-focusable").get("href")
    imdb_id = imdb_href.split("/")[2]

    return [
        movie_rank,
        movie_title,
        release_year,
        duration,
        parental_rating,
        imdb_rating,
        imdb_id,
    ]


# url = "https://www.nytimes.com/interactive/2025/movies/best-movies-21st-century.html"
imdb_url = "https://www.imdb.com/chart/top/"
html_save_path = "data/sample.html"

# Fetch and save the IMDb Top 250 page
fetch_and_save_html(imdb_url, html_save_path)

# Read the saved HTML file
with open(html_save_path, "r", encoding="utf-8") as html_file:
    imdb_html_content = html_file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(imdb_html_content, "html.parser")

# Select all movie list items
movies = soup.select("li.ipc-metadata-list-summary-item")

# Extract and print details for each movie
# for movie_element in movie_elements:
#     movie_details = extract_movie_details(movie_element)
#     print(movie_details)


import pandas as pd

data = [extract_movie_details(movie) for movie in movies]

df = pd.DataFrame(data, columns=["Index", "Title", "Year", "Duration", "PG Rating", "IMDB Rating", "IMDB ID"])
# print(df)
print(df.head())