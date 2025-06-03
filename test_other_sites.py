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
from selenium_driver import initialize_driver

# 滾動到底部
def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def test_other_sites(driver): 
    test_passed = True
    error_messages = []
    
    try:
        print("測試：首頁-相關網站連結")
        
        # 測試滾動
        try:
            scroll_bottom(driver)
            time.sleep(2)
            if "平台人數" in driver.page_source:
                print("\033[32m滾動到相關網站連結成功\033[0m")
            else:
                error_msg = "滾動到相關網站連結失敗：未找到'平台人數'文字"
                print(f"\033[31m{error_msg}\033[0m")
                error_messages.append(error_msg)
                test_passed = False
        except Exception as e:
            error_msg = f"滾動測試失敗: {str(e)}"
            print(f"\033[31m{error_msg}\033[0m")
            error_messages.append(error_msg)
            test_passed = False
        
        # 測試左右箭頭
        try:
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:chevron-right']//*[name()='svg']"))
            ).click()
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-icon[@svgicon='common:chevron-left']//*[name()='svg']")) 
            ).click()
            time.sleep(1)
            print("\033[32m左右箭頭測試成功\033[0m")
        except Exception as e:
            error_msg = f"左右箭頭測試失敗: {str(e)}"
            print(f"\033[31m{error_msg}\033[0m")
            error_messages.append(error_msg)
            test_passed = False

        # 測試第一個相關網站連結
        try:
            original_window_handles = driver.window_handles
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='輪播圖第 0 張']"))
            ).click()
            WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
            new_window_handles = driver.window_handles

            if len(new_window_handles) > len(original_window_handles):
                print("\033[32m點選相關網站連結並跳轉成功一次\033[0m")
                # 切換到新視窗並檢查網址
                new_window = [x for x in new_window_handles if x not in original_window_handles][0]
                driver.switch_to.window(new_window)
                time.sleep(2)  # 等待頁面加載
                print(f"新視窗網址: {driver.current_url}")
                driver.close()
                driver.switch_to.window(original_window_handles[0])
            else:
                raise Exception("新視窗未正確開啟")
                
        except Exception as e:
            error_msg = f"第一個相關網站連結測試失敗: {str(e)}"
            print(f"\033[31m{error_msg}\033[0m")
            error_messages.append(error_msg)
            test_passed = False
            # 確保回到原始視窗
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        # 測試第二個相關網站連結
        try:
            original_window_handles = driver.window_handles
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@alt='輪播圖第 1 張']"))
            ).click()
            WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
            new_window_handles = driver.window_handles

            if len(new_window_handles) > len(original_window_handles):
                print("\033[32m點選相關網站連結並跳轉成功兩次\033[0m")
                # 切換到新視窗並檢查網址
                new_window = [x for x in new_window_handles if x not in original_window_handles][0]
                driver.switch_to.window(new_window)
                time.sleep(2)  # 等待頁面加載
                print(f"新視窗網址: {driver.current_url}")
                driver.close()
                driver.switch_to.window(original_window_handles[0])
            else:
                raise Exception("新視窗未正確開啟")
                
        except Exception as e:
            error_msg = f"第二個相關網站連結測試失敗: {str(e)}"
            print(f"\033[31m{error_msg}\033[0m")
            error_messages.append(error_msg)
            test_passed = False
            # 確保回到原始視窗
            if len(driver.window_handles) > 1:
                driver.switch_to.window(driver.window_handles[-1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])

        # 如果有任何錯誤，拋出異常
        if not test_passed:
            raise Exception("\n".join(error_messages))
            
    except Exception as e:
        # 捕獲並重新拋出異常，讓上層處理
        error_msg = f"測試執行時發生錯誤: {str(e)}"
        print(f"\033[31m{error_msg}\033[0m")
        raise Exception(error_msg) from e
    except NoSuchElementException as e:
        print(f"未找到元素: {e}")
        return
    except ElementClickInterceptedException as e:
        print(f"無法點擊該元素: {e}")
        return
    except TimeoutException as e:
        print(f"等待元素可點擊超時: {e}")
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
