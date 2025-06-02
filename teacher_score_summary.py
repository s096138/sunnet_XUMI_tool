from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from selenium import webdriver
import time
import os
from dotenv import load_dotenv

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

def teacher_score_summary(driver):
    try:
        print("測試：辦公室-成績管理-成績總表")
        menu_expanded(driver, "成績管理", "成績總表")
        time.sleep(2)
        if "連續輸入的游標方向" in driver.page_source:
            print("\033[32m進入成績總表成功\033[0m")
        else:
            print("\033[31m進入成績總表失敗\033[0m") 

        # 新增成績
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'成績管理')])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'成績管理')])[2]"))
        ).click()

        time.sleep(2)
        driver.execute_script("processFunc(1);")
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        ) 
        name.click()
        name.clear()
        name.send_keys("自動化測試用")  
        scroe1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fields[yyytest][0]']"))
        ) 
        scroe1.click()
        scroe1.clear()
        scroe1.send_keys("50") 
        scroe2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='fields[yqi][0]']"))
        ) 
        scroe2.click()
        scroe2.clear()
        scroe2.send_keys("60")     
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='確定建立']"))
        ).click()      
        time.sleep(2)
        if "自動化測試" in driver.page_source:
            print("\033[32m新增成績成功\033[0m")
        else:
            print("\033[31m新增成績失敗\033[0m") 

        # 成績總表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(),'成績管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'成績總表')]"))
        ).click()
        time.sleep(2)    

        # 批次調整(上)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='批次調整分數']"))
        ).click()
        time.sleep(2)
        move = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入分數']"))
        )
        move.clear()
        move.send_keys("50")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 驗證
        time.sleep(2)
        text1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)"))
        ).text
        text2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)"))
        ).text
        time.sleep(2)
        if text1 == "100" and text2 == "100":
            print("\033[32m往上平移成績成功\033[0m")
        else:
            print("\033[31m往上平移成績失敗\033[0m")             
        
        # 批次調整(下)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='批次調整分數']"))
        ).click()
        time.sleep(2)
        move = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入分數']"))
        )
        move.clear()
        move.send_keys("-20")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 驗證
        time.sleep(2)
        text1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)"))
        ).text
        text2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)"))
        ).text
        time.sleep(2)
        if text1 == "80" and text2 == "80":
            print("\033[32m往下平移成績成功\033[0m")
        else:
            print("\033[31m往下平移成績失敗\033[0m")  

        # 批次調整(自訂)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@title='批次調整分數']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > div:nth-child(5) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > form:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"))
        ).click()
        move = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入公式']"))
        )
        move.clear()
        move.send_keys("S^(1/2)+60")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()

        # 驗證
        text1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)"))
        ).text
        text2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)"))
        ).text
        time.sleep(2)
        if text1 == "68.94"  and text2 == "68.94":
            print("\033[32m自定義公式套用成功\033[0m")
        else:
            print("\033[31m自定義公式套用失敗\033[0m")              

        # 手動輸入
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(2)"))
        ).click()
        text1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[onsubmit='return false;'] input[type='text']"))
        )
        text1.clear()
        text1.send_keys("50",Keys.ENTER)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(12) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(2)"))
        ).click()
        text2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[onsubmit='return false;'] input[type='text']"))
        )
        text2.clear()
        text2.send_keys("60",Keys.ENTER)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='saveBtm']"))
        ).click()

        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m儲存成績成功\033[0m")
        else:
            print("\033[31m儲存成績失敗\033[0m")    
        alert.accept()

        # 組距圖表
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@src='/theme/default/teach/graph.gif']"))
        ).click()       
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        original_window = driver.current_window_handle
        for handle in driver.window_handles:
            if handle != original_window:
                driver.switch_to.window(handle)
                break
        try:
            load_dotenv()
            base_url = os.getenv("BASE_URL")
            target_url = f"{base_url}/teach/grade/grade_graph1.php"
            time.sleep(2)
            if target_url in driver.page_source:
                print("\033[32m組距圖表開啟成功\033[0m")
            else:
                print("\033[31m組距圖表開啟失敗\033[0m")

        finally:
            time.sleep(2)
            driver.close()
            driver.switch_to.window(original_window)

        # 匯出csv
        initial_files = get_downloaded_files(download_directory)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='匯出 CSV']"))
        ).click()        
        time.sleep(5)
        final_files = get_downloaded_files(download_directory)
        time.sleep(2)
        if len(final_files) > len(initial_files):
            print("\033[32m統計資料下載成功\033[0m")
        else:
            print("\033[31m統計資料下載失敗\033[0m")

        # 刪除成績
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".pb-1:nth-child(8) > .nav-link > span:nth-child(1)"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu8 > .nav-item:nth-child(1) span:nth-child(2)"))
        ).click()

        delect = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ckbox"))
        ).click() 
        driver.execute_script("processFunc(3);")
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "你確定要刪除這些選擇的成績項目嗎" in alert_text:
            delect = True
        else:
            delect = False
        alert.accept()
        time.sleep(2)
        if "自動化測試成績修改用" not in driver.page_source and delect == True:
            print("\033[32m刪除成績成功\033[0m") 
        else:
            print("\033[31m刪除成績失敗\033[0m") 

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