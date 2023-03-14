from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    PATH = "C:/Users/IBazilevych/Desktop/Become_QA_Auto/"
    DRIVER_NAME = "chromedriver.exe"

    driver = webdriver.Chrome(
            service=Service(PATH + DRIVER_NAME)
            )
    
    @classmethod
    def wait_time(cls , time):
        wait = WebDriverWait(cls, time)
        wait.until(EC.element_to_be_clickable)
    
    @classmethod
    def get(cls , url):
        cls.driver.get(url)
    
    @classmethod
    def find_element(cls , type , name):
        return cls.driver.find_element(type,name)
    
    @classmethod
    def close(cls):
        cls.driver.close()
    
    @classmethod
    def maximize_window(cls):
        cls.driver.maximize_window()

    @classmethod
    def switch_to(cls):
        cls.driver.switch_to.window

    