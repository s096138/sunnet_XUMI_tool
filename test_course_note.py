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
import time

def test_course_note(driver):
    try:
        print("測試：首頁-會員專區-筆記空間(課程筆記)")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'筆記空間')]"))
        ).click()
        time.sleep(2)
        if "我的筆記數" in driver.page_source:
            print("\033[32m進入筆記空間成功\033[0m")
        else:
            print("\033[31m進入筆記空間失敗\033[0m")
        
        # 課程狀態
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-form-field-infix:nth-child(3)"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text'][contains(text(),'開課中')]"))
        ).click()
        time.sleep(2)
        if "人文地理學" in driver.page_source and "科技與生活" not in driver.page_source:
            print("\033[32m課程狀態(開課中)搜尋成功\033[0m")
        else:
            print("\033[31m課程狀態(開課中)搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-form-field-infix:nth-child(3)"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'已退選')]"))
        ).click()
        time.sleep(2)
        if "科技與生活" in driver.page_source and "人文地理學" not in driver.page_source:
            print("\033[32m課程狀態(已退選)搜尋成功\033[0m")
        else:
            print("\033[31m課程狀態(已退選)搜尋失敗\033[0m")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".mat-form-field-infix:nth-child(3)"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'全部課程')]"))
        ).click()
        time.sleep(2)  

        # 關鍵字搜尋
        search = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入課程名稱']"))
        )
        search.clear()
        search.send_keys("科技與生活") 
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "科技與生活" in driver.page_source and "人文地理學" not in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")

        # 空白搜尋 
        time.sleep(2)                  
        search = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='請輸入課程名稱']"))
        )
        search.clear()
        search.send_keys(" ") 
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "科技與生活" in driver.page_source and "人文地理學" in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")  

        # 進入筆記
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[1]/div[1]"))
        ).click()       
        time.sleep(2)

        # 課程狀態
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[2]/mat-form-field/div/div/div[3]/mat-select/div/div"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'我的筆記')]"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m我的筆記搜尋成功\033[0m")
        else:
            print("\033[31m我的筆記搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[2]/mat-form-field/div/div/div[3]/mat-select/div/div"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'他人筆記')]"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "羅斯汀的筆記喔0930" in driver.page_source and "0919改" in driver.page_source:
            print("\033[32m他人筆記搜尋成功\033[0m")
        else:
            print("\033[31m他人筆記搜尋失敗\033[0m")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//div[2]/mat-form-field/div/div/div[3]/mat-select/div/div"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='mat-option-text'][contains(text(),'所有筆記')]"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "羅斯汀的筆記喔0930" in driver.page_source and "自動化測試用" in driver.page_source:
            print("\033[32m所有筆記搜尋成功\033[0m")
        else:
            print("\033[31m所有筆記搜尋失敗\033[0m")

        # 關鍵字搜尋 
        time.sleep(2)                  
        search = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='搜尋主旨、內容、作者']"))
        )
        search.clear()
        search.send_keys("自動化測試用") 
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")  

        # 空白搜尋 
        time.sleep(2)                  
        search = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='搜尋主旨、內容、作者']"))
        )
        search.clear()
        search.send_keys(" ") 
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "羅斯汀的筆記喔0930" in driver.page_source and "0919改" in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")  
        
        # 按讚
        topic_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//em[contains(text(),'自動化測試用')]"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        ).click()
        time.sleep(2)
        like_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button1 = like_button.text.strip()
        time.sleep(2)

        # 驗證
        # print(button1)
        if button1 == "1":
            print("\033[32m按讚數+1\033[0m")
        else:
            print("\033[31m按讚數無變化\033[0m")
            
        # 驗證點讚按鈕狀態
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button_class = button.get_attribute("class")
        time.sleep(2)
        if "comment__press-like--liked" in button_class:
            print("\033[32m按讚成功\033[0m")
        else:
            print("\033[31m按讚失敗\033[0m")

        # 收回讚     
        topic_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//em[text()='自動化測試用']"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        ).click()
        time.sleep(2)
        like_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button0 = like_button.text.strip()
        time.sleep(2)

        # 驗證
        # print(button0)
        if button0 == "0":
            print("\033[32m按讚數-1\033[0m")
        else:
            print("\033[31m按讚數無變化\033[0m")            

        # 驗證點讚按鈕狀態
        button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'comment__press-like')]"))
        )
        button_class = button.get_attribute("class")
        time.sleep(2)
        if "comment__press-like--liked" not in button_class:
            print("\033[32m收回讚成功\033[0m")
        else:
            print("\033[31m收回讚失敗\033[0m")

        # 回列表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
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