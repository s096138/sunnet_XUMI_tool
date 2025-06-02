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
from menu_expanded import menu_expanded_with_sibling
import time

def teacher_score_management(driver):
    try:
        print("測試：辦公室-成績管理-成績管理")
        menu_expanded_with_sibling(driver, "成績管理", "成績管理")
        time.sleep(2)
        if "成績名稱" in driver.page_source:
            print("\033[32m進入成績管理成功\033[0m")
        else:
            print("\033[31m進入成績管理失敗\033[0m") 

        # 新增
        driver.execute_script("processFunc(1);")
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        ) 
        name.click()
        name.clear()
        name.send_keys("自動化測試用")  
        scroe = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fields[yqi][0]']"))
        ) 
        scroe.click()
        scroe.clear()
        scroe.send_keys("50")     
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定建立']"))
        ).click()      
        time.sleep(2)
        if "自動化測試" in driver.page_source:
            print("\033[32m新增成績成功\033[0m")
        else:
            print("\033[31m新增成績失敗\033[0m") 

        # 寄送
        send = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ckbox"))
        ).click() 
        driver.execute_script("processFunc(4);")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn3"))
        ).click()   
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick=\"$('#mailForm').submit();$('#emailModal').modal('hide');\"]"))
        ).click()
        time.sleep(2)      
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "發送完成" in alert_text:
            send = True
            alert.accept()
        else:
            send = False
            alert.accept()

        # 修改
        revise = False
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'自動化測試用')]"))
        ).click() 
        time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "【編輯】功能只編輯第一個選項" in alert_text:
        #     alert.accept()
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        ) 
        name.click()
        name.clear()
        name.send_keys("自動化測試修改用")  
        driver.execute_script("checkFields();")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改成績項目內容完成" in alert_text:
            revise = True
            alert.accept()
        else:
            revise = False
            alert.accept()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source and revise == True:
            print("\033[32m修改成績成功\033[0m") 
        else:
            print("\033[31m修改成績失敗\033[0m") 
        
        # 刪除
        delect = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ckbox"))
        ).click() 
        driver.execute_script("processFunc(3);")
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "你確定要刪除這些選擇的成績項目嗎" in alert_text:
            delect = True
            alert.accept()
        else:
            delect = False
            alert.accept()
        time.sleep(2)
        if "自動化測試修改用" not in driver.page_source and delect == True:
            print("\033[32m刪除成績成功\033[0m") 
        else:
            print("\033[31m刪除成績失敗\033[0m") 

        # 開新分頁
        time.sleep(2)
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "成績單發送" in driver.page_source and send == True:
            print("\033[32m寄送成績成功\033[0m")
        else:
            print("\033[31m寄送成績失敗\033[0m")
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