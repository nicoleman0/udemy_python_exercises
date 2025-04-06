import sqlite3
import requests
from bs4 import BeautifulSoup


def scrape_books(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    all_books = []
    for book in books:
        book_data = (get_title(book), get_price(book), get_rating(book))
        all_books.append(book_data)
    return all_books


def get_title(book):
    return book.find('h3').find('a')['title']


def get_price(book):
    price = book.select('.price_color')[0].get_text()
    float(price.replace('£', '').replace('Â', ''))
    return price


def get_rating(book):
    ratings = {
        'Zero': 0,
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5,
    }

    paragraph = book.select('.star-rating')[0]
    word = paragraph.get_attribute_list('class')[-1]
    return ratings[word]


book_list = scrape_books(
    'https://books.toscrape.com/catalogue/category/books/history_32/index.html')

print(book_list)
