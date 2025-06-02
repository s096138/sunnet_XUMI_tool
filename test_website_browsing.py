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
from selenium_driver import initialize_driver
import time

def test_website_browsing(driver):
    driver = initialize_driver()
    try:
        print("測試：首頁-網站導覽")
        # 網站導覽
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'category__description'))
            
        ).click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m跳轉網站導覽成功\033[0m')
        else:
            print("\033[31m跳轉網站導覽失敗\033[0m")
        time.sleep(2)

        # 常見問題
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'常見問題')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用常見問題1" in driver.page_source:
            print('\033[32m跳轉常見問題成功\033[0m')
        else:
            print("\033[31m跳轉常見問題失敗\033[0m")
        time.sleep(2)
        back = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'category__description'))
        )
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 下載專區
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='ng-star-inserted']//a[contains(text(),'下載專區')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用下載1" in driver.page_source:
            print('\033[32m跳轉下載專區成功\033[0m')
        else:
            print("\033[31m跳轉下載專區失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 最新消息
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='ng-star-inserted']//a[contains(text(),'最新消息')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用最新消息1" in driver.page_source:
            print('\033[32m跳轉最新消息成功\033[0m')
        else:
            print("\033[31m跳轉最新消息失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 活動輪播
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '活動輪播'))
        ).click()
        time.sleep(2)
        if "最新消息" in driver.page_source:
            print('\033[32m跳轉活動輪播成功\033[0m')
        else:
            print("\033[31m跳轉活動輪播失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 最新課程
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '最新課程'))
        ).click()
        if "最新課程" in driver.page_source:
            print('\033[32m跳轉最新課程成功\033[0m')
        else:
            print("\033[31m跳轉最新課程失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 熱門課程
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '熱門課程'))
        ).click()
        if "熱門課程" in driver.page_source:
            print('\033[32m跳轉熱門課程成功\033[0m')
        else:
            print("\033[31m跳轉熱門課程失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 相關網站輪播區
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, '網站輪播'))
        ).click()
        if "平台人數" in driver.page_source:
            print('\033[32m跳轉相關網站輪播區成功\033[0m')
        else:
            print("\033[31m跳轉相關網站輪播區失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)
        
        # 網站資訊區塊
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'網站資訊區塊')]"))
        ).click()
        if "平台人數" in driver.page_source:
            print('\033[32m跳轉網站資訊區塊成功\033[0m')
        else:
            print("\033[31m跳轉網站資訊區塊失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 資訊安全政策
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH," //div[@class='ng-star-inserted']//a[contains(text(),'資訊安全政策')]"))
        ).click()
        if "網路安全保護措施" in driver.page_source:
            print('\033[32m跳轉資訊安全政策成功\033[0m')
        else:
            print("\033[31m跳轉資訊安全政策失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)

        # 隱私權宣告
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH," //a[contains(text(),'隱私權宣告')]"))
        ).click()
        if "個人資料之蒐集政策" in driver.page_source:
            print('\033[32m跳轉隱私權宣告成功\033[0m')
        else:
            print("\033[31m跳轉隱私權宣告失敗\033[0m")
        time.sleep(2)
        back.click()
        if "本網站依無障礙網頁設計原則建置" in driver.page_source:
            print('\033[32m返回網站導覽成功\033[0m')
        else:
            print("\033[31m返回網站導覽失敗\033[0m")
        time.sleep(2)
        
        # 回首頁
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CLASS_NAME, 'header__logo'))
        ).click()
        print('回首頁')

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

