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
    WebDriverException, 
    NoAlertPresentException
)
from menu_expanded import menu_expanded
from selenium_driver import initialize_driver
import time

def handle_alert(driver):
        # 預防上次未儲存
        try:
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "您有上一次未完成的暫存資料，要使用它嗎？" in alert_text:
                alert.dismiss()
            else:
                alert.dismiss()
        except NoAlertPresentException:
            pass

def handle_random_alert(driver):
    # 隨機分組使用
    success = False
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.alert_is_present())
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "系統可能不會儲存你所做的變更" in alert_text:
                alert.accept()
            elif "隨機分組完成" in alert_text:
                print("\033[32m隨機分組成功\033[0m")
                success = True
                alert.accept()
            elif "您有上一次未完成的暫存資料，要使用它嗎？" in alert_text:
                alert.dismiss()  
            else:
                alert.dismiss() 
                time.sleep(2)

        except TimeoutException:
            break
        except NoAlertPresentException:
            break
    return success

def teacher_student_group(driver):
    try:
        print("測試：辦公室-人員管理-學員分組")
        menu_expanded(driver, "人員管理", "學員分組")
        handle_alert(driver)
        time.sleep(2)
        handle_alert(driver)
        if "學員分組管理" in driver.page_source:
            print("\033[32m進入學員分組成功\033[0m")
        else:
            print("\033[31m進入學員分組失敗\033[0m")

        # 新增群組
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='新增群組']"))
        ).click()  
        time.sleep(2)                   
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@type="checkbox" and @value="yyytest	yyytest "]'))
        )
        driver.execute_script("arguments[0].click();", checkbox) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'新組別')]"))
        ).click() 

        # 重新命名
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='javascript:;']//img"))
        ).click()      
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#group_name_big5"))
        )  
        name.click()
        name.clear()
        name.send_keys("自動化測試用") 
        captain = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='captain']"))
        )   
        captain.click()
        time.sleep(2)
        select = Select(captain)
        select.select_by_value("yyytest")  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@onclick='setPropertyComplete();']"))
        ).click()  
        font = driver.find_element(By.CLASS_NAME, "font02").text
        if "yyytest" in font:
            print("\033[32m學員分組到新組別成功\033[0m")
        else:
            print("\033[31m學員分組到新組別失敗\033[0m")   
             
        # 完成分組
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='saveButton']"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "資料儲存完畢" in alert_text:
            print("\033[32m儲存學員分組成功\033[0m")
            alert.accept()
        else:
            print("\033[31m儲存學員分組失敗\033[0m") 
        
        # 重新分組
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='重新分組']"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "執行重新分組，會將所有組內的人員歸入『尚未分組』的團體中。確定要真的重新分組嗎？"
        alert.accept() 
        try:
            font = driver.find_element(By.CLASS_NAME, "font02")
            if font:
                print("\033[31m重新分組失敗\033[0m")
            else:
                print("\033[32m重新分組成功\033[0m")
        except NoSuchElementException:
            print("\033[32m重新分組成功\033[0m")       

        # 隨機分組
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='隨機分組']"))
        ).click() 
        time.sleep(2)
        num = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='group_num']"))
        )
        num.click()
        num.send_keys("1")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']"))
        ).click() 
        time.sleep(2)
        success = handle_random_alert(driver)      
        if not success:
            print("\033[31m隨機分組失敗\033[0m") 

        # 移除分組 
        box1 = driver.find_element(By.XPATH, "//td[@class='cssTrOdd']//input[@value='1']")
        driver.execute_script("arguments[0].click();", box1) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='移除群組']"))
        ).click()  
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "移除群組的話，會將群組中的人員歸類到「尚未分組」的群體中，並將該群組的討論區與討論室刪除。確定要移除群組嗎？" in alert_text:
            print("\033[32m移除群組成功\033[0m")
            alert.accept()
        else:
            print("\033[31m移除群組失敗\033[0m") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='saveButton']"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "資料儲存完畢" in alert_text:
            alert.accept()
        else:
            alert.accept()

        # 分組次管理-新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        ).click()    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar1'] input[value='新增']"))
        ).click()   
        teamname1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "team_name_big5"))
        )     
        teamname1.click()
        teamname1.clear()
        teamname1.send_keys("自動化測試用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/table[1]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/input[1]"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增分組次完成" in alert_text:
            print("\033[32m新增分組次成功\033[0m")
            alert.accept()
        else:
            print("\033[31m新增分組次失敗\033[0m") 

        # 分組次管理-修改
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[3]/td[3]/input[1]"))
        ).click() 
        teamname2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(11) > table:nth-child(5) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(2) > input:nth-child(1)"))
        )     
        teamname2.click()
        teamname2.clear()
        teamname2.send_keys("自動化測試修改用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/table[2]/tbody[1]/tr[2]/td[1]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/input[2]"))
        ).click() 
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改分組次成功\033[0m")
        else:
            print("\033[31m修改分組次失敗\033[0m") 

        # 分組次管理-刪除
        time.sleep(2)
        tlist = driver.find_element(By.XPATH, "//body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/form[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[3]/td[1]/input[1]") 
        driver.execute_script("arguments[0].click();", tlist) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar1'] input[value='刪除']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除" in alert_text:
            print("\033[32m刪除分組次成功\033[0m")
            alert.accept()
        else:
            print("\033[31m刪除分組次失敗\033[0m")  

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