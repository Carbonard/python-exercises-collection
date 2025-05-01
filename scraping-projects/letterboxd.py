# This program scrapes and lists the films from a specified Letterboxd user's profile by iterating through the pages.

import requests
from bs4 import BeautifulSoup
import time

user = input("Introoduce user name on Letterboxd: ")

count=0
page=0

while True:
    page += 1
    url = "https://embed.letterboxd.com/" + user + "/films/page/" + str(page) + "/"
    response = requests.get(url)
    time.sleep(3)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        films = soup.find_all('div', class_='film-poster')
        # If there are more untracked films
        if films:
            for film_div in films:
                count += 1
                rate_span = film_div.parent.find('p', class_='poster-viewingdata').select_one('span')
                # If the film is rated by the user, collect the rate
                if rate_span:
                    rate_classes = rate_span['class']
                    rated_class = next((c for c in rate_classes if c.startswith('rated-')), False)
                    rate = int(rated_class.split('-')[1]) if rated_class else -1
                else:
                    rate=False
                if rate:
                    print(f"{count}. {film_div.find('img')['alt']} ({rate}/10)")
                else:
                    print(f"{count}. {film_div.find('img')['alt']}")
        else:
            print(f"{page-1} pages read.")
            break
    else:
        # print(f"Failed reading page {page}.")
        page -=1
        continue