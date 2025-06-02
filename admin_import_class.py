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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
import time
import os

def admin_import_class(driver):
    try:
        print("測試：管理者環境-群組管理-匯入群組成員")  
        menu_expanded(driver, "群組管理", "匯入群組成員")
        time.sleep(2)
        if "點擊這裡上傳檔案" in driver.page_source:
            print("\033[32m進入匯入群組成員成功\033[0m")
        else:
            print("\033[31m進入匯入群組成員失敗\033[0m")

        # 匯入
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "import_btn"))
        ).click()
        time.sleep(2)
        if "請選擇上傳檔案" in driver.page_source:
            print("\033[32m未選檔案不可上傳\033[0m")
        else:
            print("\033[31m未選檔案可以上傳\033[0m")            
        upload_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='xlsxfile']"))
        )
        file_path = "c:\\Users\\SGQA2\\Desktop\\Auto\\import_class_new.xlsx"
        if os.path.exists(file_path):
            upload_button.send_keys(file_path)
            print(f"\033[32m帳號檔案已上傳：{file_path}\033[0m")
        else:
            print(f"\033[31m帳號檔案不存在：{file_path}\033[0m")
        time.sleep(2)
        classid = Select(driver.find_element(By.ID, "class_id"))
        classid.select_by_visible_text("圖書館系")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "import_btn"))
        ).click()
        error_messages = ["帳號已存在於此群組", "群組代碼錯誤", "群組代碼未指定"]
        error_found = False
        for error_message in error_messages:
            try:
                found_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//div[contains(text(), '{error_message}')]"))
                ).text
                print(f"\033[31m匯入群組成員失敗：{found_message}\033[0m")
                error_found = True
                break
            except:
                continue
        if not error_found:
            print("\033[32m匯入群組成員成功\033[0m")
        time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-wm-purple-outline' and text()='關閉']"))
        # ).click()
        close_button = driver.find_element(By.XPATH, "//button[@class='btn btn-wm-purple-outline' and text()='關閉']")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/academic/class/people_manager.php']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'圖書館系')]"))
        ).click()
        time.sleep(2)
        if "yqi" in driver.page_source:
            print("\033[32m群組查看人員成功\033[0m")
        else:
            print("\033[32m群組查看人員失敗\033[0m")

        # 移出
        remove = False
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

 