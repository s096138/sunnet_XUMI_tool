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
from pywinauto import Application
import time
import os
from dotenv import load_dotenv

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def test_personal_data(driver):
    try:
        print("測試：首頁-會員專區-個人資料")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='個人資料']"))
        ).click()
        time.sleep(2)
        if "個人資料" in driver.page_source:
            print("\033[32m進入個人資料成功\033[0m")
        else:
            print("\033[31m進入個人資料失敗\033[0m")

        # 個人照片
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='編輯圖示']"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        if "個人資料已更新" in driver.page_source:
            print("\033[32m更改個人照片成功\033[0m")
        else:
            print("\033[31m更改個人照片失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='confirm']"))
        ).click()

        # 姓名
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "realname"))
        )
        name.clear()
        name.send_keys('小精靈')

        # 性別
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[3]//span[1]"))
        ).click()
        
        # 身分證號
        time.sleep(2)
        idcard = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "personal_id"))
        )
        idcard.clear()
        idcard.send_keys('123456789')
        time.sleep(2)
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".cgust-form__form-mark.invalid.ng-star-inserted"))
        )
        if error_message:
            print("\033[32m正確驗證身分證號不符要求格式\033[0m")
        else:
            print("\033[31m未驗證身分證號不符要求格式\033[0m")
        idcard.clear()
        idcard.send_keys('A109951849')

        # 滾動
        time.sleep(2)
        title = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='company']"))
        )
        if title:
            driver.execute_script("arguments[0].scrollIntoView(true);", title)
        else:
            print("\033[31m未找到元素，請檢查元素定位\033[0m")

        # 密碼
        time.sleep(2)
        old_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='old_password']"))
        )
        old_password.send_keys('j123456')
        time.sleep(2)
        new_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        new_password.send_keys('1q2w3e4r5tt')
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//small[contains(text(),'不符要求格式')]"))
        )
        if error_message:
            print("\033[32m正確驗證密碼不符要求格式\033[0m")
        else:
            print("\033[31m未驗證密碼不符要求格式\033[0m")
        new_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='password']"))
        )
        new_password.clear()
        new_password.send_keys('1q2w3e4r5T')
        time.sleep(2)
        confirm_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='confirm_password']"))
        )
        confirm_password.send_keys('1q2w3e5t')
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//small[contains(text(),'本次輸入密碼與前次不相符')]"))
        )
        if error_message:
            print("\033[32m正確驗證本次輸入密碼與前次不相符\033[0m")
        else:
            print("\033[31m未驗證本次輸入密碼與前次不相符\033[0m")
        time.sleep(2)
        confirm_password = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@id='confirm_password']"))
        )
        confirm_password.clear()
        confirm_password.send_keys('1q2w3e4r5T')

        #舊密碼顯示與隱藏
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//mat-icon[@aria-label='顯示圖示'][normalize-space()='visibility_off'])[1]"))
        ).click()
        time.sleep(2)
        if  old_password.get_attribute('type') == 'text':
            print("\033[32m舊密碼欄位顯示與隱藏成功\033[0m")
        else:
            print("\033[31m舊密碼欄位顯示與隱藏失敗\033[0m")

        # 新密碼顯示與隱藏
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//mat-icon[@aria-label='顯示圖示'][normalize-space()='visibility_off'])[1]"))
        ).click()
        time.sleep(2)
        if  new_password.get_attribute('type') == 'text':
            print("\033[32m新密碼欄位顯示與隱藏成功\033[0m")
        else:
            print("\033[31m新密碼欄位顯示與隱藏失敗\033[0m")

        # 確認密碼顯示與隱藏
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "(//mat-icon[@aria-label='顯示圖示'][normalize-space()='visibility_off'])[1]"))
        ).click()
        time.sleep(2)
        if  confirm_password.get_attribute('type') == 'text':
            print("\033[32m確認密碼欄位顯示與隱藏成功\033[0m")
        else:
            print("\033[31m確認密碼欄位顯示與隱藏失敗\033[0m")
        
        # 電子信箱
        load_dotenv()
        time.sleep(2)
        email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        )
        email.clear()
        email.send_keys('yyytest')
        time.sleep(2)
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//small[@class='cgust-form__form-mark invalid ng-star-inserted']"))
        )
        if error_message:
            print("\033[32m正確驗證電子信箱不符要求格式\033[0m")
        else:
            print("\033[31m未驗證電子信箱不符要求格式\033[0m")
        email.clear()
        email.send_keys(os.getenv("TEST_EMAIL"))

        # 手機
        time.sleep(2)
        cellphone = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cellphone"))
        )
        cellphone.clear()
        cellphone.send_keys('9690969')
        time.sleep(2)
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//small[@class='cgust-form__form-mark invalid ng-star-inserted']"))
        )
        if error_message:
            print("\033[32m正確驗證手機不符要求格式\033[0m")
        else:
            print("\033[31m未驗證手機不符要求格式\033[0m")
        cellphone.clear()
        cellphone.send_keys('0912345678') 

        # 更新
        time.sleep(2)
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'更新')]"))
        ).click()
        time.sleep(2)
        if "個人資料已更新" in driver.page_source:
            print("\033[32m儲存成功\033[0m")
        else:
            print("\033[31m儲存失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='confirm']"))
        ).click()

        # 驗證各項欄位成功儲存
        time.sleep(2)
        current_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "realname"))
        ).get_attribute('value')
        if current_name == '小精靈':
            print("\033[32m更改姓名成功\033[0m")
        else:
            print(f"\033[31m更改姓名失敗：{current_name}\033[0m")

        selected_gender = driver.find_element(By.XPATH, "//label[input[@value='none']]/input[@formcontrolname='gender']")
        if selected_gender.is_selected():
            print("\033[32m更改性別成功\033[0m")
        else:
            print("\033[31m更改性別失敗\033[0m")
    
        current_email = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "email"))
        ).get_attribute('value')
        if current_email == 'yyytest@mailinator.com':
            print("\033[32m更改電子信箱成功\033[0m")
        else:
            print(f"\033[31m更改電子信箱失敗：{current_email}\033[0m")

        current_cellphone = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "cellphone"))
        ).get_attribute('value')
        if current_cellphone == '0912345678':
            print("\033[32m更改手機號碼成功\033[0m")
        else:
            print(f"\033[31m更改手機號碼失敗：{current_cellphone}\033[0m")

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