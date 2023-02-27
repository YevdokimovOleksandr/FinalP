import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome(
        service=Service(r"C:/Users/Admin/Documents/GitHub/FinalP"+ "chromedriver.exe")
        )

    driver.get("https://github.com/login")

    login_elem = driver.find_element(By.ID, "login_field")

    login_elem.send_keys("fdkgfdgk@google.com")

    passwod_elem = driver.find_element(By.ID, "password")

    passwod_elem.send_keys("hgfjfg")

    btn_elem = driver.find_element(By.NAME, "commit")

    btn_elem.click()

    assert driver.title == "Sign in to GitHub · GitHub"
    

    driver.close()
    