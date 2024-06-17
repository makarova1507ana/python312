import json

from bs4 import BeautifulSoup
import requests



# находим главную новость
def get_main_news(page):
    html_doc = requests.get(f'https://ria.ru/{page}/').content

    # print(html_doc, type(html_doc))

    soup = BeautifulSoup(html_doc, 'lxml')

    main_news = soup.find(class_='cell-list-f__main')
    #print(main_news) # скорее нужно для отладки

    link_main_news = main_news.find('a').get('href')
    #print(link_main_news)

    title_main_news = soup.find(class_='cell-list-f__main-title').text
    #print(title_main_news)

    image_main_news = soup.find('picture').next_element.next_sibling.get('srcset')
    #print(image_main_news)
    return link_main_news, title_main_news, image_main_news


def write_to_txt(*args: str):
    with open('main_news_culture.txt', 'w') as f:
        f.write(', '.join(args))

def write_to_json(link_main_news: str, title_main_news: str, image_main_news: str):
    data ={
        'ссылка': link_main_news,
        'заголовок': title_main_news,
        'изображение': image_main_news
    }
    with open('main_news_culture.json', 'w', encoding='utf-16') as f:
        json.dump(data, f)

# -----#
link_main_news, title_main_news, image_main_news = get_main_news('science')
print(f'''
ссылка: {link_main_news}
заголовок: {title_main_news}
изображение: {image_main_news}''')

write_to_json(link_main_news, title_main_news, image_main_news)
write_to_txt(link_main_news, title_main_news, image_main_news)
