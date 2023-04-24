import os

import bs4
import requests


def save_images_wiki(domain_name: str, image_class_name: str):
    result = requests.get(domain_name)
    soup = bs4.BeautifulSoup(result.text, "lxml")
    title = get_title_text(soup)
    save_images(title, soup, image_class_name)


def get_title_text(soup):
    return soup.select("title")[0].text.split("-")[0].replace(" ", "-")


def save_images(title, soup, image_class_name):
    folder_name = "resources/images"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    img_list = soup.select(image_class_name)
    for index, img in enumerate(img_list):
        image = requests.get(f'https:{img["src"]}')
        if image.status_code == 200:
            file_name = f"{folder_name}/{title}{index + 1}.jpg" if index + 1 >= 10 \
                else f"resources/images/{title}0{index + 1}.jpg"
            with open(file_name, "wb") as file:
                file.write(image.content)


def divider(title: str):
    print(f"=========={title.upper()}==========")


if __name__ == '__main__':
    divider("save images wiki")
    save_images_wiki("https://en.wikipedia.org/wiki/Scarlett_Johansson", ".thumbimage")
    save_images_wiki("https://en.wikipedia.org/wiki/Chess", ".thumbimage")
