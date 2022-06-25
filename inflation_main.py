from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re

driver = webdriver.Chrome('/usr/local/bin/chromedriver')
base_url = "https://www.jumia.com.gh"

driver.get(base_url)

elem = driver.find_elements(by=By.XPATH, value='//a[@class="tit"]')

for item in elem:
    print(item.text)



# category_elements = []

# subdivision_results = {}
# for url in category_elements:
#     driver.get(base_url+url+".html")

#     elem = driver.find_elements(by=By.XPATH, value="//div[@class='filter-options-content']//li[@class='item']//a")
#     subdivision_results[url] = []
#     for el in elem:
#         # if el.text not in ["items", "item"]:
#         element_text = ''.join([i for i in el.text if not i.isdigit()])
#         # element_text = element_text.replace(" ", "-")
#         # element_text = re.sub(r'[/\W+/g]',' ',element_text)
#         subdivision_results[url].append(element_text.lower().split("\n")[0])

# # category_elements = [item.split("\n")[0] for item in category_elements]
# print(subdivision_results)
# # print(element_attribute_value)



assert "No results found." not in driver.page_source
driver.quit()



# if __name__ == "__main__":
    
#     url = "https://melcom.com/categories/food-beverages-toiletries/food.html"

#     print("Starting the execution")

#     soup = html_code(url)