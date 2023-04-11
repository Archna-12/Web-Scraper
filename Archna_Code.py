import requests
import csv
import sqlite3
import datetime
from bs4 import BeautifulSoup


class Article:
    def __init__(self, headline, url, author, date):
        self.headline = headline
        self.url = url
        self.author = author
        self.date = date


class VergeScraper:
    def __init__(self):
        self.articles = []
        self.base_url = 'https://www.theverge.com'

    def scrape(self):
        # Send a GET request to theverge.com and parse the HTML
        response = requests.get(self.base_url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all article elements
        article_elements = soup.find_all('article')

        # Extract article data and create Article objects
        for article_element in article_elements:
            headline = article_element.find('h2').text.strip()
            url = article_element.find('a')['href']
            author = article_element.find('span', class_='c-byline__author').text.strip()
            date = article_element.find('time')['datetime']
            article = Article(headline, url, author, date)
            self.articles.append(article)

    def save_to_csv(self):
        # Generate the CSV filename based on the current date
        today = datetime.datetime.now().strftime('%d%m%Y')
        filename = f'{today}_verge.csv'

        # Write article data to the CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'URL', 'headline', 'author', 'date'])
            for i, article in enumerate(self.articles, start=1):
                writer.writerow([i, article.url, article.headline, article.author, article.date])

        print(f'Saved articles to {filename}')

    def save_to_sqlite(self):
        # Generate the SQLite database filename based on the current date
        today = datetime.datetime.now().strftime('%d%m%Y')
        filename = f'{today}_verge.db'

        # Create SQLite database and table
        conn = sqlite3.connect(filename)
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS articles
                     (id INTEGER PRIMARY KEY, URL TEXT, headline TEXT, author TEXT, date TEXT)''')

        # Insert article data into the table
        for i, article in enumerate(self.articles, start=1):
            c.execute("INSERT INTO articles (id, URL, headline, author, date) VALUES (?, ?, ?, ?, ?)",
                      (i, article.url, article.headline, article.author, article.date))

        conn.commit()
        conn.close()

        print(f'Saved articles to {filename}')


if __name__ == '__main__':
    scraper = VergeScraper()
    scraper.scrape()
    scraper.save_to_csv()
    scraper.save_to_sqlite()
