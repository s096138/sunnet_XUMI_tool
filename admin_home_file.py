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
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
import time

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def admin_homefile(driver):
    try:
        print("測試：管理者環境-平台管理-首頁檔案管理")
        menu_expanded(driver, "平台管理", "首頁檔案管理")
        time.sleep(2)
        if "檔案名稱" in driver.page_source:
            print("\033[32m進入首頁檔案管理成功\033[0m")
        else:
            print("\033[31m進入首頁檔案管理失敗\033[0m") 

        # 新建目錄
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="tab02"]'))
        ).click()
        input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContent2"]/div[2]/div/div/input'))
        )
        input.click()
        input.send_keys("自動化測試目錄用")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"確定建立")]'))
        ).click() 
        time.sleep(2)
        if "建立目錄 [自動化測試目錄用] 成功。" in driver.page_source:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="tab01"]'))
            ).click()
            time.sleep(2)
            if "自動化測試目錄用" in driver.page_source:
                print("\033[32m新建目錄成功\033[0m")
                time.sleep(2)
                # scroll_bottom(driver)
                # WebDriverWait(driver, 20).until(
                #     EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試目錄用')]/ancestor::tr//input[@type='checkbox']"))
                # ).click()
                # driver.execute_script("removeFile()")
                # alert = driver.switch_to.alert
                # assert alert.text == "您確定要刪除這些選定的項目嗎？"
                # alert.accept()
                # time.sleep(2)
            else:
                print("\033[31m新建目錄失敗\033[0m")
        else:
            print("\033[31m新建目錄失敗\033[0m")

        # 上傳檔案
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="tab04"]'))
        ).click()
        file_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "upload[]"))
        )
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].disabled = false;", file_input)
        file_input.send_keys("C:\\Users\\SGQA2\\Downloads\\兔子.jpg")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="上傳"]'))
        ).click()
        time.sleep(2)
        if "上傳完成" in driver.page_source:
            print("\033[32m上傳檔案成功\033[0m")
        else:
            print("\033[31m上傳檔案失敗\033[0m")
        
        # 上傳壓縮檔
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="tab05"]'))
        ).click()
        zip_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "uploadz"))
        )
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].disabled = false;", zip_input)
        zip_input.send_keys("C:\\Users\\SGQA2\\Downloads\\chromedriver-win64.zip")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="上傳壓縮檔"]'))
        ).click()
        if "解壓縮 [chromedriver-win64.zip] 成功。" in driver.page_source:
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//button[@id="tab01"]'))
            ).click()
            if "chromedriver-win64" in driver.page_source:
                print("\033[32m上傳壓縮檔成功\033[0m")       
            else:
                print("\033[31m檔案總管沒有上傳的壓縮檔\033[0m")
                time.sleep(2)
        else:
            print("\033[31m上傳壓縮檔失敗\033[0m")

        # 編輯檔名
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'兔子.jpg')]/ancestor::tr//span[@class='material-icons-outlined opacity-60 studAction' and text()='edit']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert.send_keys("123")
        alert.accept()
        time.sleep(2)
        if "已存在相同的目錄名稱或檔案名稱，請重新命名":
            print("\033[32m檔名不可重複\033[0m")
        else:
            print("\033[31m檔名可以重複\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'兔子.jpg')]/ancestor::tr//span[@class='material-icons-outlined opacity-60 studAction' and text()='edit']"))
        ).click()
        alert = driver.switch_to.alert
        alert.send_keys("自動化測試修改用")
        alert.accept()
        time.sleep(2)
        if "更換名稱成功。" in driver.page_source:
            print("\033[32m編輯檔名成功\033[0m")
        else:
            print("\033[31m編輯檔名失敗\033[0m")
        time.sleep(2)

        # 複製
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試目錄用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        driver.execute_script("copy('cp')")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "複製功能不適用於目錄。" in alert_text:
            alert.accept()
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "請勾選所要複製的項目。" in alert_text:
                print("\033[32m複製功能不適用於目錄\033[0m")
                alert.accept()
            else:
                print("\033[32m複製功能適用於目錄\033[0m")
                time.sleep(5)
                alert.accept()
        else:
            print("\033[32m複製功能適用於目錄\033[0m")
            time.sleep(5)
            alert.accept()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試修改用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        scroll_top(driver)
        driver.execute_script("copy('cp')")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="自動化測試目錄用"]'))
        ).click()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"自動化測試目錄用")]'))
        ).click()   
        time.sleep(2)
        if "切換目錄成功":
            print("\033[32m切換目錄成功\033[0m")
            if "自動化測試修改用" in driver.page_source:
                print("\033[32m複製檔案成功\033[0m")
            else:
                print("\033[31m複製檔案失敗\033[0m")
        else:
            print("\033[31m切換目錄失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//b[normalize-space()=".."]'))
        ).click()

        # 搬移
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'chromedriver-win64')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        driver.execute_script("copy('mv')")
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "搬移功能不適用於目錄。" in alert_text:
            alert.accept()
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "請勾選所要搬移的項目。" in alert_text:
                print("\033[32m搬移功能不適用於目錄\033[0m")
                alert.accept()
            else:
                print("\033[31m搬移功能適用於目錄\033[0m")
                time.sleep(5)
                alert.accept()
        else:
            print("\033[31m搬移功能適用於目錄\033[0m")
            time.sleep(5)
            alert.accept()
            
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試修改用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        scroll_top(driver)
        driver.execute_script("copy('mv')")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="自動化測試目錄用"]'))
        ).click()
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"自動化測試目錄用")]'))
        ).click()   
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m搬移檔案成功\033[0m")
        else:
            print("\033[31m搬移檔案失敗\033[0m")
        
        #搬回去
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試修改用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        driver.execute_script("copy('mv')")      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="/root"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("復原")
        else:
            print("復原失敗")

        # 刪除檔案
        time.sleep(2)
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試修改用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        driver.execute_script("removeFile()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些選定的項目嗎？" in alert_text:
            alert.accept()
            time.sleep(2)
            if "自動化測試修改用" not in driver.page_source:
                print("\033[32m刪除檔案成功\033[0m")
            else:
                print("\033[31m刪除檔案失敗\033[0m", alert_text)
        else:
            print("\033[31m刪除檔案失敗\033[0m", alert_text)
            time.sleep(2)
            alert.accept()

        # 刪除目錄
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'自動化測試目錄用')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//td/a[contains(text(),'chromedriver-win64')]/ancestor::tr//input[@type='checkbox']"))
        ).click()
        driver.execute_script("removeFile()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些選定的項目嗎？" in alert_text:
            alert.accept()
            time.sleep(2)
            if "自動化測試目錄用" not in driver.page_source:
                print("\033[32m刪除目錄成功\033[0m")
            else:
                print("\033[31m刪除目錄失敗\033[0m", alert_text)
        else:
            print("\033[31m刪除目錄失敗\033[0m", alert_text)
            time.sleep(2)
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