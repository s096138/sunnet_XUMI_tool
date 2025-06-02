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
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
import time

# 重複嘗試取得text
def get_text(driver, xpath):        
    retries = 3
    while retries > 0:            
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )      
            return element.text
        except Exception as e:
            print(f"Error: {e}")
            retries -= 1
            time.sleep(2)
    return None

def admin_questionnaire(driver):
    try:
        print("測試：管理者環境-問卷管理-問卷維護")
        menu_expanded(driver, "問卷管理", "問卷維護")
        time.sleep(2)
        if "問卷名稱" in driver.page_source:
            print("\033[32m進入問卷維護成功\033[0m")
        else:
            print("\033[31m進入問卷維護失敗\033[0m") 

        # 新增
        driver.execute_script("executing(1)")

        # 問卷名稱
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "title[Big5]"))
        ).send_keys(Keys.BACK_SPACE * 10)
        driver.find_element(By.ID, "title[Big5]").send_keys("自動化測試用")
        # 作答說明
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "notice"))
        ).send_keys("自動化測試用")
        # 發布設定
        WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.ID, "sysRadioBtn7"))
        ).click()
        # 開放附檔作答(預設否)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "sysRadioBtn8"))
        ).click()
        # 是否記名(預設記名)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sysRadioBtn11"))).click()
        # 修改設定(預設可以)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "modifiable"))).click()
        # 問卷類型(預設封閉)
        #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "sysRadioBtn13"))).click()  
        # 公布答案
        select = Select(driver.find_element(By.ID, "announce_type"))
        select.select_by_visible_text("作答完公布")

        # 挑題5題
        time.sleep(2)
        driver.execute_script("switchTab(1);")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="開始搜尋"]'))
        ).click()

        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        elements = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.NAME, "pick[]"))
        )

        # 點擊前五個元素
        for i in range(min(5, len(elements))):
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(elements[i])
            ).click()

        driver.execute_script("pickItem()")
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "請按【下一步】到排列調整去，或繼續挑選題目"
        alert.accept()

        # 完成存檔
        driver.execute_script("switchTab(2);")
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增問卷成功\033[0m")
        else:
            print("\033[31m新增問卷失敗\033[0m")

        # 拖曳問卷順序
        def get_element_text(driver, xpath):
            retries = 3
            while retries > 0:
                try:
                    elements = WebDriverWait(driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, xpath))
                    )
                    if elements:
                        return elements[0].text
                except Exception as e:
                    print(f"Error: {e}")
                    retries -= 1
                    time.sleep(2)
            return None
            time.sleep(2)

        actions = ActionChains(driver)
        source_element = driver.find_element(By.XPATH, '//*[@id="displayPanel"]/tbody/tr[1]/td[5]')
        target_element = driver.find_element(By.XPATH, '//*[@id="displayPanel"]/tbody/tr[5]/td[5]')
        actions.drag_and_drop(source_element, target_element).perform()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu3"]/li[1]/a'))  # 點出去
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu3"]/li[2]/a'))  # 點回來
        ).click()
    
        xpath = '//*[@id="displayPanel"]/tbody/tr[1]/td[2]/table/tbody/tr/td'
        top_text = get_element_text(driver, xpath)
        if top_text is not None:
            if top_text == "自動化測試用":
                print("\033[32m拖曳順序未儲存成功\033[0m")
            else:
                print("\033[31m拖曳順序未儲存失敗\033[0m")

        time.sleep(2)
        actions = ActionChains(driver)
        source_element = driver.find_element(By.XPATH, '//*[@id="displayPanel"]/tbody/tr[1]/td[5]')
        target_element = driver.find_element(By.XPATH, '//*[@id="displayPanel"]/tbody/tr[5]/td[5]')
        actions.drag_and_drop(source_element, target_element).perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="btn_save"]'))  # 儲存
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "儲存順序成功"
        alert.accept()
        xpath = '//*[@id="displayPanel"]/tbody/tr[1]/td[2]/table/tbody/tr/td'
        top_text = get_element_text(driver, xpath)
        if top_text is not None:
            if top_text != "自動化測試用":
                print("\033[32m拖曳順序儲存成功\033[0m")
            else:
                print("\033[31m拖曳順序儲存失敗\033[0m")
        
        # 批次動作-發布/準備中
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td//text()='自動化測試用']//input[@type='checkbox']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"批次動作")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"發布/準備中 (可多選)")]'))
        ).click()
        time.sleep(2)
        if "準備中" in driver.page_source:
            print("\033[32m批次動作：發布/準備中成功\033[0m")
        else:
            print("\033[31m批次動作：發布/準備中失敗\033[0m")

        # 批次動作-複製
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td//text()='自動化測試用']//input[@type='checkbox']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"批次動作")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"複製 (可多選)")]'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "複製完成"
        alert.accept()
        time.sleep(2)
        #print(copy)
        if "COPY" in driver.page_source:
            print("\033[32m批次動作：複製成功\033[0m")
        else:
            print("\033[31m批次動作：複製失敗\033[0m")

        # 批次動作-清除作答紀錄
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td//text()='自動化測試用']//input[@type='checkbox']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"批次動作")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"清除作答記錄 (可多選)")]'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "系統將會清除目前所選項目的全部學員填答的內容，\n確定要清除作答記錄嗎？"
        alert.accept()
        time.sleep(2)
        #print(copy)
        if "COPY" in driver.page_source:
            print("\033[32m批次動作：清除作答紀錄成功\033[0m")
        else:
            print("\033[31m批次動作：清除作答紀錄失敗\033[0m")

        # 批次動作-刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td//text()='自動化測試用']//input[@type='checkbox']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td//text()='COPY_自動化測試用']//input[@type='checkbox']"))
        ).click() 
        time.sleep(2)       
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"批次動作")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"刪除 (可多選)")]'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "確定刪除問卷嗎？確定請按「確定」，要停止請按「取消」。"
        alert.accept()
        time.sleep(2)
        if "COPY_自動化測試用" not in driver.page_source and "自動化測試用" not in driver.page_source:
            print("\033[32m批次動作：刪除成功\033[0m")
        else:
            print("\033[31m批次動作：刪除失敗\033[0m")

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