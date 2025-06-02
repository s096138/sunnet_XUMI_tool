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
import time

def teacher_file_statistics(driver):
    try:
        print("測試：辦公室-課程管理-教材統計")
        menu_expanded(driver, "課程管理", "教材統計")
        time.sleep(2)
        if "平均時數" in driver.page_source and "閱讀時數" in driver.page_source:
            print("\033[32m進入教材統計成功\033[0m")
        else:
            print("\033[31m進入教材統計失敗\033[0m")
        

        # 最長時間
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(text(),'最長時間')]"))
        ).click()  
        try:
            td1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/font").text
            td2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/font").text
        except NoSuchElementException:
            print("\033[32m資料數量不足無法排序\033[0m")
            return
        time.sleep(2)
        if len(td1) <= len(td2):
            print("\033[32m最長時間排序成功\033[0m")
        else:
            print("\033[31m最長時間排序失敗\033[0m")

        # 最短時間
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(text(),'最短時間')]"))
        ).click()  
        td1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[3]/font").text
        td2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[2]/td[3]/font").text
        time.sleep(2)
        if len(td1) >= len(td2):
            print("\033[32m最短時間排序成功\033[0m")
        else:
            print("\033[31m最短時間排序失敗\033[0m")
        
        # 閱讀次數
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(text(),'閱讀次數')]"))
        ).click()  
        td1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[4]").text
        td2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[2]/td[4]").text
        time.sleep(2)
        if int(td1) >= int(td2):
            print("\033[32m閱讀次數排序成功\033[0m")
        else:
            print("\033[31m閱讀次數排序失敗\033[0m")

        # 閱讀時數
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(text(),'閱讀時數')]"))
        ).click()  
        td1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[5]/font").text
        td2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[2]/td[5]/font").text
        time.sleep(2)
        if len(td1) >= len(td2):
            print("\033[32m閱讀時數排序成功\033[0m")
        else:
            print("\033[31m閱讀時數排序失敗\033[0m")

        # 平均時數
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//th[contains(text(),'平均時數')]"))
        ).click()  
        td1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[1]/td[6]/font").text
        td2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/table/tbody/tr[2]/td[6]/font").text
        time.sleep(2)
        if len(td1) <= len(td2):
            print("\033[32m平均時數排序成功\033[0m")
        else:
            print("\033[31m平均時數排序失敗\033[0m")

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