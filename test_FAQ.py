from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException,
    UnexpectedAlertPresentException
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium_driver import initialize_driver
import time
import os
from dotenv import load_dotenv

def test_FAQ(driver):
    try:
        print("測試：首頁-常見問題")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'常見問題')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用常見問題1" in driver.page_source:
            print('\033[32m進入常見問題成功\033[0m')
        else:
            print("\033[31m進入常見問題失敗\033[0m")

        # 分類
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'自動化測試用分類2')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用常見問題2" in driver.page_source and "自動化測試用常見問題1" not in driver.page_source:
            print("\033[32m搜尋分類成功\033[0m")
        else:
            print("\033[31m搜尋分類失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'全部')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用常見問題2" in driver.page_source and "自動化測試用常見問題1" in driver.page_source:
            print("\033[32m返回全部分類成功\033[0m")
        else:
            print("\033[31m返回全部分類失敗\033[0m")

        # 搜尋
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        ).send_keys("自動化測試用常見問題1")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "共有 1 筆" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")
        time.sleep(5)

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        ).clear()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        ).send_keys(" ")       
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用常見問題1" in driver.page_source and "自動化測試用常見問題2" in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")
        time.sleep(5)
        
        # 問題展開收合
        def click_plus_icon():
            try:
                open_button = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.XPATH, "//mat-icon[@data-mat-icon-name='plus']"))
                )
                # 滾動到加號圖示
                actions = ActionChains(driver)
                actions.move_to_element(open_button).perform()
                open_button.click()
                time.sleep(2)
                style = driver.find_element(By.CLASS_NAME, 'mat-expansion-panel-content').get_attribute('style') 
                if 'hidden' not in style:
                    print("\033[32m問題展開成功\033[0m")
                else:
                    print("\033[31m問題展開失敗\033[0m")
            except StaleElementReferenceException:
                print("元素無效，重新查找元素...")
                click_plus_icon()  # 重新查找並點擊元素
        click_plus_icon()
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-expansion-panel-header[@aria-expanded='true']"))
        ).click()
        time.sleep(2)
        style = driver.find_element(By.CLASS_NAME, 'mat-expansion-panel-content').get_attribute('style') 
        if 'hidden' in style:
            print("\033[32m問題收合成功\033[0m")
        else:
            print("\033[31m問題收合失敗\033[0m")
        
        # 轉寄
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-overlay__cover']"))
        ).click()
        input = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='轉寄']"))
        )
        input.click()
        input.send_keys(os.getenv("TEST_EMAIL"))
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[normalize-space()='add']"))
        ).click()  
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'關閉')]"))
        ).click()

        # # 換頁
        # time.sleep(2)
        # WebDriverWait(driver, 30).until(
        #     EC.element_to_be_clickable((By.XPATH, "//cgust-category-button//ul/li[button[contains(text(),'報名課程')]]"))
        # ).click()
        # time.sleep(2)
        # if "跟實體班相比，線上課程的優點是什麼？" in driver.page_source:
        #     print("\033[32m切換頁籤成功\033[0m")
        # else:
        #     print("\033[31m切換頁籤失敗\033[0m")

        # 另開視窗
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "忘記帳號或密碼" in driver.page_source:
            print("\033[32m轉寄問題成功\033[0m")
        else:
            print("\033[31m轉寄問題失敗\033[0m")
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(2)

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        print("回首頁")

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
        
    return driver