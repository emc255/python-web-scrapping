#
from enum import Enum

import bs4
import requests


class Rating(Enum):
    One = "One"
    Two = "Two"
    Three = "Three"
    Four = "Four"
    Five = "Five"


def book_scrapping(rating: Rating):
    page_number = 1
    base_url = "https://books.toscrape.com/catalogue/page-{}.html"
    books = []

    while True:
        try:
            response = requests.get(base_url.format(page_number))
            response.raise_for_status()
        except requests.exceptions.RequestException:
            break

        soup = bs4.BeautifulSoup(response.text, "lxml")
        products = soup.select(".product_pod")
        has_rating(books, products, rating)
        page_number += 1

    print_loop(books)

    # folder_name = "resources/books"
    # if not os.path.exists(folder_name):
    #     os.makedirs(folder_name)


def has_rating(books: list, products, rating: Rating):
    for product in products:
        if len(product.select(f".star-rating.{rating.value}")):
            book_name = product.find("h3").find("a")["title"]
            books.append(book_name)


def print_loop(array_list: list):
    for index, array in enumerate(array_list):
        print(f"{index + 1}. {array}")


if __name__ == '__main__':
    # find all <p> elements with the class "my-class"
    # find the first <p> element in the HTML document
    book_scrapping(Rating.Four)
