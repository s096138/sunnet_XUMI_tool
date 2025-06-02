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
    WebDriverException,
    NoAlertPresentException
)
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from admin_enter import admin_enter
from teacher_enter import teacher_enter
from admin_course_center import admin_course_center
from menu_expanded import menu_expanded
import random
import time

def add_course(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@alt="數位學習平台logo"]'))
    ).click()
    time.sleep(2)
    admin_enter(driver)
    admin_course_center(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sldebar-nav"]/li[1]/div'))
    ).click()       
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
    ).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
    ).click()
    name = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'Big5'))
    )
    name.clear()
    name.send_keys("自動化測試複製用")
    point = WebDriverWait(driver, 10).until(
         EC.element_to_be_clickable((By.ID, 'credit'))
    )
    point.click()
    point.send_keys("2")
    driver.execute_script("save_step(1)") 
    time.sleep(2)     
    alert = driver.switch_to.alert
    alert_text = alert.text
    if "新增課程成功，繼續設定其他內容。" in alert_text:
        print("\033[32m新增課程成功\033[0m")
        alert.accept()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@alt="數位學習平台logo"]'))
    ).click()
    time.sleep(2)
    teacher_enter(driver)

def delect_course(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@alt="數位學習平台logo"]'))
    ).click()
    time.sleep(2)
    admin_enter(driver)
    admin_course_center(driver)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="sldebar-nav"]/li[1]/div'))
    ).click()       
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
    ).click()
    time.sleep(2)
    keyword = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'keyword'))
    )
    keyword.click()
    keyword.send_keys("自動化測試")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'search_btn'))
    ).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '#checkAll'))
    ).click()     
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'btn_delCourse'))
    ).click()
    time.sleep(2) 
    alert = driver.switch_to.alert
    alert_text = alert.text
    if "你確定要刪除嗎？" in alert_text:
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "刪除成功！" in alert_text:
            print("\033[32m刪除課程成功\033[0m")
            alert.accept()               
        else:
            print("\033[32m刪除課程失敗\033[0m")
            alert.accept()

    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@alt="數位學習平台logo"]'))
    ).click()
    time.sleep(2)
    teacher_enter(driver)

def teacher_course_copy(driver):
    try:
        print("測試：辦公室-課程管理-課程複製精靈")
        add_course(driver)

        # 選擇課程
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='selcourse']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("自動化測試複製用")

        # 進入
        menu_expanded(driver, "課程管理", "課程複製精靈")   
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請注意" in alert_text:
            print("\033[32m進入課程複製精靈成功\033[0m")
        else:
            print("\033[31m進入課程複製精靈失敗\033[0m")   
        alert.accept()

        # 來源課程
        time.sleep(2)
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='course_id']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("課程複製精靈")    

        # 複製內容
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'議題討論區,不含文章資料')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'課程討論區/課程公告板,含文章資料')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'作業 (含題目夾檔)，不含學員繳交資料')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'測驗 (含題目夾檔)，不含學員繳交資料')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'問卷 (含題目夾檔)，不含學員繳交資料')]"))
        ).click()

        # 開始匯入
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='submitbtn']"))
        ).click()        
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "課程複製將由[課程複製精靈 ]複製到[自動化測試複製用]" in alert_text:
            print("課程複製將由[課程複製精靈]複製到[自動化測試複製用]")
        else:
            print(f"{alert_text}")   
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "匯入完成" in alert_text:
            print("\033[32m課程複製精靈匯入完成\033[0m")
        else:
            print("\033[31m課程複製精靈匯入失敗\033[0m")   
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請注意" in alert_text:  
            alert.accept()

        # 學習路徑管理
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'學習路徑管理')]"))
        ).click()
        time.sleep(2)
        texts_to_check = [
            "114年辦公日曆表",
            "旭航v4",
            "課程討論區",
            "同步討論室",
            "作業1",
            "測驗1",
            "問卷1"
        ]
        selected_texts = random.sample(texts_to_check, 3)
        for text in selected_texts:
            if text in driver.page_source:
                print(f"\033[32m學習路徑匯入成功({text})\033[0m")
            else:
                print(f"\033[31m學習路徑匯入失敗，缺少{text}\033[0m")
        
        # 回課程複製精靈
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程複製精靈')]"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請注意" in alert_text:
            print("\033[32m進入課程複製精靈成功\033[0m")
        else:
            print("\033[31m進入課程複製精靈失敗\033[0m")   
        alert.accept()

        # 來源課程
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='course_id']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("課程複製精靈")    

        # 複製內容
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'學習路徑的教材節點,包含教材檔案資料')]"))
        ).click()

        # 開始匯入
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='submitbtn']"))
        ).click()        
        time.sleep(2)
        timeout = 10
        for _ in range(timeout):
            try:
                alert = driver.switch_to.alert
                alert.accept()
                break
            except NoAlertPresentException:
                time.sleep(1)
        else:
            pass
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "課程複製將由[課程複製精靈] 複製到[自動化測試複製用]" in alert_text:
            print("課程複製將由[課程複製精靈] 複製到[自動化測試複製用]")
        else:
            print("課程複製將由[課程複製精靈] 複製到[自動化測試複製用]")
            pass  
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "匯入完成" in alert_text:
            print("\033[32m課程複製精靈匯入完成\033[0m")
        else:
            print("\033[31m課程複製精靈匯入失敗\033[0m")   
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請注意" in alert_text:  
            alert.accept()

        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'作業管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'作業維護')]"))
        ).click()
        time.sleep(2)
        if "作業1" in driver.page_source:
            print("\033[32m作業匯入成功\033[0m")
        else:
            print("\033[31m作業匯入失敗\033[0m") 

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'測驗管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'試卷維護')]"))
        ).click()
        time.sleep(2)
        if "測驗1" in driver.page_source:
            print("\033[32m測驗匯入成功\033[0m")
        else:
            print("\033[31m測驗匯入失敗\033[0m") 

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'問卷管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'問卷維護')]"))
        ).click()
        time.sleep(2)
        if "問卷1" in driver.page_source:
            print("\033[32m問卷匯入成功\033[0m")
        else:
            print("\033[31m問卷匯入失敗\033[0m") 
        
        # 復原
        time.sleep(2)
        delect_course(driver)

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