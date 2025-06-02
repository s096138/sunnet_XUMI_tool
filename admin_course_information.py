from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException,
    UnexpectedAlertPresentException
)
from menu_expanded import menu_expanded
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import Select
from pywinauto import Application
from datetime import datetime
import time

def scroll_top(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0,0);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def admin_course_information(driver):
    try:
        print("測試：管理者環境-課程管理-課程設定(課程資訊)")  
        menu_expanded(driver, "課程管理", "課程設定")
        time.sleep(2)
        if "新增課程" in driver.page_source:
            print("\033[32m進入課程設定成功\033[0m")
        else:
            print("\033[31m進入課程設定失敗\033[0m")

        # 新增課程-------------------------------
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()

        # 課程名稱
        time.sleep(2)
        driver.execute_script("save_step(1)")      
        if "課程名稱必填" in driver.page_source:
            print("\033[32m課程名稱有檢驗必填\033[0m")
        else:
            print("\033[32m課程名稱沒有檢驗必填\033[0m")
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.send_keys("自動化測試用")

        # 報名期間
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check"]//input[@name="en_option"]'))
        ).click() 
        time.sleep(2)
        en_begin = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="saveForm1"]/fieldset[1]/div/div[3]/button'))
        )
        en_begin.click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="28"]'))
        ).click()    
        time.sleep(2)   
        en_end = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="saveForm1"]/fieldset[1]/div/div[4]/button'))
        )
        en_end.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="1"]'))
        ).click() 
        time.sleep(2)  
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "結束時間不可小於開始時間" in alert_text:
            alert.accept()
            print("\033[32m報名結束時間不可小於開始時間\033[0m")
        else:
            alert.accept()  
            print("\033[31m報名結束時間可以小於開始時間\033[0m")
                 
        # 上課期間
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check"]//input[@name="st_option"]'))
        ).click() 
        st_begin = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="saveForm1"]/fieldset[2]/div[1]/div[3]/button'))
        )
        st_begin.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="28"]'))
        ).click() 
        st_end = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="saveForm1"]/fieldset[2]/div[1]/div[4]/button'))
        )
        st_end.click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[normalize-space()="1"]'))
        ).click() 
        time.sleep(2)  
        alert = driver.switch_to.alert
        alert_text = alert.text        
        if "結束時間不可小於開始時間" in alert_text:
            alert.accept()
            print("\033[32m上課結束時間不可小於開始時間\033[0m")
        else:
            alert.accept()  
            print("\033[31m上課結束時間可以小於開始時間\033[0m")  

        # 學分數
        time.sleep(2)
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.clear()
        driver.execute_script("save_step(1)")      
        if "必需是阿拉伯數字型態" in driver.page_source:
            print("\033[32m學分數有檢驗正整數\033[0m")
        else:
            print("\033[32m學分數沒有檢驗正整數\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")

        # 及格成績
        time.sleep(2)
        scroll_bottom(driver)
        grade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fair_grade'))
        )
        grade.clear()
        driver.execute_script("save_step(1)")      
        if "必需是阿拉伯數字型態" in driver.page_source:
            print("\033[32m及格成績有檢驗正整數\033[0m")
        else:
            print("\033[32m及格成績沒有檢驗正整數\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        grade = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'fair_grade'))
        )
        grade.click()
        grade.send_keys("60")
        time.sleep(2)

        # 所屬群組
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'group_affiliation'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click() 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請勾選群組" in alert_text:
            alert.accept()
            print("\033[32m未勾選群組不能加入群組\033[0m")
        else:
            alert.accept() 
            print("\033[31m未勾選群組可以加入群組\033[0m") 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'圖書館系')]"))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click() 
        time.sleep(2)
        if "圖書館系" in driver.page_source:
            print("\033[32m課程加入群組成功\033[0m")
        else:
            print("\033[31m課程加入群組失敗\033[0m")

        # # 課程代表圖
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check"]//input[@name="course_picture"]'))
        # ).click()    
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//div[@class="upload-div d-flex flex-column mt-3 p-3"]//label[@class="text-center p-4"]'))
        # ).click() 
        # time.sleep(5)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(2)

        # 確定新增
        driver.execute_script("save_step(1)") 
        time.sleep(2)
        alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert_text = alert.text
        if "新增課程成功" in alert_text:
            print("\033[32m新增課程成功\033[0m")
        else:
            print("\033[31m新增課程失敗\033[0m")
        alert.accept()
        
        # 課程介紹
        print("測試：管理者環境-課程管理-課程設定(課程介紹)") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="intro-tab"]'))
        ).click()  

        # 影片介紹 
        time.sleep(2)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="video-file"]/div/label/p[1]/span'))
        ).click() 
        time.sleep(5)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)

        # # 影片網址
        scroll_bottom(driver)
        # youtubeUrl = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'youtubeUrl'))
        # )
        # youtubeUrl.clear()
        # youtubeUrl.send_keys("https://www.youtube.com/live/jfKfPfyJRdk?si=UGMKMVJmMJf8XR24")
        # time.sleep(2)

        # 課程簡介
        time.sleep(2)
        textarea = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "content"))
        )
        textarea.clear()
        textarea.send_keys("自動化測試簡介用")

        # 下一步
        time.sleep(2) 
        driver.execute_script("save_step(2)")    
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            print("\033[32m儲存修改成功\033[0m")
        else:
            print("\033[31m儲存修改失敗\033[0m")
        alert.accept()
           
        # 驗證
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="intro-tab"]'))
        ).click()  
        time.sleep(2)
        video_element = driver.find_element(By.ID, "videoPreview")
        video_src = video_element.get_attribute("src")
        time.sleep(2)
        if video_src:
            print("\033[32m上傳影片成功\033[0m")
        else:
            print("\033[31m上傳影片失敗\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        # url_element = driver.find_element(By.ID, "youtubeUrl")
        # url_value = url_element.get_attribute("value").strip()
        # if url_value == "https//www.youtube.com/live/jfKfPfyJRdk?si=UGMKMVJmMJf8XR24": # 不知道為什麼https後面要少一個冒號
        #     print("\033[32m填寫影片網址成功\033[0m")
        # else:
        #     print("\033[31m填寫影片網址失敗\033[0m")
        time.sleep(2) 
        if "自動化測試簡介用" in driver.page_source:
            print("\033[32m填寫課程簡介成功\033[0m")
        else:
            print("\033[31m填寫課程簡介失敗\033[0m")


        # 權限設定
        print("測試：管理者環境-課程管理-課程設定(權限設定)") 
        driver.refresh()
        scroll_top(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click() 

        # 教師
        time.sleep(2)
        driver.execute_script("select_teacher('setTeacherValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("yyy") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="yyytest"]'))
        ).click() 
        driver.execute_script("ReturnWork()") 
        time.sleep(2)
        if "yyytest" in driver.page_source:
            print("\033[32m新增教師成功\033[0m")
        else:
            print("\033[31m新增教師失敗\033[0m")

        # 講師
        time.sleep(2)
        driver.execute_script("select_teacher('setInstructorValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("yyy") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="yyytest"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號yyytest已存在於教師名單中" in alert_text:
            print("\033[32m教師名單不可重複\033[0m")
        else:
            print("\033[31m教師名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("MUMU") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="MUMUMU"]'))
        ).click() 
        driver.execute_script("ReturnWork()")
        time.sleep(2)
        if "MUMUMU" in driver.page_source:
            print("\033[32m新增講師成功\033[0m")
        else:
            print("\033[31m新增講師失敗\033[0m")

        # 助教
        time.sleep(2)
        driver.execute_script("select_teacher('setAssistantValue')") 
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.click()
        keyword.send_keys("MU") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="MUMUMU"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號MUMUMU已存在於講師名單中" in alert_text:
            print("\033[32m講師名單不可重複\033[0m")
        else:
            print("\033[31m講師名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("didi") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="didi"]'))
        ).click() 
        driver.execute_script("ReturnWork()")
        time.sleep(2)
        if "didi" in driver.page_source:
            print("\033[32m新增助教成功\033[0m")
        else:
            print("\033[31m新增助教失敗\033[0m")  

        # 重複
        time.sleep(2)
        driver.execute_script("select_teacher('setTeacherValue')") 
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'keyword'))
        )
        keyword.clear()
        keyword.send_keys("didi") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="didi"]'))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "帳號didi已存在於助教名單中" in alert_text:
            print("\033[32m助教名單不可重複\033[0m")
        else:
            print("\033[31m助教名單可以重複\033[0m")
        alert.accept()
        time.sleep(2)
        driver.execute_script("ReturnWork()")
        
        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_yyytest"]/span'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_MUMUMU"]/span'))
        ).click()         
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="teach_didi"]/span'))
        ).click() 
        driver.execute_script("save_step(6)")
        time.sleep(2)   
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功" in alert_text:
            print("\033[32m儲存修改成功\033[0m")
        else:
            print("\033[31m儲存修改失敗\033[0m")
        alert.accept()
        time.sleep(2)  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[@id="setup-tab"]'))
        ).click()   
        if "yyytest" not in driver.page_source:
            print("\033[32m刪除教師成功\033[0m")
        else:
            print("\033[31m刪除教師失敗\033[0m")
        time.sleep(2)
        if "MUMUMU" not in driver.page_source:
            print("\033[32m刪除講師成功\033[0m")
        else:
            print("\033[31m刪除講師失敗\033[0m")
        time.sleep(2)
        if "didi" not in driver.page_source:
            print("\033[32m刪除講師成功\033[0m")
        else:
            print("\033[31m刪除講師失敗\033[0m")

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