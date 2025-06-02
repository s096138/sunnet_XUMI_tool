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
from selenium_driver import initialize_driver
from menu_expanded import menu_expanded
import time

def teacher_chatroom_management(driver):
    try:
        print("測試：辦公室-教室管理-聊天室管理")
        menu_expanded(driver, "教室管理", "聊天室管理")
        time.sleep(2)
        if "課程聊天室列表" in driver.page_source:
            print("\033[32m進入聊天室管理成功\033[0m")
        else:
            print("\033[31m進入聊天室管理失敗\033[0m")

        # 新增
        add = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增')]"))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'host_room_name_big5'))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試用")
        driver.execute_script("saveSetting()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增成功" in alert_text:
            add = True
            alert.accept()
        else:
            add = False
        driver.execute_script("goManage()")
        time.sleep(2) 
        if "自動化測試用" in driver.page_source and add == True:
            print("\033[32m新增討論室成功\033[0m")
        else:
            print("\033[31m新增討論室失敗\033[0m")

        # 編輯
        change = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tbody/tr[2]/td[8]/button[1]"))
        ).click()   
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'host_room_name_big5'))
        )
        name.click()
        name.clear()
        name.send_keys("修改測試用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn3")) # 停用
        ).click() 
        driver.execute_script("saveSetting()")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "更新成功" in alert_text:
            change = True
            alert.accept()
        else:
            change = False
        driver.execute_script("goManage()")
        time.sleep(2)
        if "停用" in driver.page_source and "修改測試用"in driver.page_source and change == True:
            print("\033[32m修改討論室成功\033[0m")
        else:
            print("\033[31m修改討論室失敗\033[0m")

        # 刪除
        delete = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "tr:nth-child(1) > .text-center > .form-check-input"))
        ).click()
        driver.execute_script("delChat();")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您確定要刪除這些討論室嗎？" in alert_text:
            delete = True
            alert.accept()
        else:
            delete = False
        time.sleep(2)
        driver.execute_script("goManage()")   
        if "修改測試用" not in driver.page_source and delete == True:
            print("\033[32m刪除討論室成功\033[0m")
        else:
            print("\033[31m刪除討論室失敗\033[0m")
            
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