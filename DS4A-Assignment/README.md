Financial Data Aggregator and Analyzer

# Introduction:

In today’s data-driven world, financial analysts and investors require timely access to accurate and comprehensive financial data to make informed decisions. The finance industry generates vast amounts of data from various sources, including stock markets, financial news, and company financial statements. By aggregating, analyzing, and visualizing this data, analysts and investors can identify trends, evaluate risks, and discover investment opportunities.

# Objective:

The objective of the Financial Data Aggregator and Analyzer project is to create an end-to-end Extract, Transform, Load (ETL) pipeline that consolidates and processes financial data from multiple sources. This pipeline will empower you to practice essential data engineering skills, such as data collection, data transformation and data loading while working with real-world financial data. By implementing this project, you will gain hands-on experience in utilizing Python, APIs, Web Scraping, and SQL to address challenges in the finance industry.

1. Extraction:

   1. Financial News: Scrape financial news websites from [CNBC](https://www.cnbc.com/stocks/) using web scraping libraries such as BeautifulSoup to collect all the headlines that are present in the page at the moment of performing the requests. Save the timestamp of the moment you realized the request in some variable.
   2. Stock Market Data: Use Alpha Vantage API to extract stock market data. Get historical stock prices for the following companies:

   - Apple
   - Microsoft
   - Google
   - Amazon
   - Meta

   Reference to [Alpha Vantage API documentation](https://www.alphavantage.co/documentation/) to get the correct way of using the API. Remember to ask for your free API Key.

2. Transformation:

   1. Sentiment Analysis: Business would like to know the sentiment of the financial stocks news headlines that you extracted. The headlines are short and concise, and they reflect the latest developments and trends in the stock market. They want to know if the headlines are positive, negative, or neutral in terms of their emotional tone and impact on the investors.

   For this you can use a library called [textblob](https://textblob.readthedocs.io/en/dev/) and apply the sentiment polarity method. Save the polarity score in a new column called `sentiment_score`. If the result obtained is between -1 and -0.2 classify the sentiment as negative, if it is between -0.2 and 0.2 classify it as neutral, else classify it as positive. Save this classification into a new column called `sentiment`.

   2. Relevant Words: Business wants to know which might be the most relevant words for each headline. For this you can use the [word_tokenize](https://www.nltk.org/api/nltk.tokenize.html) function from nltk.tokenize library. Create a column called relevant_words to save the result for this task.

   3. Headlines Translation: Business wants to translate the headlines to Spanish and Italian; it seems they are working on some interesting projects for new markets. Translate the headlines to these two languages. You can use googletrans library to achieve this. Please save the translated headlines in two new columns headline_spanish and headline_it for saving translated headlines to Spanish and to Italian respectively.

   4. Save data: Save data from scrapped headlines into a csv file called headlines_data.csv under the path: data/headlines. The file should contain the following columns:
      |Column Name| Description|
      |headline| The title or headline of the article in English|
      |url| The URL of the article|
      timestamp The date and time the article was scrapped
      sentiment_score A numerical value indicating the sentiment of the article
      sentiment A categorical value indicating the sentiment of the article, such as “positive,” “negative,” or “neutral”
      relevant_words A list of words that are relevant to the article’s content
      headline_es The translated version of the headline in Spanish
      headline_it The translated version of the headline in Italian
      e. Stocks Data Transformation: Using an API for collecting data usually is a good idea. One of the advantages is that normally data comes in a structured or semi-structured way so data transformations are easier. For this data you just need to apply simple transformations to the stocks data you collected before so it follows following structure:
      Column Name Description
      date The date on which the stock price was recorded.
      open_price The price at which the stock opened on the given date.
      highest_price The highest price of the stock on the given date.
      lowest_price The lowest price of the stock on the given date.
      close_price The price at which the stock closed on the given date.
      volume The total number of shares traded on the given date.
      symbol A unique identifier that represents a particular stock symbol.
      f. Save Data: Save the data into a CSV file called stocks_data.csv under the path data/stocks.

3) Load:
   a. Create SQLite Database: Install SQLite in your machine and create a database called etl_extended_case.
   b. Create Tables: Create two tables headlines and stocks for loading headlines and stocks data respectively.
   c. Load Data From CSV Files: Load data from CSV files (headlines_data.csv and stocks_data.csv) into created tables in the SQLite database.
   b and c steps should be accomplished programmatically, that means, a script should do it.
