"""
This program scrapes and saves in a CSV file the films from a specified Letterboxd user's diary by iterating through the pages.
The output CSV will be used for later data analysis and manipulation exercises.

Output CSV format:
- Watch Date: Date when the film was watched (YYYY-MM-DD)
- Film Title: Name of the film
- Release Date: Year the film was released
- Rating: User's rating (1-10), only present for rated films
"""

import requests
from bs4 import BeautifulSoup, Tag
import time
import pandas as pd
import re
from datetime import datetime
from os import path

# Class to maintain search state and avoid global variables in nested loops.
class SearchContext:
    def __init__(self):
        self.watch_date = None
        self.film_title = None
        self.film_released = None
        self.film_rating = None
        self.films_data=[]
        self.search_finished = False
    def set_date(self,date):
        self.watch_date = datetime.strptime(date, "%Y/%m/%d").date()
    def set_film_title(self,film):
        self.film_title = film
    def set_film_released(self,released):
        self.film_released = released
    def set_film_rating(self,rating):
        self.film_rating = rating

context = SearchContext()

# Loads HTML content from Letterboxd's diary pages.
def get_html(user,page):
    url = "https://embed.letterboxd.com/" + user + "/films/diary/page/" + str(page) + "/"
    while True:
        # Avoid server overloads by introducing a small delay between requests.
        time.sleep(2)
        response = requests.get(url)
        # Check if the page was read correctly.
        if response.status_code == 200:
            return response.content

# Decorator that implements recursive tree traversal for BeautifulSoup tags.
# Ensures the decorated function is called on all children of the current tag.
def recursive_search(func):
    def wrapper(tag, context):
        if not isinstance(tag, Tag):
            return
        func(tag,context)
        for tag_child in tag.children:
            wrapper(tag_child, context)
    return wrapper

# Processes HTML tags to extract film diary information.
@recursive_search
def search_for_interest(tag, context):
    # Search film's watch date.
    if tag.get('href'):
        date = re.search(r"\d{4}/\d{2}/\d{2}",tag.get('href'))
    else:
        date=False
    if date:
        context.set_date(date.group())
    # Search film's name.
    if tag.name=='h3':
        context.set_film_title(tag.get_text())
    # Search film's released date.
    if tag.name=='span' and re.search(r"\d{4}",tag.get_text()):
        context.set_film_released(tag.get_text())
    # Search film's user rating.
    if tag.get('class')!=None and any("rated" in cls for cls in tag.get('class')):
        # Check if the film is rated.
        if any("not-rated" in cls for cls in tag.get('class')):
            context.films_data.append({
                "watch_date": context.watch_date,
                "film_title": context.film_title,
                "release_year": context.film_released,
            })
        else:
            context.set_film_rating(re.search(r"\d+",tag.get('class')[1]).group())
            context.films_data.append({
                "watch_date": context.watch_date,
                "film_title": context.film_title,
                "release_year": context.film_released,
                "rating": context.film_rating
            })

page = 0
user = input("Introduce Letterboxd user: ")

# Main scraping loop.
while not context.search_finished:
    page += 1
    print("reading page",page)
    soup = BeautifulSoup(get_html(user,page), 'html.parser')
    search_for_interest(soup.body, context)
    # Detect if there is a next page
    if not any("Older" in a.get_text() for a in soup.body.find_all('a')):
        context.search_finished=True

# Convert collected data to Pandas DataFrame and save as CSV.
films_df = pd.DataFrame(context.films_data)
films_df.to_csv(path.join("scraping-projects","letterboxd",f"diary-{user}.csv"), index=False)