from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from selenium_driver import initialize_driver
import random
import time

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def test_news(driver):
    try:
        print("測試：首頁-最新消息")
        # 最新消息
        time.sleep(2)
        if "更多消息" in driver.page_source and "最新消息" in driver.page_source:
            print('\033[32m查看最新消息成功\033[0m')
        else:
            print("\033[31m查看最新消息失敗\033[0m")   

        # 更多消息
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'最新消息')]"))   
        ).click()
        time.sleep(2)
        if "消息快報" in driver.page_source and "最新消息" in driver.page_source:
            print('\033[32m進入更多消息成功\033[0m')
        else:
            print("\033[31m進入更多消息失敗\033[0m")  

        # 關鍵字搜尋
        kw = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        kw.click()
        kw.send_keys("自動化測試用最新消息1")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "共有 1 筆" in driver.page_source:
            print('\033[32m關鍵字搜尋成功\033[0m')
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m") 
        
        # 空白搜尋
        kw.clear()
        kw.send_keys(" ")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用最新消息1" in driver.page_source and "自動化測試用最新消息2" in driver.page_source:
            print('\033[32m空白搜尋成功\033[0m')
        else:
            print("\033[31m空白搜尋失敗\033[0m") 

        # 點擊文章 
        kw = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        kw.click()
        kw.send_keys("1")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)  
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='news__content']"))
        ).click()
        time.sleep(2)
        if "自動化測試用最新消息1" in driver.page_source and "回列表" in driver.page_source:
            print('\033[32m點擊文章成功\033[0m')
        else:
            print("\033[31m點擊文章失敗\033[0m") 

        # 切換文章
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//h4[contains(text(),'自動化測試用最新消息2')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用最新消息2" in driver.page_source and "回列表" in driver.page_source:
            print('\033[32m切換文章成功\033[0m')
        else:
            print("\033[31m切換文章失敗\033[0m") 
        
        # 回列表
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator news-detail-button mat-button mat-button-base']"))
        ).click()
        time.sleep(2)
        if "自動化測試用最新消息1" in driver.page_source and "自動化測試用最新消息2" in driver.page_source:
            print('\033[32m回列表成功\033[0m')
        else:
            print("\033[31m回列表失敗\033[0m") 

        # # 切換頁籤
        # scroll_bottom(driver)
        # WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='下一頁']"))
        # ).click()
        # time.sleep(2)
        # if "人才策略與管理" in driver.page_source:
        #     print('\033[32m切換頁籤成功\033[0m')
        # else:
        #     print("\033[31m切換頁籤失敗\033[0m") 

        # # 每頁筆數
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//mat-select[@aria-label='每頁筆數']"))
        # ).click()
        # page = [
        #     "//span[@class='mat-option-text'][normalize-space()='5']",
        #     #"//span[@class='mat-option-text'][normalize-space()='15']",
        #     #"//span[@class='mat-option-text'][normalize-space()='20']"
        # ]
        # selected_page = random.choice(page)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, selected_page))
        # ).click()
        # time.sleep(5)
        # page_source = driver.page_source
        # text_to_find = "消息快報"
        # items = page_source.count(text_to_find)
        # if selected_page == "//span[@class='mat-option-text'][normalize-space()='5']" and items == 5:
        #     print('\033[32m每筆頁數切換成功\033[0m')
        # elif selected_page == "//span[@class='mat-option-text'][normalize-space()='15']" and items == 15:
        #     print('\033[32m每筆頁數切換成功\033[0m')
        # elif selected_page == "//span[@class='mat-option-text'][normalize-space()='20']" and items == 20:
        #     print('\033[32m每筆頁數切換成功\033[0m')
        # else:
        #     print("\033[31m每筆頁數切換失敗\033[0m") 
        
        # 回首頁
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        print('回首頁')

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