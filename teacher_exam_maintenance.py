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
from datetime import datetime
import time

# 取得當前時間
nowdatetime = datetime.now().strftime("%Y-%m-%d")

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def teacher_exam_maintenance(driver):
    try:
        print("測試：辦公室-測驗管理-試卷維護")
        menu_expanded(driver, "測驗管理", "試卷維護")
        time.sleep(2)
        if "試卷名稱" in driver.page_source:
            print("\033[32m進入試卷維護成功\033[0m")
        else:
            print("\033[31m進入試卷維護失敗\033[0m") 

        # # 題庫分享中心
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pb-1:nth-child(6) > .nav-link"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu6 > .nav-item:nth-child(1) span:nth-child(2)"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab04"))
        # ).click()
        # driver.execute_script("search_item();")
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_box2"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選取')]"))
        # ).click()
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "您已從資源中心選用" in alert_text:
        #     print("\033[32m分享中心選用題庫成功\033[0m")
        #     alert.accept()
        # else:
        #     print("\033[31m分享中心選用題庫失敗\033[0m")
        #     time.sleep(5)
        #     alert.accept()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#menu6 > .nav-item:nth-child(3) span:nth-child(2)"))
        # ).click()  

        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        ).click()

        # 作業資訊
        time.sleep(2)
        driver.execute_script("switchTab(1);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "最少要填寫其中一種語言" in alert_text:
            print("\033[32m未填測驗名稱不可下一步\033[0m")
            alert.accept()
        else:
            print("\033[31m未填測驗名稱可以下一步\033[0m")
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
        WebDriverWait(driver, 20).until( # 開放作答時間
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_begin_time"))
        ).click()
        driver.execute_script("switchTab(1);")   

        # 挑選題目
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn11"))
        ).click()  
        scroll_bottom(driver)     
        num = WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='num'])[2]"))
        )
        # num.click() 
        # num.clear()
        # num.send_keys("1")
        score = WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#immediate_random_pick_score"))
        )
        # score.click() 
        # score.clear()
        # score.send_keys("100")      
        driver.execute_script("arguments[0].removeAttribute('onblur');", num)
        driver.execute_script("arguments[0].value = '1';", num)
        driver.execute_script("arguments[0].removeAttribute('onblur');", score)
        driver.execute_script("arguments[0].value = '100';", score)     
        time.sleep(2)
        driver.execute_script("calculation();")
        time.sleep(2)
        driver.execute_script("switchTab(4);")

        # 作業預覽
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增測驗成功\033[0m")
        else:
            print("\033[31m新增測驗失敗\033[0m")

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
            print("\033[32m編輯測驗成功\033[0m")
        else:
            print("\033[31m編輯測驗失敗\033[0m") 

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
            print("\033[32m複製測驗成功\033[0m")
            copy = True
        else:
            print("\033[31m複製測驗成功失敗\033[0m")
            copy = False
            time.sleep(5)

        #  清除作答紀錄
        time.sleep(2)
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkAll"))
        ).click() 
        driver.execute_script("executing(8);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "此動作將清除學員在此試卷中所填的答案以及考試分數" in alert_text:
            print("\033[32m清除作答記錄成功\033[0m")
            alert.accept()
        time.sleep(2)      

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
        time.sleep(2)
        if "COPY" in driver.page_source:
            print("\033[32m取消刪除測驗成功\033[0m")
        else:
            print("\033[31m取消刪除測驗失敗\033[0m")
        time.sleep(2)
        driver.execute_script("executing(3);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定刪除測驗嗎" in alert_text:
            copy = True
            alert.accept()
        else:
            copy = False
            alert.accept()  
        time.sleep(2) 
        if "COPY" not in driver.page_source and copy == True:
            print("\033[32m刪除測驗成功\033[0m")
        else:
            print("\033[31m刪除測驗失敗\033[0m")
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