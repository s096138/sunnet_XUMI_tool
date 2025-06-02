from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException,
    StaleElementReferenceException
)
from menu_expanded import menu_expanded
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import os
from dotenv import load_dotenv

load_dotenv()

def admin_teacher_setting(driver):
    try:
        print("測試：管理者環境-教師管理-教師設定")
        time.sleep(2)
        menu_expanded(driver, "教師管理", "教師設定")
        time.sleep(2)
        if "選擇授課教師" in driver.page_source:
            print("\033[32m進入教師設定成功\033[0m")
        else:
            print("\033[31m進入教師設定失敗\033[0m")        

        # 搜尋
        first_row = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(2)"))
        ).text
        keyword_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword_input.send_keys('自動化測試主課程')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "自動化測試主課程" in  driver.page_source and "2026年的課程" not in driver.page_source:
            print("\033[32m課程關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m課程關鍵字搜尋失敗\033[0m")

        # 空白搜尋
        keyword_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword_input.clear()
        keyword_input.send_keys(' ')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if first_row in  driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")

        # 指派教師
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_teacher']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "keytype")))
        # 選擇搜尋類型為"帳號"
        select_keytype = Select(driver.find_element(By.ID, "keytype"))
        select_keytype.select_by_value("account")
        # 在關鍵字輸入框中輸入"joy03"
        keyword = driver.find_element(By.ID, "keyword")
        keyword.clear()
        keyword.send_keys("joy03")
        search_button = driver.find_element(By.ID, "search_btn")
        search_button.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "sel[]")))
        joy03_checkbox = driver.find_element(By.XPATH, "//input[@name='sel[]' and @value='joy03']")
        joy03_checkbox.click()
        # 點選確定按鈕
        return_button = driver.find_element(By.ID, "return_btn")
        return_button.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])      
        search_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "level"))
        )
        select = Select(search_option)
        select.select_by_value("teacher")
        selected_option = select.first_selected_option
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='sel[]'])[1]")) # 第一個課程
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']")) 
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "指派成功" in alert_text:
            print("\033[32m指派教師成功\033[0m")
        else:
            print("\033[31m指派教師失敗\033[0m")
        alert.accept()
        time.sleep(2)

        # 指派講師
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_teacher']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "keytype")))
        # 選擇搜尋類型為"帳號"
        select_keytype = Select(driver.find_element(By.ID, "keytype"))
        select_keytype.select_by_value("account")
        # 在關鍵字輸入框中輸入"joy03"
        keyword = driver.find_element(By.ID, "keyword")
        keyword.clear()
        keyword.send_keys("joy03")
        search_button = driver.find_element(By.ID, "search_btn")
        search_button.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "sel[]")))
        joy03_checkbox = driver.find_element(By.XPATH, "//input[@name='sel[]' and @value='joy03']")
        joy03_checkbox.click()
        # 點選確定按鈕
        return_button = driver.find_element(By.ID, "return_btn")
        return_button.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])      
        search_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "level"))
        )
        select = Select(search_option)
        select.select_by_value("instructor")
        selected_option = select.first_selected_option
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='sel[]'])[1]")) # 第一個課程
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']")) 
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "指派成功" in alert_text:
            print("\033[32m指派講師成功\033[0m")
        else:
            print("\033[31m指派講師失敗\033[0m")
        alert.accept()
        time.sleep(2)

        # 指派助教
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_teacher']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[-1])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "keytype")))
        # 選擇搜尋類型為"帳號"
        select_keytype = Select(driver.find_element(By.ID, "keytype"))
        select_keytype.select_by_value("account")
        # 在關鍵字輸入框中輸入"joy03"
        keyword = driver.find_element(By.ID, "keyword")
        keyword.clear()
        keyword.send_keys("joy03")
        search_button = driver.find_element(By.ID, "search_btn")
        search_button.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "sel[]")))
        joy03_checkbox = driver.find_element(By.XPATH, "//input[@name='sel[]' and @value='joy03']")
        joy03_checkbox.click()
        # 點選確定按鈕
        return_button = driver.find_element(By.ID, "return_btn")
        return_button.click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[0])      
        search_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "level"))
        )
        select = Select(search_option)
        select.select_by_value("assistant")
        selected_option = select.first_selected_option
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='sel[]'])[1]")) # 第一個課程
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']")) 
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "指派成功" in alert_text:
            print("\033[32m指派助教成功\033[0m")
        else:
            print("\033[31m指派助教失敗\033[0m")
        alert.accept()
        time.sleep(2)

        # 排序
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        td_element1 = driver.find_element(By.XPATH, "//tr//td[2]")
        td_text1 = td_element1.text
        td_element2 = driver.find_element(By.XPATH, "//tr[2]//td[2]")
        td_text2 = td_element2.text
        time.sleep(2)
        if td_text1 < td_text2:
            print("\033[32m課程編號排序成功\033[0m")
        else:
            print("\033[31m課程編號排序失敗\033[0m")

    except TimeoutException as e:
        print(f"等待元素可點擊超時: {e}")
        return
    except NoSuchElementException as e:
        print(f"未找到元素: {e}")
        return
    except ElementClickInterceptedException as e:
        print(f"無法點擊該元素: {e}")
        return
    except StaleElementReferenceException as e:
        print(f"元素已不再可用: {e}")
        return
    except ElementNotInteractableException as e:
        print(f"元素不可互動: {e}")
        return
    except WebDriverException as e:
        print(f"WebDriver 錯誤: {e}")
        return
    except Exception as e:
        print(f"發生未預期的錯誤: {e}")
        return