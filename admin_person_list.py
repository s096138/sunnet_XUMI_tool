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
from menu_expanded import menu_expanded_with_sibling
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv

def admin_person_list(driver):
    try:
        print("測試：管理者環境-群組管理-人員管理")  
        menu_expanded_with_sibling(driver, "群組管理", "人員管理")
        time.sleep(2)
        if "隸屬群組" in driver.page_source:
            print("\033[32m進入人員管理成功\033[0m")
        else:
            print("\033[31m進入人員管理失敗\033[0m")

        # 帳號搜尋
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "keytype"))
        )
        select = Select(search)
        select.select_by_value("account")
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys("joy")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m帳號搜尋成功\033[0m")
        else:
            print("\033[31m帳號搜尋失敗\033[0m")

        # email搜尋
        time.sleep(2)
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "keytype"))
        )
        select = Select(search)
        select.select_by_value("email")
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys("yyytest")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32memail搜尋成功\033[0m")
        else:
            print("\033[31memail搜尋失敗\033[0m")

        # 姓名搜尋
        time.sleep(2)
        search = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "keytype"))
        )
        select = Select(search)
        select.select_by_value("real")
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "keyword"))
        )
        keyword.clear()
        keyword.send_keys("小精靈")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m姓名搜尋成功\033[0m")
        else:
            print("\033[31m姓名搜尋失敗\033[0m")

        # 成績列表
        load_dotenv()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tbody tr:nth-child(1) td:nth-child(9) span:nth-child(1)"))
        ).click()
        time.sleep(2)
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        if course_name in driver.page_source:
            print("\033[32m成績列表檢視成功\033[0m")
        else:
            print("\033[31m成績列表檢視失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='grade-modal']//button[@id='btn_submit']"))
        ).click()

        # 加入
        add = False
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_add"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='groups-modal']//label[contains(text(),'圖書館系')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_submit"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "人員加入群組成功" in alert_text:
            add = True
            alert.accept()
        else:
            add = False
            print("\033[31m人員加入群組失敗\033[0m")
        time.sleep(2)
        if "圖書館系" in driver.page_source and add == True:
            print("\033[32m人員加入群組成功\033[0m")
        else:
            print("\033[31m人員加入群組失敗\033[0m")

        # 檢視群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'圖書館系')]"))
        ).click()
        time.sleep(2)
        if "joy09" in driver.page_source:
            print("\033[32m群組顯示人員成功\033[0m")
        else:
            print("\033[31m群組顯示人員失敗\033[0m")

        # 匯出人員
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_account_mail']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='groups-choose-modal']//label[contains(text(), '圖書館系')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_choose_submit']"))
        ).click() 
        time.sleep(2)
        email = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='send_email']"))
        )  
        email.clear()
        email.send_keys(os.getenv("TEST_EMAIL"))
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_choose_confirm']"))
        ).click()        
        time.sleep(2)
        if "已發送" in driver.page_source:
            print("\033[32m匯出人員成功\033[0m")
        else:
            print("\033[31m匯出人員失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-wm-purple-outline'][contains(text(),'確定')]"))
        ).click() 
        
        # 移出
        remove = False
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'圖書館系')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_remove"))
        ).click()  
        time.sleep(2)      
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "從群組中移除只會將課程從群組中移除" in alert_text:
            alert.accept()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "人員移出群組成功" in alert_text:
                remove = True
                alert.accept()
            else:
                remove = False
        time.sleep(2)
        if "沒有任何資料" in driver.page_source:
            print("\033[32m人員移出群組成功\033[0m")
        else:
            print("\033[31m人員移出群組失敗\033[0m")

        # 另開視窗
        time.sleep(5) #等待發信
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(5)
        if "匯出人員資料" in driver.page_source:
            print("\033[32m發送匯出人員信件成功\033[0m")
        else:
            print("\033[31m發送匯出人員信件失敗\033[0m")
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(2)  

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