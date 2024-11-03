# from selenium import webdriver

# # initialize the web driver
# driver = webdriver.Firefox()

# # Open the tutorials point website using get() method
# driver.get("https://www.ketabrah.ir/books/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%B1%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C?sort=populars")
from bs4 import BeautifulSoup
import requests
# url = 'https://www.ketabrah.ir/books/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%B1%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C?bt=books&sort=populars'
# response = requests.get(url)
# soup = BeautifulSoup(response.text, 'lxml')
# books_container = soup.find('div', class_="book-list")
# books_items = books_container.find_all('div', class_="item")
# for book in books_items:
#     book_name = book.find('a', class_='title').text.strip()
#     book_author = book.find('div', class_='authors').text.strip()
#     book_translator = book.find('div', class_='translator').text.strip() if book.find('div', class_='translator') else "مترجم موجود نیست"
#     book_publisher = book.find('div', class_='publisher').text.strip() if book.find('div', class_='publisher') else "ناشر موجود نیست"
#     print(f"نام کتاب: {book_name}")
#     print(f"نویسنده: {book_author}")
#     print(f"مترجم: {book_translator}")
#     print(f"ناشر: {book_publisher}")
#     print("-" * 40)
def publisher():
    html_text=requests.get('https://www.ketabrah.ir/books/%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D9%86%D9%84%D9%88%D8%AF-%DA%A9%D8%AA%D8%A7%D8%A8-%D8%AF%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D8%B1%D9%85%D8%A7%D9%86-%D8%AE%D8%A7%D8%B1%D8%AC%DB%8C?bt=books&sort=populars').text
    soup=BeautifulSoup(html_text , 'lxml')
    books=soup.find('div',class_="book-list")
    for link in books.find_all('a'):
        print(link.get('href'))
