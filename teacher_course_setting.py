from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from selenium_driver import initialize_driver
import time
import os

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

def teacher_course_setting(driver):
    try:
        print("測試：辦公室-課程管理-課程設定")
        menu_expanded(driver, "課程管理", "課程設定")
        time.sleep(2)
        if "課程資訊" in driver.page_source:
            print("\033[32m進入課程設定成功\033[0m")
        else:
            print("\033[31m進入課程設定失敗\033[0m")

        # 課程資訊
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        name.send_keys("123321")
        scroll_bottom(driver)
        time.sleep(2)
        driver.execute_script("save_step(1)")
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            alert.accept()
            time.sleep(2)
        scroll_top(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程設定')]"))
        ).click()
        select_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'selcourse'))
        )   
        select = Select(select_element)  
        option_found = False
        for option in select.options:
            if "123321" in option.text:
                option_found = True
                break  
        if option_found:
            print("\033[32m修改課程名稱有正確顯示\033[0m")
        else:
            print("\033[31m修改課程名稱未正確顯示\033[0m")   
        time.sleep(2) 
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        name.send_keys(course_name)   
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.clear()
        point.send_keys("-1")
        scroll_bottom(driver)
        time.sleep(2)
        driver.execute_script("save_step(1)")
        if "必需是阿拉伯數字型態" in driver.page_source:
            print("\033[32m學分數有驗證是否是正整數\033[0m")
        else:
            print("\033[31m學分數沒驗證是否是正整數\033[0m") 
        point.click()
        point.clear()
        point.send_keys("2")   
        score = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fair_grade'))
        )
        score.click()
        score.clear()
        score.send_keys("-1")
        time.sleep(2)
        driver.execute_script("save_step(1)")
        if "必需是阿拉伯數字型態" in driver.page_source:
            print("\033[32m及格成績有驗證是否是正整數\033[0m")
        else:
            print("\033[31m及格成績沒驗證是否是正整數\033[0m") 
        score.click()
        score.clear()
        score.send_keys("60")    
        driver.execute_script("save_step(1)") 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            print("\033[32m修改課程成功\033[0m")
            alert.accept()
            time.sleep(2)

        # 回到上方
        scroll_top(driver)

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