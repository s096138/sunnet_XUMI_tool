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
from test_login import test_login
from admin_enter import admin_enter
import time
import os
from dotenv import load_dotenv

load_dotenv()

def admin_teacher_manage(driver):
    try:
        print("測試：管理者環境-教師管理-教師維護")
        menu_expanded(driver, "教師管理", "教師維護")
        time.sleep(2)
        if "授課記錄" in driver.page_source:
            print("\033[32m進入教師維護成功\033[0m")
        else:
            print("\033[31m進入教師維護失敗\033[0m")  

        # # 排序
        # time.sleep(2)
        # account1 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//tbody/tr[1]/td[1]'))
        # )
        # account2 = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//td[normalize-space()="fstu"]'))
        # )
        # text1 = ord(account1.text[0])
        # text2 = ord(account2.text[0])
        # time.sleep(2)
        # if text1 <= text2:
        #     print("\033[32m帳號排序成功\033[0m")
        # else:
        #     print("\033[31m帳號排序失敗\033[0m")  

        # 課程名稱搜尋
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("course")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        keyword.send_keys(course_name) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m課程名稱搜尋成功\033[0m")
        else:
            print("\033[31m課程名稱搜尋失敗\033[0m")

        # email搜尋
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("email")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        keyword.send_keys("yyytest") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32memail搜尋成功\033[0m")
        else:
            print("\033[31memail搜尋失敗\033[0m")
        
        # 姓名搜尋
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("real")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        keyword.send_keys("精靈") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m姓名搜尋成功\033[0m")
        else:
            print("\033[31m姓名搜尋失敗\033[0m")

        # 帳號搜尋
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("account")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        keyword.send_keys("joy09") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m帳號搜尋成功\033[0m")
        else:
            print("\033[31m帳號搜尋失敗\033[0m")

        # 修改
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("real")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        keyword.send_keys("精靈") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".material-icons-outlined.opacity-60.editTeacherRole"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_modify_role']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請勾選要修改的課程名稱" in alert_text:
            print("\033[32m未勾選課程不可修改\033[0m")
        else:
            print("\033[31m未勾選課程可以修改\033[0m")
        alert.accept()
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "level"))
        keytype.select_by_value("128")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td[contains(text(), '2026年的課程')]]//input[@type='checkbox']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn_modify_role"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改變更完成" in alert_text:
            print("\033[32m修改成功\033[0m")
        else:
            print("\033[31m修改失敗\033[0m")
        alert.accept()
        time.sleep(2)

        # 復原
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.material-icons-outlined.opacity-60.editTeacherRole[data-level='128']"))
        ).click()
        time.sleep(2)
        keytype = Select(driver.find_element(By.ID, "level"))
        keytype.select_by_value("512")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td[contains(text(), '2026年的課程')]]//input[@type='checkbox']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "btn_modify_role"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改變更完成" in alert_text:
            print("復原")
        else:
            pass
        alert.accept()
        time.sleep(2)

        # 授課紀錄
        keytype = Select(driver.find_element(By.ID, "keytype"))
        keytype.select_by_value("real")
        keyword = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        )   
        keyword.click()
        keyword.clear()
        keyword.send_keys("精靈") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "search_btn"))
        ).click()  
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".material-icons-outlined.opacity-60.studAction"))
        ).click() 
        time.sleep(2)
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        if course_name in driver.page_source:
            print("\033[32m授課紀錄顯示成功\033[0m")
        else:
            print("\033[31m授課紀錄顯示錯誤\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "back_btn"))
        ).click()     

        # # 變更身分 
        # time.sleep(2)
        # keytype = Select(driver.find_element(By.ID, "keytype"))
        # keytype.select_by_value("account")
        # keyword = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        # )   
        # keyword.click()
        # keyword.clear()
        # keyword.send_keys("joy03") 
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.ID, "search_btn"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='login']"))
        # ).click()        
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='loginsubmit']"))
        # ).click()    
        # time.sleep(5)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        # ).click()
        # time.sleep(2)
        # if "我***" in driver.page_source:
        #     print("\033[32m切換身分成功\033[0m")
        # else:
        #     print("\033[31m切換身分失敗\033[0m")

        # # 復原
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'登出')]"))
        # ).click()
        # time.sleep(2)
        # test_login(driver)
        # time.sleep(2)
        # admin_enter(driver)

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