import pytest
from main_pageobject import MainPage



@pytest.mark.ui
def test_search_appartment():
    MainPage.get("https://www.booking.com/")

    MainPage.maximize_window()

    MainPage.change_language_window()

    MainPage.select_english_language()

    MainPage.add_destination("Kyiv")
    
    MainPage.click_search_button()
    
    MainPage.close()