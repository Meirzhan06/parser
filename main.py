import requests
from bs4 import BeautifulSoup

# Задайте URL сайта, с которого начнем
initial_url = "https://krisha.kz/prodazha/kvartiry/astana/"

# Отправляем GET-запрос к начальной ссылке
response = requests.get(initial_url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Создаем объект BeautifulSoup для разбора HTML-кода страницы
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Находим первый тег a с классом a-card__image
    a_card_image = soup.find('a', class_='a-card__image')
    
    if a_card_image:
        # Получаем значение атрибута href
        href_value = a_card_image.get('href')
        
        # Собираем абсолютную ссылку
        absolute_url = "https://krisha.kz" + href_value
        
        # Отправляем GET-запрос к абсолютной ссылке
        response = requests.get(absolute_url)
        
        if response.status_code == 200:
            # Создаем объект BeautifulSoup для разбора HTML-кода новой страницы
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Находим div с атрибутом data-name="live.square"
            live_square_div = soup.find('div', {'data-name': 'live.square'})
            
            if live_square_div:
                # Находим div с классом "offer__advert-short-info" внутри div с атрибутом data-name="live.square"
                advert_short_info_div = live_square_div.find('div', class_='offer__advert-short-info')
                
            if advert_short_info_div:
                # Получаем текстовое содержимое этого div
                advert_short_info_text = advert_short_info_div.text
                
                # Удаляем все буквы и оставляем только цифры и символы
                cleaned_text = ''.join(filter(str.isdigit, advert_short_info_text))
                
                # Удаляем последний элемент (последнюю цифру)
                cleaned_text = cleaned_text[:-1]
                
                # Выводим текст в консоль
                print(cleaned_text)
            else:
                print("Div с классом 'offer__advert-short-info' не найден в div с атрибутом data-name='live.square'.")

            # Находим div с классом "offer__sidebar-header"
            sidebar_header_div = soup.find('div', class_='offer__sidebar-header')
            
            if sidebar_header_div:
                # Находим первый элемент внутри div (recursive=False)
                first_element_inside_div = sidebar_header_div.find(recursive=False)
                
                if first_element_inside_div:
                    # Получаем текстовое содержимое первого элемента
                    first_element_text = first_element_inside_div.text
                    
                    # Удаляем все буквы и оставляем только цифры и символы
                    cleaned_text = ''.join(filter(str.isdigit, first_element_text))
                    
                    # Выводим текст в консоль
                    print(cleaned_text)
                else:
                    print("Первый элемент внутри div с классом 'offer__sidebar-header' не найден.")
            else:
                print("Div с классом 'offer__sidebar-header' не найден на странице.")
            
        else:
            print("Ошибка при запросе к странице", absolute_url)
    else:
        print("Тег a с классом 'a-card__image' не найден на начальной странице.")
else:
    print("Ошибка при запросе к начальной странице. Код ответа:", response.status_code)
