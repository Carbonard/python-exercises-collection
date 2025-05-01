"""
Wikipedia Section Extractor

This script extracts and lists items from a specific section or subsection of a Wikipedia page.

The user provides:
1. A Wikipedia URL.
2. The name of the section or subsection to extract.
3. The section type: <h2> for main sections, <h3> for subsections.

The program will:
1. Request the given URL and parse the page.
2. Search for the specified section or subsection in the HTML.
3. Allow the user to select which sections to extract data from and when to stop.
4. Extract items from <i> tags in tables, excluding any that contain <span> tags.
5. Print the results in a numbered list that reflects the hierarchy of sections.

The program uses nested loops to dynamically handle varying levels of sections and subsections.

Dependencies:
- requests: For making the HTTP request to the Wikipedia page.
- BeautifulSoup (from bs4): For parsing the HTML content.
"""

import requests
from bs4 import BeautifulSoup, Tag

# Granting questoins answered as desired
def answer(question):
    ans = None
    while not ans in ['y','n']:
        ans = input(question + " (yes/no) ")
        if ans:
            ans = ans.lower()[0]
    return ans == 'y'

url = input("Introduce url from wikipedia: ")
section = input("Introduce section name: ").lower()
level = input("Kind of section? (h2 for sections / h3 for subsections): ").lower()

# To avoid the use of global variables in the nested loops
class SearchContext:
    def __init__(self):
        self.count_section = 0
        self.count_subsection = 0
        self.count_list = 0
        self.is_target_section = False
context=SearchContext()

# To exit from the nested loops if needed
class StopSearch(Exception):
    pass

collected_data = []

# Recursively goes through the HTML tree and processes relevant sections and tables
def search_for_interest(tag, context):
    if isinstance(tag, Tag):
        if tag.name == "h2":
            # Possible section of interest
            if section in tag.get_text().lower() and level=='h2':
                if answer(f"Collect data from section {tag.get_text()}?"):
                    context.count_section += 1
                    context.count_subsection = 0
                    context.count_list = 0
                    collected_data.append("-"*30+"Section: "+tag.get_text()+"-"*30)
                    context.is_target_section = True
                else:
                    if not answer("Keep collecting data?"):
                        raise StopSearch
            else:
                context.is_target_section = False
        elif tag.name == "h3":
            # Possible subsection of interest
            if level == 'h2' and context.is_target_section:
                if answer(f"Collect data from subsection {tag.get_text()}?"):
                    context.count_subsection +=1
                    context.count_list = 0
                    collected_data.append("-"*20+"Subsection: "+tag.get_text()+"-"*20)
                else:
                    if not answer("Keep collecting data?"):
                        raise StopSearch
            elif level == 'h3' and section in tag.get_text().lower():
                if answer(f"Collect data from subsection {tag.get_text()}?"):
                    context.is_target_section = True
                    context.count_subsection +=1
                    context.count_list = 0
                    collected_data.append("-"*20+"Subsection: "+tag.get_text()+"-"*20)
                else:
                    if not answer("Keep collecting data?"):
                        raise StopSearch
            else:
                context.is_target_section = False
        # If a table is found inside a selected section, extract the desired content
        elif context.is_target_section and tag.name == "table":
            for i in tag.find_all("i"):
                if isinstance(i, Tag) and not i.find('span'):
                    context.count_list += 1
                    if level=='h2':
                        collected_data.append(f"{context.count_section}.{context.count_subsection}.{context.count_list}. {i.get_text()}")
                    else:
                        collected_data.append(f"{context.count_subsection}.{context.count_list}. {i.get_text()}")
        for tag_child in tag.children:
            search_for_interest(tag_child, context)

response = requests.get(url)
if response.status_code == 200:
    print("Successful request.")
    soup = BeautifulSoup(response.content, 'html.parser')
    try:
        search_for_interest(soup.body, context)
    except StopSearch:
        pass
else:
    print("Failed request.")

# Display collected data
if collected_data:
    for item in collected_data:
        print(item)