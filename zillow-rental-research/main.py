import requests
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from time import sleep

ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.79107130957031%2C%22east%22%3A-122.07558669042969%2C%22south%22%3A37.56196014937253%2C%22north%22%3A37.98800895300511%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
headers = {
    "Accept-Language": "en-US,en;q=0.9,ko;q=0.8",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"
}

response = requests.get(url=ZILLOW_URL, headers=headers)
data = response.text

soup = BeautifulSoup(data, "html.parser")
# print(soup)

all_link_elements = soup.select(".list-card-top a")
# print(all_link_elements)

all_links = []

for link in all_link_elements:
    # href = link.get("href")
    href = link["href"]
    # print(href)
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

all_address_elements = soup.select(".list-card-info a")
# print(all_address_elements)
all_addresses = [address.getText().split(" | ")[-1] for address in all_address_elements]
# print(all_addresses)

all_price_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_price_elements:
    # Get the prices. Single and multiple listings have different tag & class structures
    price = 0
    try:
        # Price with only one listing
        price = element.select(".list-card-price")[0].contents[0]
        print(price)
    except IndexError:
        print('Multiple listings for the card')
        # Price with multiple listings
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)
print(all_prices)


# Create Spreadsheet using Google Form
GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdoYsSzI_4flZ3qPJ998GX7uqIzpvwRjL-rnACOUtNANfl-UA/viewform"
chrome_driver_path = "/Users/hyeeun/Projects/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_URL)

    sleep(2)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()





