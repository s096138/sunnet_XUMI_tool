from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from menu_expanded import menu_expanded_with_sibling
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
import time

def admin_class(driver):    
    try:        
        print("測試：管理者環境-群組管理-群組管理")  
        menu_expanded_with_sibling(driver, "群組管理", "群組管理")
        time.sleep(2)
        if "新增群組" in driver.page_source:
            print("\033[32m進入群組管理成功\033[0m")
        else:
            print("\033[31m進入群組管理失敗\033[0m")

        # 新增群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_add"))
        ).click()
        time.sleep(2)
        group_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "GPName_Big5"))
        )
        group_name.clear()   
        group_name.send_keys("自動化測試用")
        group_id = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "dep_id"))
        )
        group_id.clear()   
        group_id.send_keys("test001")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "setting_btn"))
        ).click()
        
        # 驗證
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增群組成功\033[0m")
        else:
            print("\033[31m新增群組失敗\033[0m")

        # 修改
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='自動化測試用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='自動化測試用']//div//span[@title='修改群組']"))
        ).click()
        time.sleep(2)
        group_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "GPName_Big5"))
        )
        group_name.clear()   
        group_name.send_keys("自動化測試修改用")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "setting_btn"))
        ).click()
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改群組成功\033[0m")
        else:
            print("\033[31m修改群組失敗\033[0m")

        # 複製
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='自動化測試修改用']//div//span[@title='複製群組']"))
        ).click()
        time.sleep(2)
        elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        if len(elements) == 2:
            print("\033[32m複製群組成功\033[0m")
        else:
            print("\033[31m複製群組失敗\033[0m")
        
        # 刪除
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='自動化測試修改用']//div//span[@title='刪除群組']"))
        ).click()
        time.sleep(2)
        elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        if len(elements) == 1:
            print("\033[32m刪除群組成功\033[0m")
        else:
            print("\033[31m刪除群組失敗\033[0m")

        # 子群組
        time.sleep(2)
        group_row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(group_row).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='自動化測試修改用']//div//span[@title='新增群組']"))
        ).click()       
        time.sleep(2)
        group_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "GPName_Big5"))
        )
        group_name.clear()   
        group_name.send_keys("自動化測試子群組")
        group_id = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "dep_id"))
        )
        group_id.clear()   
        group_id.send_keys("test002")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "setting_btn"))
        ).click()
        time.sleep(2)
        parent = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@title='自動化測試修改用']"))
        )
        child = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//a[@title='自動化測試子群組' and @aria-level='2']"))
        )    
        time.sleep(2)    
        if child:
            print("\033[32m新增子群組成功\033[0m")
        else:
            print("\033[31m新增子群組失敗\033[0m")

        # 不儲存  
        time.sleep(2)      
        driver.refresh()
        time.sleep(2)

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