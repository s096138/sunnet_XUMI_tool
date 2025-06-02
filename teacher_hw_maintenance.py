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

# 取得當前時間
nowdatetime = datetime.now().strftime("%Y-%m-%d")

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

def teacher_hw_maintenance(driver):
    try:
        print("測試：辦公室-作業管理-作業維護")
        menu_expanded_with_sibling(driver, "作業管理", "作業維護")
        time.sleep(2)
        if "作業名稱" in driver.page_source:
            print("\033[32m進入作業維護成功\033[0m")
        else:
            print("\033[31m進入作業維護失敗\033[0m") 

        # 題庫分享中心
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'作業管理')])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'題庫維護')])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab03"))
        ).click()
        driver.execute_script("search_item();")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_box2"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選取')]"))
        ).click()
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "您已從資源中心選用" in alert_text:
            print("\033[32m分享中心選用題庫成功\033[0m")
            alert.accept()
        else:
            print("\033[31m分享中心選用題庫失敗\033[0m")
            time.sleep(5)
            alert.accept()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'作業維護')]"))
        ).click()
        
        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        ).click()

        # 作業資訊
        driver.execute_script("switchTab(1);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "最少要填寫其中一種語言" in alert_text:
            print("\033[32m未填作業名稱不可下一步\033[0m")
            alert.accept()
        else:
            print("\033[31m未填作業名稱可以下一步\033[0m")
            time.sleep(5)
            alert.accept()
        time.sleep(2)
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys(f"自動化測試用：{nowdatetime}")
        WebDriverWait(driver, 20).until( # 發布
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn7"))
        ).click()
        WebDriverWait(driver, 20).until( # 發布
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_begin_time"))
        ).click()
        time.sleep(2)
        driver.execute_script("switchTab(1);")   

        # 挑選題目
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='開始搜尋']"))
        ).click()        
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_ck"))
        ).click()            
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//td[@align='right']//input[@value='選取']"))
        ).click()  
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請按【下一步】到排列與配分去" in alert_text:
            print("\033[32m挑選題目成功\033[0m")
            alert.accept()
        else:
            print("\033[31m挑選題目失敗\033[0m")
            time.sleep(5)
            alert.accept()
        driver.execute_script("switchTab(2);")
        
        # 排列與配分
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@value='平均配分']"))
        ).click() 
        score = WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@name='score']"))
        )
        score.click()
        score.clear()
        score.send_keys("100") 
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'確定')])[2]"))
        ).click() 
        driver.execute_script("switchTab(4);")

        # 作業預覽
        driver.execute_script("saveContent();")
        time.sleep(2)
        td1 = driver.find_element(By.XPATH, "//*[@id='displayPanel']/tbody/tr/td[5]").text
        if "自動化測試用" in driver.page_source and nowdatetime in td1:
            print("\033[32m新增作業成功\033[0m")
        else:
            print("\033[31m新增作業失敗\033[0m")

        # 編輯
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".material-icons-outlined.opacity-60.studAction"))
        ).click()  
        time.sleep(2)       
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("自動化測試修改用")
        driver.execute_script("saveContent();") 
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m編輯作業成功\033[0m")
        else:
            print("\033[31m編輯作業失敗\033[0m") 

        #  複製
        time.sleep(2)
        copy = False
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click() 
        driver.execute_script("executing(15);")
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > table:nth-child(12) > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(1) > form:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(1) > input:nth-child(1)"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "複製完成" in alert_text:
            copy = True
            alert.accept()
        else:
            copy = False
            time.sleep(5)
            alert.accept()  
        time.sleep(2) 
        if "COPY" in driver.page_source and copy == True:
            print("\033[32m複製作業成功\033[0m")
            copy = True
        else:
            print("\033[31m複製作業成功失敗\033[0m")
            copy = False
            time.sleep(5)

        #  刪除
        time.sleep(2)
        copy = False
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click() 
        driver.execute_script("executing(3);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除作業嗎" in alert_text:
            alert.dismiss()
        else:
            alert.dismiss()  
        if "COPY" in driver.page_source:
            print("\033[32m取消刪除作業成功\033[0m")
        else:
            print("\033[31m取消刪除作業成功失敗\033[0m")
        time.sleep(2)
        driver.execute_script("executing(3);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除作業嗎" in alert_text:
            copy = True
            alert.accept()
        else:
            copy = False
            alert.accept()  
        time.sleep(2) 
        if "COPY" not in driver.page_source and copy == True:
            print("\033[32m刪除作業成功\033[0m")
        else:
            print("\033[31m刪除作業成功失敗\033[0m")
            time.sleep(5)

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

