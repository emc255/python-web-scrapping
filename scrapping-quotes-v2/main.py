import bs4
import requests


def authors_and_quotes():
    page_number = 1
    url = "https://quotes.toscrape.com/page/{}/"
    authors_and_quotes_dict = {}
    while True:
        try:
            response = requests.get(url.format(page_number))
            response.raise_for_status()
        except requests.exceptions.RequestException:
            break

        soap = bs4.BeautifulSoup(response.text, "lxml")
        quotes = soap.select(".quote")

        if not quotes:
            break

        for quote in quotes:
            author = quote.find("small", class_="author").text.strip()
            text = quote.find("span", class_="text").text.strip()
            if author in authors_and_quotes_dict:
                authors_and_quotes_dict[author].append(text)
            else:
                authors_and_quotes_dict[author] = [text]
        page_number += 1

    for index, (key, values) in enumerate(authors_and_quotes_dict.items()):
        print(f"{index + 1}.{key}")
        for i, value in enumerate(values):
            print(f"\t{i + 1}.{value}")
        print("")


if __name__ == '__main__':
    authors_and_quotes()
