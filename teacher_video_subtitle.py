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
            
def teacher_video_subtitle(driver):
    try:
        print("測試：辦公室-課程管理-全能影像轉譯(AI生成字幕與摘要)")
        menu_expanded(driver, "課程管理", "全能影像轉譯")
        time.sleep(2)
        if "讓備課更輕鬆" in driver.page_source:
            print("\033[31m影片列表沒有影片可供測試\033[0m")
            return
        else:
            pass

        # AI生成字幕與摘要
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
        ).click() 
        time.sleep(2)
        if "字幕與摘要" in driver.page_source:
            print("\033[32m進入全能影像轉譯(AI生成字幕與摘要)成功\033[0m")
        else:
            print("\033[31m進入全能影像轉譯(AI生成字幕與摘要)失敗\033[0m") 
        time.sleep(2)
        if "您的教材還沒有字幕嗎" in driver.page_source:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'讓我們開始吧!')]"))
            ).click()  
        else:
            subtitles_textarea = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "subtitles_textarea"))
            )
            subtitles_textarea.clear()
            summary_textarea = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "summary_textarea"))
            )
            summary_textarea.clear()
            scroll_bottom(driver)
            driver.execute_script("document.getElementById('save_summary').disabled = false;")
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@id='save_summary']"))
            ).click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text
            time.sleep(2)
            if "儲存成功" in alert_text:
                print("\033[32m清空字幕與摘要成功\033[0m")
            else:
                print("\033[31m清空字幕與摘要失敗\033[0m")
            alert.accept()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
            ).click()

            # 重新進入
            time.sleep(2)  
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
            ).click()
            time.sleep(2)
            if "您的教材還沒有字幕嗎" in driver.page_source:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'讓我們開始吧!')]"))
                ).click()  

        # 回列表 
        time.sleep(2)                    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-wm-purple-outline'][contains(text(),'回列表')]"))
        ).click()
        time.sleep(2)
        if "字幕與摘要" not in driver.page_source:
            print("\033[32m回列表成功\033[0m")
        else:
            print("\033[31m回列表失敗\033[0m")
            
        # 真正進入
        time.sleep(2)  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//img[@id='go#202410旭航v4.mp4']"))
        ).click()
        time.sleep(2)
        if "您的教材還沒有字幕嗎" in driver.page_source:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'讓我們開始吧!')]"))
            ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='check_certain']"))
        ).click()
        time.sleep(20) #等待生成
        if "00:00:00,000" in driver.page_source:
            print("\033[32mAI生成字幕成功\033[0m")
        else:
            print("\033[31mAI生成字幕失敗\033[0m")
        time.sleep(2)
        if "教育產業" in driver.page_source or "General AI" in driver.page_source:
            print("\033[32mAI生成摘要成功\033[0m")
        else:
            print("\033[31mAI生成摘要失敗\033[0m")
        scroll_bottom(driver)
        driver.execute_script("document.getElementById('save_summary').disabled = false;")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='save_summary']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        time.sleep(2)
        if "儲存成功" in alert_text:
            print("\033[32m儲存字幕與摘要成功\033[0m")
        else:
            print("\033[31m儲存字幕與摘要失敗\033[0m")
        alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
        ).click() 
        time.sleep(2)
        label1 = driver.find_element(By.XPATH, "//span[contains(text(),'字幕')]").get_attribute("class")
        label2 = driver.find_element(By.XPATH, "//span[contains(text(),'摘要')]").get_attribute("class")   
        if "green-label" in label1 and "green-label" in label2:
            print("\033[32m標籤顏色顯示正確\033[0m")
        else:
            print("\033[31m標籤顏色顯示錯誤\033[0m")
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