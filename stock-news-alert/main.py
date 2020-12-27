import requests
from twilio.rest import Client
import config

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = config.stock_api_key
NEWS_API_KEY = config.news_api_key

#Twilio
ACCOUNT_SID = config.twilio_account_sid
AUTH_TOKEN = config.twilio_auth_token
TWILIO_PHONE_NUMBER = config.twilio_phone_num
RECIPIENT_PHONE_NUMBER = config.recipient_phone_num

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}

# Get yesterday's closing stock price.
response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
# Get the day before yesterday's closing stock price
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

# Find the positive difference between 1 and 2.
difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)

up_down = None
if difference > 0:
    up_down = "🔺"
elif difference < 0:
    up_down = "🔻"
else:
    up_down = ""

# Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percentage = round((difference / float(yesterday_closing_price)) * 100, 2)

# If the diff_percentage is greater than 5 then get the first 3 news pieces for the COMPANY_NAME.
if abs(diff_percentage) > 2:
    news_params = {
        "qInTitle": COMPANY_NAME,
        "SortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_data = news_response.json()
    articles = news_data["articles"]
    # Use Python slice operator to create a list that contains the first 3 articles.
    three_articles = articles[:3]

# Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    #Send each article as a separate message via Twilio.
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages \
            .create(
            body=f"{STOCK_NAME}: {up_down}{diff_percentage}%\n{article}",
            from_=TWILIO_PHONE_NUMBER,
            to=RECIPIENT_PHONE_NUMBER
        )

        print(message.status)

