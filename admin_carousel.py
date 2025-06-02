from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait   
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
import time
import os
from dotenv import load_dotenv

# 取得當前時間
nowdatetime = datetime.now().strftime("%Y-%m-%d")

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height 

def admin_carousel(driver):
    try:
        print("測試：管理者環境-公告管理-首頁活動輪播")
        menu_expanded(driver, "公告管理", "首頁活動輪播")
        time.sleep(2)
        if "廣告名稱" in driver.page_source:
            print("\033[32m進入首頁活動輪播成功\033[0m")
        else:
            print("\033[31m進入首頁活動輪播失敗\033[0m") 

        # 新增
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="name"]'))
        )
        name.click()
        name.send_keys("自動化測試用")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_date'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_date'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        url = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="url"]'))
        )
        url.click()
        url.send_keys("https://www.cwa.gov.tw/V8/C/")
        time.sleep(2)
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'upload'))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)

        # 確定
        driver.execute_script("checkData()")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增首頁活動輪播成功\033[0m")
        else:
            print("\033[31m新增首頁活動輪播失敗\033[0m") 
            
        # 查看
        scroll_bottom(driver)
        row = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, f"//td[text()='{nowdatetime}']/following-sibling::td/a/span[contains(text(), 'link')]"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable(row)
        ).click()
        time.sleep(2)
        all_handles = driver.window_handles
        main_window = driver.current_window_handle
        new_window = [window for window in all_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        expected_url = "https://www.cwa.gov.tw/V8/C/"  # 你的預期網址
        current_url = driver.current_url
        time.sleep(2)
        if current_url == expected_url:
            print("\033[32m點選網站連結跳轉成功\033[0m")
        else:
            print(f"\033[31m點選網站連結跳轉失敗，當前網址是: {current_url}\033[0m")
        driver.close()
        driver.switch_to.window(main_window)

        # 回首頁
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        driver.get(base_url)

        # 確認首頁輪播狀態
        time.sleep(2)
        initial_src = driver.find_element(By.CSS_SELECTOR, "div.swiper-slide.swiper-slide-active img.swiper__image").get_attribute("src")
        iterations=10  #檢查十次
        check_interval=2  #每兩秒檢查一次
        for i in range(iterations):
            time.sleep(check_interval)
            current_src = driver.find_element(By.CSS_SELECTOR, "div.swiper-slide.swiper-slide-active img.swiper__image").get_attribute("src")
            print(f"Iteration {i}: {current_src}")
            time.sleep(2)
            if initial_src != current_src:
                image_changed = True 
                break
        if image_changed:
            print("\033[32m輪播圖片成功\033[0m")
        else:
            print("\033[31m輪播圖片失敗\033[0m")
        
        # 回首頁活動輪播
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'管理者環境')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sysbarHeader"]/ul/li[3]/a'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sldebar-nav"]/li[2]/div'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu2"]/li[1]/a'))
        ).click()
        time.sleep(2)

        # 刪除
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td[contains(text(), '自動化測試用')]]//input[@type='checkbox']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_del']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "您確定要刪除嗎?"
        alert.accept()
        time.sleep(2)
        if "自動化測試用" not in driver.page_source:
            print("\033[32m刪除首頁活動輪播成功\033[0m")
        else:
            print("\033[31m刪除首頁活動輪播失敗\033[0m")

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