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

def teacher_discussion_management(driver):
    try:
        print("測試：辦公室-教室管理-討論區")
        menu_expanded(driver, "教室管理", "討論區")
        time.sleep(2)
        if "課程討論區" in driver.page_source and "群組討論區" in driver.page_source:
            print("\033[32m進入討論區成功\033[0m")
        else:
            print("\033[31m進入討論區失敗\033[0m")  

        # 新增
        add = False
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增')]"))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'subject_name_big5'))
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
            print("\033[32m新增討論區成功\033[0m")
        else:
            print("\033[31m新增討論區失敗\033[0m")

        # 修改
        change = False
        time.sleep(2)
        try:
            rows = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//tr"))
            )
            for row in rows:
                if "自動化測試用" in row.text:
                    modify_button = row.find_element(By.XPATH, ".//button[contains(text(), '修改')]")
                    modify_button.click()
                    break  
        except Exception as e:
            print(f"發生錯誤: {e}")
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'subject_name_big5'))
        )
        name.click()
        name.clear()
        name.send_keys("修改測試用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[@id='trStatus']//input[1]")) # 停用
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
            print("\033[32m修改討論區成功\033[0m")
        else:
            print("\033[31m修改討論區失敗\033[0m")

        # 刪除
        delete = False
        time.sleep(2)
        try:
            rows = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, "//tr"))
            )
            for row in rows:
                if "修改測試用" in row.text:
                    checkbox = row.find_element(By.XPATH, ".//input[@type='checkbox']")
                    driver.execute_script("arguments[0].checked = true;", checkbox)
                    break 
        except Exception as e:
            print(f"發生錯誤: {e}")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'刪除')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎？" in alert_text:
            delete = True
            alert.accept()
        else:
            delete = False
        time.sleep(2)
        driver.execute_script("goManage()")   
        if "修改測試用" not in driver.page_source and delete == True:
            print("\033[32m刪除討論區成功\033[0m")
        else:
            print("\033[31m刪除討論區失敗\033[0m")

        # 群組討論區

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