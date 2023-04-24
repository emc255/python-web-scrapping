import bs4
import requests


def get_title(domain_name: str):
    result = requests.get(domain_name)
    # print(result.text)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    print(soup)
    title = soup.select("title")
    print(title)
    print(title[0].getText())
    p_tag = soup.select("p")
    print(type(p_tag))
    print(p_tag)
    print(p_tag[0].getText())


def divider(title: str):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    divider("GET TITLE")
    get_title("https://example.com/")
