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
import time

# 滾動到底部
def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def teacher_adddelete_student(driver):
    try:
        print("測試：辦公室-人員管理-增刪學員")
        menu_expanded(driver, "人員管理", "增刪學員")
        time.sleep(2)
        if "批次帳號管理" in driver.page_source:
            print("\033[32m進入增刪學員成功\033[0m")
        else:
            print("\033[31m進入增刪學員失敗\033[0m")

        # 清除
        time.sleep(2)
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest") 
        scroll_bottom(driver)  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='清除輸入']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='新增正式生']"))
        ).click()   
        time.sleep(2)             
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請輸入帳號" in alert_text:
            print("\033[32m清除輸入成功\033[0m")
            alert.accept()
        else:
            print("\033[31m清除輸入失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 新增正式生
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest")  
        scroll_bottom(driver) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='新增正式生']"))
        ).click()   

        # 驗證
        time.sleep(2)
        add1 = False
        if "賦予正式生身分" in driver.page_source and "確定" in driver.page_source:
            add1 = True
        else:
            add1 = False
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()  
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2) 
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("正式生")
        time.sleep(2)
        if "yyytest" in driver.page_source and add1 == True:
            print("\033[32m新增正式生成功\033[0m")
        else:
            print("\033[31m新增正式生失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        ).click()

        # 正式生變旁聽生
        time.sleep(2) 
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest") 
        scroll_bottom(driver)  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='正式生變旁聽生']"))
        ).click() 

        # 驗證
        time.sleep(2)
        add2 = False
        if "正式生變旁聽生" in driver.page_source and "確定" in driver.page_source:
            add2 = True
        else:
            add2 = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()    
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2)
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("旁聽生")
        time.sleep(2) 
        if "yyytest" in driver.page_source and add2 == True:
            print("\033[32m正式生變旁聽生成功\033[0m")
        else:
            print("\033[31m正式生變旁聽生失敗\033[0m") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        ).click()

        # 旁聽生變正式生
        time.sleep(2) 
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest")   
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='旁聽生變正式生']"))
        ).click()

        # 驗證
        time.sleep(2)
        add3 = False
        if "旁聽生變正式生" in driver.page_source and "確定" in driver.page_source:
            add3 = True
        else:
            add3 = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()  
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2)
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("正式生")
        time.sleep(2) 
        if "yyytest" in driver.page_source and add3 == True:
            print("\033[32m旁聽生變正式生成功\033[0m")
        else:
            print("\033[31m旁聽生變正式生失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        ).click()

        # 刪除
        time.sleep(2) 
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest")   
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='移除']"))
        ).click()

        # 驗證
        time.sleep(2)
        add4 = False             
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除嗎" in alert_text:
            alert.accept()
            if "移除" in driver.page_source and "確定" in driver.page_source:
                add4 = True
        else:
            add4 = False
            time.sleep(5)
            alert.accept()        
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()  
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2)
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("全部")
        time.sleep(2) 
        if "yyytest" not in driver.page_source and add4 == True:
            print("\033[32m移除學員成功\033[0m")
        else:
            print("\033[31m移除學員失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        ).click()

        # 新增旁聽生
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest")  
        scroll_bottom(driver) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='新增旁聽生']"))
        ).click()   

        # 驗證
        time.sleep(2)
        add5 = False
        if "賦予旁聽生身分" in driver.page_source and "確定" in driver.page_source:
            add5 = True
        else:
            add5 = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()  
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'到課統計')]"))
        ).click()
        time.sleep(2) 
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("旁聽生")
        time.sleep(2)
        if "yyytest" in driver.page_source and add5 == True:
            print("\033[32m新增旁聽生成功\033[0m")
        else:
            print("\033[31m新增旁聽生失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'增刪學員')]"))
        ).click()

        # 刪除
        time.sleep(2) 
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='userlist']"))
        )
        userlist.click()
        userlist.send_keys("yyytest")   
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[id='toolbar2'] input[value='移除']"))
        ).click()

        # 驗證
        time.sleep(2)            
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除嗎" in alert_text:
            alert.accept()
        else:
            time.sleep(5)
            alert.accept()    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定']"))
        ).click()  
        
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