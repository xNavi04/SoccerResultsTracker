import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from data import tabels, link

class srapWeb:
    def __init__(self):
        self.CLUBS = []
        self.x = ""
        self.y = ""

    def groupUEFA(self):
        sm = self.driver.find_element(By.XPATH, value=tabels[self.y])
        span_elements = sm.find_elements(By.CLASS_NAME, value="hsKSJe")
        for i in span_elements:
            self.CLUBS.append(i.text)

    def groupEKSTRAKLASA(self):
        sm = self.driver.find_elements(By.CLASS_NAME, value="hsKSJe")
        for i in sm:
            self.CLUBS.append(i.text)


    def input(self):
        while True:
            x = input("Input soccer league, which you are interested! (UEFA, EKSTRAKLASA) ").upper()
            if x == "UEFA" or x == "EKSTRAKLASA":
                self.x = x
                if x == "UEFA":
                    while True:
                        y = input("Which group you are interested! (A-H) ").upper()
                        if y == "A" or y == "B" or y == "C" or y == "D" or y == "E" or y == "F" or y == "G" or y == "H":
                            self.y = y
                            break
                break

    def choose_correct_link(self):
        if self.x == "UEFA":
            webdriver_option = webdriver.ChromeOptions()
            webdriver_option.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=webdriver_option)
            self.driver.get(link["UEFA"])
            button = self.driver.find_element(By.XPATH, value='//*[@id="L2AGLb"]/div')
            button.click()
            time.sleep(3)
            self.groupUEFA()
        elif self.x == "EKSTRAKLASA":
            webdriver_option = webdriver.ChromeOptions()
            webdriver_option.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(options=webdriver_option)
            self.driver.get(link["EKSTRAKLASA"])
            button = self.driver.find_element(By.XPATH, value='//*[@id="L2AGLb"]/div')
            button.click()
            time.sleep(3)
            self.groupEKSTRAKLASA()


