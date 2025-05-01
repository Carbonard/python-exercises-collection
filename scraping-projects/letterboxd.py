# This program scrapes and save in a dataframe the films from a specified Letterboxd user's profile by iterating through the pages.

import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

user = input("Introduce user name on Letterboxd: ")

counter_films=0
page=0
films_df = pd.DataFrame(columns=["Film Title", "Rating"])

while True:
    page += 1
    url = "https://embed.letterboxd.com/" + user + "/films/page/" + str(page) + "/"
    # Avoid server overloads by introducing a small delay between requests:
    time.sleep(2)
    response = requests.get(url)
    # Check if the page was read correctly:
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        films = soup.find_all('div', class_='film-poster')
        # Check if there are films on page
        if films:
            for film_div in films:
                counter_films += 1
                rate_span = film_div.parent.find('p', class_='poster-viewingdata').select_one('span')
                # If the film is rated by the user, extract the rating
                if rate_span:
                    rate_classes = rate_span['class']
                    rated_class = next((c for c in rate_classes if c.startswith('rated-')), False)
                    rate = int(rated_class.split('-')[1]) if rated_class else -1
                else:
                    rate=None
                if rate:
                    films_df = films_df._append({"Film Title": film_div.find('img')['alt'], "Rating": rate}, ignore_index=True)
                else:
                    films_df = films_df._append({"Film Title": film_div.find('img')['alt'], "Rating": rate}, ignore_index=True)
        else:
            print(f"{page-1} pages read.")
            break
    else:
        # If reading page failed, try again
        page -=1
        continue

for index, (film_title, rating) in enumerate(zip(films_df["Film Title"], films_df["Rating"])):
    print(f"{index+1}. {film_title} ({rating}/10)")