import pytest
from selenium.webdriver.common.by import By
from base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):

    @classmethod
    def click_search_button(cls):
         search_button = cls.find_element(By.XPATH, "//span[(text()='Search')]")
         search_button.click()
         
    @classmethod
    def add_destination(cls , destination):
        city_button = cls.find_element(By.NAME, "ss")
        city_button.click()
        city_button.send_keys(destination)

    @classmethod
    def change_language_window(cls):
        language_icon = cls.find_element(By.XPATH, "//button[@data-testid ='header-language-picker-trigger']")
        language_icon.click()
        
    @classmethod
    def select_english_language(cls):
        language_selection = WebDriverWait(cls, 5).until(EC.element_to_be_clickable((By.XPATH, "//span[(text()='English (UK)')]")))
        language_selection = cls.find_element(By.XPATH, "//span[(text()='English (UK)')]")
        language_selection.click()

    
        
