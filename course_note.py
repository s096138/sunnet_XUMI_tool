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
from selenium.webdriver.common.keys import Keys
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
            
def course_note(driver):
    try:
        print("測試：學習環境-筆記")
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH,  "//div[@role='tab' and contains(., '筆記')]"))
        ).click()
        time.sleep(2)
        if "新增筆記" in driver.page_source:
            print("\033[32m進入筆記成功\033[0m")
        else:
            print("\033[31m進入筆記失敗\033[0m")

        # 新增筆記
        time.sleep(2)
        if "新增筆記" not in driver.page_source:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'取消')]"))
            ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增筆記')]"))
        ).click()
        Topics = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='筆記主旨']"))
        )
        Topics.send_keys('自動化測試用')
        WebDriverWait(driver, 20).until(
            EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, editor1']"))
        )
        editor_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable"))
        )
        editor_body.clear()
        editor_body.send_keys("自動化測試用")
        time.sleep(2)
        driver.switch_to.default_content()
        # time.sleep(2)
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, ".ql-editor"))
        # )
        # editable.click()  
        # editable.send_keys("自動化測試")
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'儲存筆記')]"))
        ).click()
        
        # 驗證
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增筆記成功\033[0m")
        else:
            print("\033[31m新增筆記失敗\033[0m")    

        # 修改
        note_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//cgust-note"))
        )
        for note in note_elements:
            title_element = note.find_element(By.XPATH, "//em[@class='truncated-text note__title ng-star-inserted']")
            if title_element.text == "自動化測試用":
                edit_button = note.find_element(By.XPATH, "//button[@class='note__icon-action ng-star-inserted']")
                edit_button.click()
                break
        time.sleep(2) 
        edit_topics = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入標題']"))
        )
        edit_topics.clear()
        edit_topics.send_keys('自動化測試修改用')
        # time.sleep(2) 
        # WebDriverWait(driver, 20).until(
        #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[contains(@aria-label, '編輯器')]"))
        # )
        # editor_body = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "body.cke_editable"))
        # )
        # editor_body.clear()
        # editor_body.send_keys("自動化測試修改用")
        # driver.switch_to.default_content()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'送出')]"))
        ).click()

        # 驗證
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改筆記成功\033[0m")
        else:
            print("\033[31m修改筆記失敗\033[0m")      
        time.sleep(2) 

        # 關鍵字搜尋
        search = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        search.clear()
        search.send_keys("自動化測試修改用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)

        # 驗證
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")      
        time.sleep(2) 
        
        # 刪除
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:trash-bin']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'取消')]"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m取消刪除成功\033[0m")
        else:
            print("\033[31m取消刪除失敗\033[0m")      
        time.sleep(2) 

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:trash-bin']//*[name()='svg']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'確定')]"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" not in driver.page_source:
            print("\033[32m刪除筆記成功\033[0m")
        else:
            print("\033[31m刪除筆記失敗\033[0m")      
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

        