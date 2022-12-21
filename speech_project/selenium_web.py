import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(options=options)

    def get_info(self, query):
        self.query = query

        self.driver.get(url="https://www.wikipedia.org")
        search = self.driver.find_element(By.ID, 'searchInput')
        search.clear()
        search.send_keys(query)
        search.send_keys(Keys.RETURN)
        time.sleep(1)
        result_info = self.driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/p[2]').text
        result_info = ".".join(result_info.split(".")[:3])
        return result_info


# print(infow().get_info("moon"))
