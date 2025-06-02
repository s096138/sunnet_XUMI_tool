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

def course_chapter(driver):
    try:
        print("測試：學習環境-課程章節")
        time.sleep(2)
        if "114年辦公日曆表" in driver.page_source:
            print("\033[32m進入課程章節成功\033[0m")
        else:
            print("\033[31m進入課程章節失敗\033[0m")

        # 點選章節
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), '114年辦公日曆表')]"))
        ).click()

        # 子母畫面
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(text(), '202410旭航v4')]"))
        ).click()  
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//vm-control[@class='ng-star-inserted']"))
        ).click()
        time.sleep(2)
        vm_player = driver.find_element(By.XPATH, '//vm-player[@id="vm-player-1"]')
        if 'pip' in vm_player.get_attribute('outerHTML'):
            print("\033[32m子母畫面已啟用\033[0m")
        else:
            print("\033[31m子母畫面未啟用\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//vm-control[@class='ng-star-inserted']"))
        ).click()
        time.sleep(2)
        vm_player = driver.find_element(By.XPATH, '//vm-player[@id="vm-player-1"]')
        if 'pip' not in vm_player.get_attribute('outerHTML'):
            print("\033[32m子母畫面已關閉\033[0m")
        else:
            print("\033[31m子母畫面未關閉\033[0m")

        # 選單收合
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//mat-icon[@aria-label='關閉圖示'][normalize-space()='close'])[2]"))
        ).click()
        time.sleep(2)
        style_value = driver.find_element(By.XPATH, '//mat-sidenav-content[@class="mat-drawer-content mat-sidenav-content"]').get_attribute('style')
        if 'margin-right: 481px;' in style_value:
            print("\033[31m選單未收合\033[0m")
        else:
            print("\033[32m選單已收合\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@role='button']"))
        ).click()
        time.sleep(2)
        style_value = driver.find_element(By.XPATH, '//mat-sidenav-content[@class="mat-drawer-content mat-sidenav-content"]').get_attribute('style')
        # print(f"{style_value}")
        if 'margin-right: 481px;' in style_value:
            print("\033[32m選單已展開\033[0m")
        else:
            print("\033[31m選單未展開\033[0m")

        # 編輯圖示
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='編輯圖示']//*[name()='svg']"))
        ).click()
        time.sleep(2)
        if "課程章節" in driver.page_source and "筆記主旨" in driver.page_source:
            print("\033[32m編輯圖示指引成功\033[0m")
        else:
            print("\033[31m編輯圖示指引失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'取消')]"))
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