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
from menu_expanded import menu_expanded_with_sibling   
from datetime import datetime
import time

# # 取得當前時間
# nowdatetime = datetime.now().strftime("%Y-%m-%d")

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

def teacher_peer_maintenance(driver):
    try:
        print("測試：辦公室-同儕作業管理-作業維護")
        menu_expanded_with_sibling(driver, "同儕作業管理", "作業維護")
        time.sleep(2)
        if "新增作業" in driver.page_source:
            print("\033[32m進入同儕作業維護成功\033[0m")
        else:
            print("\033[31m進入同儕作業維護失敗\033[0m") 

        # 新增
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增作業')]"))
        ).click()       
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試用")

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn4"))
        ).click()  
        time.sleep(2)

        scroll_bottom(driver)
        # WebDriverWait(driver, 20).until(
        #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, rating_criteria_1']"))
        # )
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'body'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '.cke_editable'))
        # ).click()
        # driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", driver.find_element(By.CSS_SELECTOR, '.cke_editable'))
        # driver.switch_to.default_content()
        editables = driver.find_elements(By.CSS_SELECTOR, ".ql-editor")
        editables[1].clear()
        editables[1].send_keys("自動化測試用")
        time.sleep(2)
        driver.execute_script("saveContent(4);")
        time.sleep(2)
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增同儕作業成功\033[0m")
        else:
            print("\033[31m新增同儕作業失敗\033[0m") 

        # 修改
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'修改')]"))
        ).click()         
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試修改用")
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改同儕作業成功\033[0m")
        else:
            print("\033[31m修改同儕作業失敗\033[0m")  

        # 刪除       
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'刪除')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除作業後" in alert_text:
            print("\033[32m刪除同儕作業成功\033[0m")
            alert.accept()
        else:
            print("\033[31m刪除同儕作業失敗\033[0m")
            alert.accept()

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