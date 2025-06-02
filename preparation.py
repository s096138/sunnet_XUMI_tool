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
from pywinauto import Application
from admin_enter import admin_enter
from admin_course_center import admin_course_center
from selenium.webdriver.support.ui import Select
import time
import os
from dotenv import load_dotenv

load_dotenv()

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def preparation(driver):
    try:
        print("測試資料建置")

        # 管理者環境
        admin_enter(driver)
        time.sleep(2)

        # 新增帳號(無須審核)
        # 學生/學生/講師/助教/管理者&教師
        all_account = """
        yqi,A12345
        yyytest,A12345
        MUMUMU
        didi
        joy03
        """
        formatted_accounts = '\n'.join([line.strip() for line in all_account.strip().split('\n')])
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'新增帳號')]"))
        ).click()
        time.sleep(2)
        userlist = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='userlist']"))
        )
        userlist.clear()
        userlist.send_keys(formatted_accounts)
        time.sleep(2) 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='create_btn']"))
        ).click()
        print("新增帳號完成")

        # # 設定email
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'查詢人員')]"))
        # ).click()
        # time.sleep(2)
        # keytype = Select(WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "keytype"))
        # ))
        # keytype.select_by_value("account")
        # time.sleep(2)
        # account = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='keyword']"))
        # )
        # account.clear()
        # account.send_keys("yyytest")
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='search_btn']"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='badge']"))
        # ).click()

        # # 新增管理者
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'管理者設定')]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "btn_add_admin"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.visibility_of_element_located((By.ID, "opnName"))
        # ).send_keys('joy09')
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "opnPermit1"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "btn_submit"))
        # ).click()      
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "更新成功" in alert_text:
        #     alert.accept()
        #     print("新增管理者完成")

        # 群組管理
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(),'群組管理')]"))
        ).click()   
        time.sleep(2)      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'nav-link sldebar-link')]//span[contains(text(),'群組管理')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "btn_add"))
        ).click()
        time.sleep(2)
        group_name = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "GPName_Big5"))
        )
        group_name.clear()   
        group_name.send_keys("圖書館系")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "setting_btn"))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_save']"))
        ).click() 
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存成功" in alert_text:
            alert.accept()                 
        print("新增班級群組完成")  

        # 課程設定
        admin_course_center(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="sldebar-nav"]/li[1]/div'))
        ).click()       
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()

        # 新增課程-自動化測試主課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        name.send_keys(course_name)
        status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "status"))
        )
        select = Select(status)
        select.select_by_value("2")
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")
        time.sleep(2)
        driver.execute_script("save_step(1)") 
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增課程成功，繼續設定其他內容。" in alert_text:
            alert.accept()
        # time.sleep(2)
        # driver.execute_script("show_page('setup')") 
        # time.sleep(2)
        # driver.execute_script("select_teacher('setTeacherValue');") 
        # teacher = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'keyword'))
        # )
        # teacher.click()
        # teacher.send_keys("joy09")
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[@id="search_btn"]'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '(//input[@id="joy09"])[1]'))
        # ).click()
        # driver.execute_script("ReturnWork()") 
        # time.sleep(2)
        # driver.execute_script("save_step(6);") 
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "修改課程成功" in alert_text:
        #     alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        print(f"新增課程-{course_name}完成")

        # 新增課程-測試課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        name.send_keys("測試課程")
        status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "status"))
        )
        select = Select(status)
        select.select_by_value("2")
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")
        time.sleep(2)
        driver.execute_script("save_step(1)") 
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增課程成功，繼續設定其他內容。" in alert_text:
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        print("新增課程-測試課程完成")

        # 新增課程-課程複製精靈
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        name.send_keys("課程複製精靈")
        status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "status"))
        )
        select = Select(status)
        select.select_by_value("2")
        scroll_bottom(driver)
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")
        time.sleep(2)
        driver.execute_script("save_step(1)") 
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增課程成功，繼續設定其他內容。" in alert_text:
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        print("新增課程-測試課程完成")

        # 新增課程-2026年的課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_addCourse'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'Big5'))
        )
        name.click()
        name.clear()
        name.send_keys("2026年的課程")
        status = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "status"))
        )
        select = Select(status)
        select.select_by_value("2")
        point = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'credit'))
        )
        point.click()
        point.send_keys("2")
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
        scroll_bottom(driver)
        time.sleep(2)  
        driver.execute_script("save_step(1)") 
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "新增課程成功，繼續設定其他內容。" in alert_text:
            alert.accept()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="menu1"]/li[2]/a'))
        ).click()
        print("新增課程-2026年的課程完成")

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