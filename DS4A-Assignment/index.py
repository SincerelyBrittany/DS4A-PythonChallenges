# Import Libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from textblob import TextBlob
from nltk.tokenize import word_tokenize
import sqlite3

# Send a request to CNBC website and retrieve the HTML content
url = "https://www.cnbc.com/stocks"
response = requests.get(url)
html_content = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the headlines on the webpage using the appropriate HTML tags and class names
headlines = soup.find_all("a", class_="Card-title")

# Create lists to store the headlines and timestamps
headline_list = []
timestamp_list = []

# Extract the headline text and current timestamp
for headline in headlines:
    headline_text = headline.get_text()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    headline_list.append(headline_text)
    timestamp_list.append(timestamp)

# Create a DataFrame from the extracted data
data = {
    'timestamp': timestamp_list,
    'headline': headline_list
}
df = pd.DataFrame(data)


def get_sentiment_polarity(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    return polarity


df['sentiment_score'] = df['headline'].apply(get_sentiment_polarity)

def classify_sentiment(score):
    if score < -0.2:
        return 'Negative'
    elif score > 0.2:
        return 'Positive'
    else:
        return 'Neutral'

df['sentiment'] = df['sentiment_score'].apply(classify_sentiment)


def extract_relevant_words(text):
    tokens = word_tokenize(text)
    return tokens

df['relevant_words'] = df['headline'].apply(extract_relevant_words)

# print(df['relevant_words'].head())

from googletrans import Translator
translator = Translator()
# StackOverflow to fix translator issue: https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group

# Translate the headlines to Spanish and save the translations in a new column 'headline_spanish'
df['headline_spanish'] = df['headline'].apply(lambda x: translator.translate(x, dest='es').text)

# # Translate the headlines to Italian and save the translations in a new column 'headline_italian'
df['headline_italian'] = df['headline'].apply(lambda x: translator.translate(x, dest='it').text)

# print(df.head())

file_path = "data/headlines/headlines_data.csv"
df.to_csv(file_path, index=False)

print("Headline data saved successfully!")

# Load data from the CSV file
csv_file = "data/headlines/headlines_data.csv"
df = pd.read_csv(csv_file)

# Establish a connection to the SQLite database
db_file = "my_database.db"
conn = sqlite3.connect(db_file)

# Create a table in the database using the DataFrame
table_name = "headlines"
df.to_sql(table_name, conn, if_exists="replace", index=False)

# Close the database connection
conn.close()

print("Table created in the SQLite database!")





import requests
import pandas as pd
from datetime import datetime

# Define your Alpha Vantage API key
api_key = "PHVOW5A6I113QTH2"
timestamp = datetime.now()

# Define the stocks you want to retrieve historical prices for
symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]

# Iterate over the stocks and make API requests
for stock in symbols:
    # Define the API endpoint URL with the necessary query parameters
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol={stock}&apikey={api_key}"
    
    # Send the HTTP request to the API
    response = requests.get(url)
    
    # Parse the JSON response into a DataFrame
    data = response.json()
    stockDF = pd.DataFrame(data["Monthly Time Series"]).T
 
    # Rename the columns for clarity
    stockDF.columns = [ "open_price", "highest_price", "lowest_price", "close_price", "volume"]
    

    
    # Print the historical prices for the current stock
    # print(f"Historical Prices for {stock}:")
    # print(stockDF)
    # print("-----------------------------------------")


    file_path = "data/stocks/stocks_data.csv"
    stockDF.to_csv(file_path, index=False)

    print("Stock data saved successfully!")

    # Load data from the CSV file
    csv_file = "data/headlines/stocks_data.csv"
    stockDF = pd.read_csv(csv_file)

    # Establish a connection to the SQLite database
    db_file = "my_database.db"
    conn = sqlite3.connect(db_file)

    # Create a table in the database using the DataFrame
    table_name = "stocks"
    stockDF.to_sql(table_name, conn, if_exists="replace", index=False)

    # Close the database connection
    conn.close()

    print("Table created in the SQLite database!")