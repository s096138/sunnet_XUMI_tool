from turtle import title
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
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
from selenium import webdriver
import time
import os

download_directory = "c:\\Users\\SGQA2\\Downloads"
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,  # 允許不安全下載

}
options.add_experimental_option("prefs", prefs)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')

def get_downloaded_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def teacher_learning_path(driver):
    try:
        print("測試：辦公室-課程管理-學習路徑管理")
        menu_expanded(driver, "課程管理", "學習路徑管理")
        time.sleep(2)
        if "新增節點" in driver.page_source:
            print("\033[32m進入學習路徑管理成功\033[0m")
        else:
            print("\033[31m進入學習路徑管理失敗\033[0m")

        # 新增節點
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_add']"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@id='title[Big5]'])[1]"))
        )       
        title.clear()   
        title.send_keys("自動化測試用")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'引用教材')]"))
        ).click()
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'上傳檔案')])[1]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='upload_file']"))
        ).send_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳檔案']"))
        ).click()
        driver.switch_to.window(windows[0])
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='setting_btn']"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增節點成功\033[0m")
        else:
            print("\033[31m新增節點失敗\033[0m")

        # 修改節點
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='自動化測試用']"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@id='title[Big5]'])[1]"))
        )       
        title.clear()   
        title.send_keys("自動化測試修改用")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='setting_btn']"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改節點成功\033[0m")
        else:
            print("\033[31m修改節點失敗\033[0m")

        # 顯示或隱藏
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='自動化測試修改用']/preceding-sibling::i[@class='jstree-icon jstree-checkbox']"))
        ).click()
        is_checked = "jstree-checked" in driver.find_element(By.XPATH, "//span[text()='自動化測試修改用']/ancestor::a").get_attribute("class")
        # if is_checked:
        #     print("\033[32mCheckbox勾選成功\033[0m")
        # else:
        #     print("\033[31mCheckbox勾選失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_action']"))
        ).click()         
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_batch_visible']"))
        ).click()        
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='jstree-text' and text()='自動化測試修改用']"))
        )
        computed_style = driver.execute_script(
            "return window.getComputedStyle(arguments[0]).getPropertyValue('text-decoration-line');", 
            element
        )
        if computed_style == "line-through":
            print("\033[32m隱藏節點成功\033[0m")
        else:
            print("\033[31m隱藏節點失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_action']"))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_batch_visible']"))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='自動化測試修改用']/preceding-sibling::i[@class='jstree-icon jstree-checkbox']"))
        ).click()  

        # 複製節點
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試修改用')]/ancestor::a/div/span[2]"))
        ).click()
        time.sleep(2)
        elements = driver.find_elements(By.XPATH, "//span[contains(text(),'自動化測試修改用')]")
        if len(elements) == 2:
            print("\033[32m複製節點成功\033[0m")
        else:
            print("\033[31m複製節點失敗\033[0m")

        # 子節點
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試修改用')]/ancestor::a/div/span[4]"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@id='title[Big5]'])[1]"))
        )       
        title.clear()   
        title.send_keys("自動化測試子節點用")    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='setting_btn']"))
        ).click()
        time.sleep(2)
        if "自動化測試子節點用" in driver.page_source:
            print("\033[32m新增子節點成功\033[0m")
        else:
            print("\033[31m新增子節點失敗\033[0m")

        # 刪除節點
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='自動化測試子節點用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試子節點用')]/ancestor::a/div/span[3]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎" in alert_text:
            alert.accept()
        time.sleep(2)
        if "自動化測試子節點用" not in driver.page_source:
            print("\033[32m刪除子節點成功\033[0m")
        else:
            print("\033[31m刪除子節點失敗\033[0m")
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試修改用')]/ancestor::a/div/span[3]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎" in alert_text:
            alert.accept()
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試修改用')]/ancestor::a/div/span[3]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎" in alert_text:
            alert.accept()
        time.sleep(2)
        if "自動化測試修改用" not in driver.page_source:
            print("\033[32m刪除節點成功\033[0m")
        else:            
            print("\033[31m刪除節點失敗\033[0m")

        # 儲存
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_save']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存成功" in alert_text:
            print("\033[32m儲存成功\033[0m")
        else:
            print("\033[31m儲存失敗\033[0m")  
        alert.accept()  

        # 匯出  
        time.sleep(2)
        initial_files = get_downloaded_files(download_directory)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_export']"))    
        ).click()
        time.sleep(2)
        final_files = get_downloaded_files(download_directory)
        time.sleep(2)
        if len(final_files) > len(initial_files):
            print("\033[32m匯出學習路徑成功\033[0m")
        else:
            print("\033[31m匯出學習路徑失敗\033[0m")

        # 全選全消
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_select']"))    
        ).click()
        time.sleep(2)
        checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and not(ancestor::*[contains(@style,'display: none')])]")
        all_checked = all(checkbox.is_selected() for checkbox in checkboxes)
        if all_checked:
            print("\033[32m全選成功\033[0m")
        else:
            unchecked_count = sum(1 for checkbox in checkboxes if not checkbox.is_selected())
            print(f"\033[31m有 {unchecked_count} 個checkbox未被選取\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_select']"))    
        ).click()
        time.sleep(2)
        all_checked = all(not checkbox.is_selected() for checkbox in checkboxes)
        if all_checked:
            print("\033[32m全消成功\033[0m")
        else:
            checked_count = sum(1 for checkbox in checkboxes if checkbox.is_selected())
            print(f"\033[31m有 {checked_count} 個checkbox未被取消\033[0m")

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
