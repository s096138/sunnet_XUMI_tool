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
from menu_expanded import menu_expanded
import time

def teacher_rating_management(driver):
    try:
        print("測試：辦公室-同儕作業管理-評量表管理")
        menu_expanded(driver, "同儕作業管理", "評量表管理")
        time.sleep(2)
        if "沒有您要找的評量表" in driver.page_source:
            print("\033[32m進入評量表管理成功\033[0m")
        else:
            print("\033[31m進入評量表管理失敗\033[0m") 

        # 新增
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#addBtn1"))
        ).click()   
        time.sleep(2)
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checklist_name"))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試用")   
        driver.execute_script("tempSave();")  
        time.sleep(2)
        td = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(5)").text
        if td == "暫存":
            print("\033[32m暫存評量表管理成功\033[0m")
        else:
            print("\033[31m暫存評量表管理失敗\033[0m")      

        # 修改
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'修改')]"))
        ).click()  
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checklist_name"))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試修改用")     
        driver.execute_script("save();") 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "評量表點選" in alert_text:
            alert.accept()
        else:
            alert.accept()
        time.sleep(2)  
        td = driver.find_element(By.CSS_SELECTOR, "tbody tr td:nth-child(5)").text
        if td == "啟用":
            print("\033[32m啟用評量表管理成功\033[0m")
        else:
            print("\033[31m啟用評量表管理失敗\033[0m") 
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改評量表管理成功\033[0m")
        else:
            print("\033[31m修改評量表管理失敗\033[0m")   

        # 刪除
        delect = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ckbox"))
        ).click()            
        driver.execute_script("checkData('D')")
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除評量表後" in alert_text:
            alert.accept()
            delect = True
        else:
            alert.accept()
            delect = False
        time.sleep(2)
        if "沒有您要找的評量表" in driver.page_source:
            print("\033[32m刪除評量表管理成功\033[0m")   
        else:
            print("\033[31m刪除評量表管理失敗\033[0m")   


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