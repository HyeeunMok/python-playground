from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

url = "https://www.python.org/"
chrome_driver_path = "/Users/hyeeun/Projects/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text
    }

print(events)

driver.quit()


# price = driver.find_element_by_id("priceblock_ourprice")
# print(price.text)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# logo = driver.find_element_by_class_name("python-logo")
# print(logo.size)
#
# documentation_link = driver.find_element_by_css_selector(".documentation-widget a")
# print(documentation_link.text)
#
# bug_link_text = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link_text.text)
#
# bug_link = driver.find_element_by_xpath('//*[@id="site-map"]/div[2]/div/ul/li[3]/a').get_attribute('href')
# print(bug_link)
#
# driver.find_elements_by_css_selector()



# driver.close()
# driver.quit()
