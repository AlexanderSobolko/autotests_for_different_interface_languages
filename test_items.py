import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_for_different_interface_languages(browser):
    browser.get(link)
    time.sleep(30)
    button_add = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                  "button.btn.btn-lg.btn-primary.btn-add-to-basket")))
    assert button_add, "add button not found"
