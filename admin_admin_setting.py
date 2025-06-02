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
from selenium.webdriver.common.alert import Alert
import time

def handle_unexpected_alert(driver):
    try:
        WebDriverWait(driver, 3).until(EC.alert_is_present())
        alert = Alert(driver)
        alert_text = alert.text
        alert.accept()
        print(f"未預期的警示訊息已關閉: {alert_text}")
    except TimeoutException:
        pass  

def admin_admin_setting(driver):
    try:
        print("測試：管理者環境-帳號管理-管理者設定")
        time.sleep(2)
        menu_expanded(driver, "帳號管理", "管理者設定") 
        if "新增管理者" in driver.page_source:
            print("\033[32m進入管理者設定成功\033[0m")
        else:
            print("\033[31m進入管理者設定失敗\033[0m")
        
        # 新增
        add = False
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_add_admin"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_submit"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請填寫帳號" in alert_text:
            print("\033[32m未輸入帳號不可新增\033[0m")
            alert.accept()
        else:
            print("\033[31m未輸入帳號可以新增\033[0m")
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "opnName"))
        )
        name.send_keys('joy03')
        ip = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='opnIP']"))
        )
        ip.clear()
        ip.send_keys('168.96')
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_submit"))
        ).click()      
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增成功" in alert_text:
            add = True
            alert.accept()
        else:
            add = False
            alert.accept()

        # 驗證
        time.sleep(2)
        if "joy03" in driver.page_source and add == True:
            print("\033[32m新增管理者成功\033[0m")
        else:
            print("\033[31m新增管理者失敗\033[0m")   
        time.sleep(2)     
        # 定位到包含 "joy03" 帳號的行
        row = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//tr[td[text()='joy03']]"))
        )
        role = row.find_element(By.XPATH, "./td[contains(text(),'一般管理者')]")
        role_text = role.text
        if role_text == "一般管理者":
            print("\033[32m設定權限成功\033[0m")
        else:
            print("\033[31m設定權限失敗\033[0m")
        time.sleep(2)
        ip_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[text()='joy03']/following-sibling::td[text()='168.96']"))
        )
        actual_ip = ip_field.text
        if actual_ip == "168.96":
            print("\033[32m設定IP限制成功\033[0m")
        else:
            print("\033[31m設定IP限制失敗\033[0m")

        # 修改
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td[2]='joy03']//button[@name='btnModify']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "opnPermit1"))
        ).click()
        ip = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='opnIP']"))
        )
        ip.clear()
        ip.send_keys("168.96.4.1")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_submit"))
        ).click()      
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "更新成功" in alert_text:
            alert.accept()

        # 驗證  
        time.sleep(2)     
        # 定位到包含 "joy03" 帳號的行
        row = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//tr[td[text()='joy03']]"))
        )
        role = row.find_element(By.XPATH, "./td[contains(text(),'超級管理者')]")
        role_text = role.text
        if role_text == "超級管理者":
            print("\033[32m修改權限成功\033[0m")
        else:
            print("\033[31m修改權限失敗\033[0m")
        time.sleep(2)
        ip_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//td[text()='joy03']/following-sibling::td[text()='168.96.4.1']"))
        )
        actual_ip = ip_field.text
        if actual_ip == "168.96.4.1":
            print("\033[32m修改IP限制成功\033[0m")
        else:
            print("\033[31m修改IP限制失敗\033[0m")

        # 刪除
        delete = False
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @value='joy03']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_delete']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請確定是否要刪除這些的管理者？" in alert_text:
            alert.accept()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "成功刪除" in alert_text:
                delete = True
                alert.accept()
        else:
            delete = False
        time.sleep(2)
        if "joy03" not in driver.page_source and delete == True:
            print("\033[32m刪除管理者成功\033[0m")
        else:
            print("\033[31m刪除管理者失敗\033[0m")           

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