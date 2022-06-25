from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

driver = webdriver.Firefox()
# driver.get("https://melcom.com/categories/food-beverages-toiletries/food/blessed-child-rice-mix-400g.html")
driver.get("https://melcom.com/categories.html")
# assert "Python" in driver.title
category_elements = ['electronics-appliances', 'furniture', 'food-beverages-toiletries', 'lighting-hardware', 'home-kitchen-essentials', 'mobiles-computers', 'toys-kids-baby-products', 'sports-fitness']
elem = driver.find_elements(by=By.XPATH, value="//div[@class='filter-options-content']//li[@class='item']//a")
for el in elem:
    # if el.text not in ["items", "item"]:
    element_text = ''.join([i for i in el.text if not i.isdigit()])
    element_text = element_text.replace(" ", "-")
    element_text = re.sub(r'[/\W+/g]',' ',element_text)
    category_elements.append(element_text.lower())

category_elements = [item.split("\n")[0] for item in category_elements]
print(category_elements)
# print(element_attribute_value)
assert "No results found." not in driver.page_source
driver.quit()
