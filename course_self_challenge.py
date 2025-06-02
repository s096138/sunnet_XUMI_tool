from selenium import webdriver
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
import re
import time
from datetime import datetime

nowdatetime = datetime.now().strftime("%Y%m%d")

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def course_self_challenge(driver):
    try:
        print("測試：學習環境-自我挑戰")
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-tab-label-content'][contains(text(),'自我挑戰')]"))
        ).click()
        
        # 檢查畫面上是否已有題目
        time.sleep(2)
        if "關卡建造中" in driver.page_source:
            print("\033[31m挑戰題目數量不足\033[0m")
            return
        elif "現在只需要按下發起挑戰" in driver.page_source:
            print("\033[32m進入自我挑戰成功\033[0m")
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'發起挑戰')]"))
            ).click()
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
            ).click()
        else:
            challenge_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'challenge-header__title')]")
            time.sleep(2)
            if challenge_elements:
                latest_challenge = challenge_elements[-1].text  # 獲取最後一個元素
                time.sleep(2)
                if nowdatetime in latest_challenge:
                    match = re.search(r'_v(\d+)$', latest_challenge)
                    time.sleep(2)
                    if match:
                        latest_version = int(match.group(1))
                        next_version = latest_version + 1
                        next_challenge_name = f"{nowdatetime}_自我挑戰_v{next_version}"
                        WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'發起挑戰')]"))
                        ).click()
                        WebDriverWait(driver, 20).until(
                            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
                        ).click()
                    else:
                        print("\033[31m未找到版本號\033[0m")
                        return
                else:
                    next_challenge_name = f"{nowdatetime}_自我挑戰_v1"
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'發起挑戰')]"))
                    ).click()
                    WebDriverWait(driver, 20).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
                    ).click()
            else:
                print("\033[31m沒有找到任何挑戰名稱\033[0m")
                return

        # 設定關卡
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-radio'])[2]")) # 試煉場
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'開始挑戰')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()

        # 開始挑戰
        time.sleep(2)
        try:
            point = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "(//span[@class='question__points ng-star-inserted'][contains(text(),'10 分')])[1]"))
            )
            print("\033[32m每題配分顯示成功\033[0m")
        except TimeoutException:
            print("\033[31m每題配分顯示失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-radio'])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[@class='mock-radio'])[3]"))
        ).click()
        scroll_bottom(driver)
        
        # 結束挑戰
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'结束挑戰')]"))
        ).click()
        time.sleep(2)
        if "繳交成功" in driver.page_source:
            print("\033[32m繳交自我挑戰成功\033[0m")
        else:
            print("\033[31m繳交自我挑戰失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'關閉')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='reset']"))
        ).click()

        # 查看結果
        time.sleep(2)
        if "關卡名稱" in driver.page_source and "練習次數" in driver.page_source and "成績" in driver.page_source:
            print("\033[32m查看自我挑戰結果成功\033[0m")
        else:
            print("\033[31m查看自我挑戰結果失敗\033[0m")
        try:
            first_option_selected = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'js-user-answer')]"))
            )
            print("\033[32m作答內容顯示成功\033[0m")
        except TimeoutException:
            print("\033[31m作答內容顯示失敗\033[0m")
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'查看詳解')])[10]"))
        ).click()
        time.sleep(2)
        try:
            explain = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='answer-key__content ng-star-inserted'])[1]"))
            )
            print("\033[32m查看詳解成功\033[0m")
        except TimeoutException:
            print("\033[31m查看詳解失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'返回列表')]"))
        ).click()
        time.sleep(2)

        # 返回列表
        scroll_bottom(driver)
        time.sleep(2)
        if next_challenge_name in driver.page_source and "試煉場" in driver.page_source:
            print("\033[32m列表顯示成功\033[0m")
        else:
            print("\033[31m列表顯示失敗\033[0m")

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