from typing import Iterable

import bs4
import requests


def display_authors(page_number: int = 1):
    url = "http://quotes.toscrape.com/page/{}"

    authors = set()
    while True:
        try:
            response = requests.get(url.format(page_number))
            response.raise_for_status()
        except requests.exceptions.RequestException:
            break
        soup = bs4.BeautifulSoup(response.text, "lxml")
        author_list = soup.select(".author")

        if not author_list:
            break

        authors.update(author_name.contents[0] for author_name in author_list)
        page_number += 1

    display_list(authors)


def display_list_of_quotes(page_number: int = 1):
    url = "http://quotes.toscrape.com/page/{}"
    response = requests.get(url.format(page_number))
    soap = bs4.BeautifulSoup(response.text, "lxml")
    quotes = list(quote.contents[0] for quote in soap.select(".text"))
    display_list(quotes)


def display_top_tags():
    page_number = 1
    url = "http://quotes.toscrape.com/page/{}"
    response = requests.get(url.format(page_number))
    soap = bs4.BeautifulSoup(response.text, "lxml")
    tags = list(tag.contents[0] for tag in soap.select(".tag-item > .tag"))
    display_list(tags)


def display_list(iterable: Iterable):
    for index, element in enumerate(iterable):
        print(f"{index + 1}.{element}")


def divider(title: str):
    print(f"=========={title.upper()}===========")


if __name__ == '__main__':
    divider("display authors")
    display_authors()

    divider("display quotes")
    display_list_of_quotes(2)

    divider("display top tags")
    display_top_tags()
