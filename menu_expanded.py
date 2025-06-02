from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

def menu_expanded(driver, menu_name, sub_menu_name):
    """選擇子功能並自動展開母選單"""
    driver.refresh()
    time.sleep(2)
    menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'nav-link sldebar-toggle d-flex') and .//span[contains(text(),'{menu_name}')]]"))
    )
    time.sleep(2)
    arrow = menu.find_element(By.XPATH, './/span[contains(@class, "material-icons ms-auto arrow")]')
    time.sleep(2)
    if arrow.get_attribute('innerHTML') == 'keyboard_arrow_down':
        menu.click()
        time.sleep(2)
    sub_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//span[contains(text(),'{sub_menu_name}')]"))
    )
    sub_menu.click()

def menu_expanded_with_sibling(driver, menu_name, sub_menu_name):
    """選擇子功能並自動展開母選單,並且需要有特定的兄弟節點"""
    driver.refresh()
    menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'nav-link sldebar-toggle d-flex') and .//span[contains(text(),'{menu_name}')]]"))
    )
    time.sleep(2)
    arrow = menu.find_element(By.XPATH, './/span[contains(@class, "material-icons ms-auto arrow")]')
    time.sleep(2)
    if arrow.get_attribute('innerHTML') == 'keyboard_arrow_down':
        menu.click()
        time.sleep(2)
    sub_menu = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, f"//li[contains(@class, 'nav-item') and .//span[contains(text(),'{menu_name}')]]//li//span[contains(text(),'{sub_menu_name}')]"))
    )
    sub_menu.click()