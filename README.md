# Web-Scraper
Web-Scraping
implementation of a web scraper using Python to read articles from theverge.com, store the data in a CSV file and SQLite database, and run it on an AWS Lambda function using AWS S3 for storage.
This implementation uses the BeautifulSoup library to scrape the HTML content of theverge.com, extract the article data, and store it in a CSV file and SQLite database. The Article class represents an article with its attributes like headline, URL, author, and date. The VergeScraper class handles the scraping logic and provides methods to save the scraped data to CSV and SQLite. The if __name__ == '__main__': block is used to run the scraper when the script is executed directly.

To run this scraper on AWS, you can create an AWS
