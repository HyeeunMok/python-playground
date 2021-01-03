import requests
from bs4 import BeautifulSoup
import smtplib
import config

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}
SENDER_EMAIL = config.sender_eamil
PASSWORD = config.password
RECIPIENT_EMAIL = config.recipient_email

response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")
price = soup.find(id="priceblock_ourprice").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").getText().strip()
print(title)

BUY_PRICE = 200
if price_as_float < BUY_PRICE:
    message = f"{title} is now ${price_as_float}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(SENDER_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=RECIPIENT_EMAIL,
            msg=f"Subject: Amazon Price Alert!\n\n{message}\n{url}".encode("utf8")
        )

