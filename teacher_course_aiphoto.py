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

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def  teacher_course_aiphoto(driver):
    try:
        print("測試：辦公室-課程管理-課程資訊(AI輔助生圖)")
        menu_expanded(driver, "課程管理", "課程設定")
        time.sleep(2)
        if "課程資訊" in driver.page_source:
            print("\033[32m進入課程資訊成功\033[0m")
        else:
            print("\033[31m進入課程資訊失敗\033[0m")

        scroll_bottom(driver) 
        time.sleep(2)

        # 自選 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'自選')]"))
        ).click()
        
        # AI輔助生圖
        try:
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='AI_image_show']"))
            ).click()
        except (TimeoutException, ElementClickInterceptedException, ElementNotInteractableException):
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@id='dropbtn']"))
            ).click()
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='AI_image_show']"))
            ).click()

        # 描述
        describe = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='describe']"))
        )
        describe.clear() 
        describe.send_keys("rabbit")       
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']"))
        ).click()

        time.sleep(30) # 等待生成

        # 驗證
        if "重新生成" in driver.page_source:
            print("\033[32mAI輔助生圖成功\033[0m")
        else:
            print("\033[31mAI輔助生圖失敗\033[0m")  

        # 確定
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='certain']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "課程代表圖已更換" in alert_text:
            print("\033[32m課程代表圖更換成功\033[0m")
        else:
            print("\033[31m課程代表圖更換失敗\033[0m") 
        alert.accept()   

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@id='dropbtn']"))
        ).click()  
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='create_btn']"))
        ).click()         
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功 " in alert_text:
            print("復原")
        else:
            print("未復原") 
        alert.accept() 

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