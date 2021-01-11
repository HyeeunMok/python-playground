from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://en.wikipedia.org/wiki/Main_Page"
chrome_driver_path = "/Users/hyeeun/Projects/chromedriver"
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

article_count = driver.find_element_by_css_selector("#articlecount a")
article_count_text = article_count.text
# print(article_count_text)
# article_count.click()

all_portals = driver.find_element_by_link_text("All portals")
# all_portals.click()

search = driver.find_element_by_name("search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)




# driver.quit()