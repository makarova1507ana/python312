"""
Извлечение данных о погоде с метеосайта:
Задание: Напишите скрипт для получения текущей погоды (температура, влажность, скорость ветра)
с выбранного метеосайта.
Пример сайта: Gismeteo
Ожидаемый результат: Текущие метеоданные в формате текста или JSON.
"""

'''
план
1. Анализ структуры HTML
2. Продумать стратегию поиска элемента(ов)
3. Написание парсера

итоговый результат: 
дата: ХХ.ХХ.ХХХХ
температура: ХХ цельсий
влажность: ХХ %
скорость: ХХ м/с
записанные в формате JSON
'''
import json
from bs4 import BeautifulSoup
import requests


def main_page():
    html_doc = requests.get(
        'https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%9C%D0%B0%D0%BD%D0%B8%D0%BB%D0%B5,_%D0%A4%D0%B8%D0%BB%D0%B8%D0%BF%D0%BF%D0%B8%D0%BD%D1%8B')
    soup = BeautifulSoup(html_doc.content, 'lxml')
    # print(soup)
    date = soup.find(class_='weekDay').text.strip()
    temperature = soup.find(class_='t_0').text.strip()
    speed = soup.find(class_='wv_0').text.strip()
    return date, temperature, speed


def json_writer(date: str, temperature: str, speed: str):
    data = {
        'время': date,
        'температура': temperature,
        'скорость ветра': speed
    }

    with open('rp5_stats.json', 'w', encoding='utf-16') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


date, temperature, speed = main_page()
print(date, temperature, speed)
json_writer(date, temperature, speed)