from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded
from selenium_driver import initialize_driver
import time

def teacher_rollcall_history(driver):
    try:
        print("測試：辦公室-人員管理-點名歷程")
        menu_expanded(driver, "人員管理", "點名歷程")
        time.sleep(2)
        if "新增點名" in driver.page_source:
            print("\033[32m進入點名歷程成功\033[0m")
        else:
            print("\033[31m進入點名歷程失敗\033[0m")

        # 新增
        initial_window_handles = driver.window_handles
        initial_window_count = len(initial_window_handles)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_new']"))
        ).click()
        try:
            WebDriverWait(driver, 10).until(
                EC.alert_is_present()
            )
            alert = driver.switch_to.alert
            if "目前正在點名中，請結束程式" in alert.text:
                print("\033[31m點名中，無法進行點名\033[0m")
                alert.accept()
                return
            else:
                print(f"\033[31m{alert.text}\033[0m")
                alert.accept()
                return
        except TimeoutException:
            pass
        time.sleep(2)
        current_window_handles = driver.window_handles
        current_window_count = len(current_window_handles)
        if current_window_count > initial_window_count:
            print("\033[32m新增點名成功\033[0m")
            root_window = driver.current_window_handle
            new_window = [window for window in driver.window_handles if window != root_window][0]
            driver.switch_to.window(new_window)
            time.sleep(2)
            # 開始點名
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "start_button"))
            ).click()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#start-box .true_button"))
            ).click()
            # 結束點名
            time.sleep(5)
            driver.execute_script("var event = new MouseEvent('click', { bubbles: true }); document.getElementById('over_button').dispatchEvent(event);")
            time.sleep(2)
            driver.execute_script("var element = document.evaluate('//a[@onclick=\"over();\"]//div[contains(@class, \"true_button\") and contains(text(), \"確定\")]',document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue; if (element) { element.dispatchEvent(new MouseEvent('click', { bubbles: true })); }")
            # driver.close()
            driver.switch_to.window(initial_window_handles[0])
        else:
            print("\033[32m新增點名失敗\033[0m")    

        # 檢視內容
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[7]/button[1]"))
        ).click() 
        time.sleep(2)
        status = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//*[@id='dataTabs']/tbody/tr[1]/td[5]/select"))
        )   
        display = driver.execute_script("return window.getComputedStyle(arguments[0]).display;", status)
        visibility = driver.execute_script("return window.getComputedStyle(arguments[0]).visibility;", status)
        # print(f"Display: {display}, Visibility: {visibility}")
        if display == "none" or visibility == "hidden":
            driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", status)    
        select = Select(status)
        select.select_by_value("1")     
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'儲存')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完成" in alert_text:
            print("\033[32m儲存點名紀錄成功\033[0m")
            alert.accept()
        else:
            print("\033[31m儲存點名紀錄失敗\033[0m") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回課程點名')]"))
        ).click()

        # 刪除   
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/td[8]/button[1]"))
        ).click()               
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除" in alert_text:
            print("\033[32m刪除點名紀錄成功\033[0m")
            alert.accept()
        else:
            print("\033[31m刪除點名紀錄失敗\033[0m") 

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