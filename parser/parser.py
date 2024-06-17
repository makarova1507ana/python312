from bs4 import BeautifulSoup
with open("example.html", encoding="UTF-8") as f:
    html_doc = f.read()

# print(html_doc, type(html_doc))

#print("------------------------------------------------------")
soup = BeautifulSoup(html_doc, 'lxml')
#print(soup, type(soup))

# title = soup.title
# print(title, type(title))
# print(title.text, type(title.text))


# -----------поиск элементов--------------- #
# .find
# .find_all()

# p = soup.find('p')
# print(p, type(p))
# print(p.text, type(p.text))

# elements = soup.find_all('p')
# print(elements, type(elements))
# for el in elements:
#     print(el.text, type(el.text))

# story = soup.find('.story')
# print(story, type(story)) # None <class 'NoneType'> Не нашел такой элемент

# story = soup.find('p', class_='story')
# print(story, type(story))



# # Поиск с использованием CSS селекторов
# story_paragraph = soup.select_one('.story')
# print(story_paragraph, story_paragraph.text, type(story_paragraph), sep=' | ')  # Вывод: Пример текста.
#

# # получение атрибутов
# link = soup.find('a')
# print(link['href'])  # Вывод: http://example.com/page1
# print(link.get('class'))  # Вывод: ['link']
# print(link.get('href'))  # Вывод: http://example.com/page1



# # ----------------------------- навигация -----------------------------#
# # .find_parent() .find_parents()
#
# span = soup.find('span')
# print(span)
# print('--------------------------------------')
# span_parent = span.find_parent()
# print(span_parent)
#
# print('--------------------------------------')
# span_parents = span.find_parents()
# for parent in span_parents:
#     print('*****************************************')
#     print(parent )


# # .next_element()  .previous_element()
# p = soup.find('p')
# print(p)
# print('--------------------------------------')
# p_child = p.next_element
# print(p_child)
#
# print('--------------------------------------')
# p_child = p.next_element.next_element
# print(p_child)

# print('--------------------------------------')
# span = soup.find('span')
# print(span)
# print('--------------------------------------')
# span_prev = span.previous_element.previous_element.previous_element # найдем брата
# print(span_prev)


# # # .findChild() .findChildren()
#
# p = soup.find('p')
# print(p)
#
# # print('--------------------------------------')
# # p_child = p.findChild('span')
# # print(p_child)
#
# # print('--------------------------------------')
# # p_children = p.findChildren('b')
# # print(p_children)



# --------------сосдение элементы--------------#
# .find_next_sibling() .find_previous_sibling()

# story = soup.find_all('p')[1]
# print(story)

# print('--------------------------')
#
# next_sib = story.find_next_sibling()
# print(next_sib)

# print('--------------------------')
#
# prev_sib = story.find_previous_sibling()
# print(prev_sib)


# --------------по содержимому  текста --------------#

# primer = soup.find(string='Пример') # text можно использовать и для find и для select_one
# print(primer)

# import re
# story_primer = soup.find_all(string=re.compile('[Пп]ример'))
# print(story_primer)


# # пример с комбинацией
# import re
# story_primer = soup.find(string=re.compile('[Пп]ример')).findParent()
# print(story_primer)