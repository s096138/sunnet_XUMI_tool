from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def admin_course_introduction(driver):
    try:
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程設定')]"))
        # ).click()
        
        # 接續admin_course_information
        print("測試：管理者環境-課程管理-課程設定(課程介紹)")  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="intro-tab"]'))
        ).click()  

        # 影片介紹 
        time.sleep(2)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="video-file"]/div/label/p[1]/span'))
        ).click() 
        time.sleep(5)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)

        # # 影片網址
        scroll_bottom(driver)
        # youtubeUrl = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'youtubeUrl'))
        # )
        # youtubeUrl.clear()
        # youtubeUrl.send_keys("https://www.youtube.com/live/jfKfPfyJRdk?si=UGMKMVJmMJf8XR24")
        # time.sleep(2)

        # 課程簡介
        time.sleep(2)
        textarea = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "content"))
        )
        textarea.clear()
        textarea.send_keys("自動化測試簡介用")

        # 下一步
        time.sleep(2) 
        driver.execute_script("save_step(2)")    
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            print("\033[32m儲存修改成功\033[0m")
        else:
            print("\033[31m儲存修改失敗\033[0m")
        alert.accept()
           
        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="intro-tab"]'))
        ).click()  
        time.sleep(2)
        video_element = driver.find_element(By.ID, "videoPreview")
        video_src = video_element.get_attribute("src")
        time.sleep(2)
        if video_src:
            print("\033[32m上傳影片成功\033[0m")
        else:
            print("\033[31m上傳影片失敗\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        # url_element = driver.find_element(By.ID, "youtubeUrl")
        # url_value = url_element.get_attribute("value").strip()
        # if url_value == "https//www.youtube.com/live/jfKfPfyJRdk?si=UGMKMVJmMJf8XR24": # 不知道為什麼https後面要少一個冒號
        #     print("\033[32m填寫影片網址成功\033[0m")
        # else:
        #     print("\033[31m填寫影片網址失敗\033[0m")
        time.sleep(2) 
        if "自動化測試簡介用" in driver.page_source:
            print("\033[32m填寫課程簡介成功\033[0m")
        else:
            print("\033[31m填寫課程簡介失敗\033[0m")

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