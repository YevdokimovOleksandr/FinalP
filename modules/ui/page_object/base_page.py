from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Basepage:
    PATH = r"C:/Users/Admin/Documents/GitHub/FinalP" 
    DRIVER_NAME = "chromedriver.exe"

    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            service = Service(Basepage.PATH + Basepage.DRIVER_NAME)
        )
    
    def close(self):
        self.driver.close()