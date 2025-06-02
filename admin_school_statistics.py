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
from pywinauto import Application
import time
import random
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

nowdatetime = datetime.now().strftime("%Y-%m-%d")
nowmonth = datetime.now().strftime("%Y-%m")
nowyear = datetime.now().strftime("%Y")

def admin_school_statistics(driver):
    try:
        print("測試：管理者環境-平台管理-平台統計資料") 
        menu_expanded(driver, "平台管理", "平台統計資料")
        time.sleep(2)
        if "開課統計" in driver.page_source:
            print("\033[32m進入平台統計資料成功\033[0m")
        else:
            print("\033[31m進入平台統計資料失敗\033[0m")

        # 開課統計------------------------------------
        # 目前課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"開課統計")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click()
        time.sleep(2)
        if "統計結果" in driver.page_source:    
            print("\033[32m搜尋開課統計(正在上課中)成功\033[0m")
        else:
            print("\033[31m搜尋開課統計(正在上課中)失敗\033[0m")
        # 週報表
        week1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'en_begin_date'))
        )
        week1.click()
        week1.clear()
        week1.send_keys(f"{nowmonth}-01")
        week2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'en_end_date'))
        )   
        week2.click()
        week2.clear()
        week2.send_keys(f"{nowmonth}-31")     
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report2'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "開課統計 - 週報表" in driver.page_source:
            print("\033[32m搜尋開課統計(週報表)成功\033[0m")
        else:
            print("\033[31m搜尋開課統計(週報表)失敗\033[0m")
        # 月報表
        time.sleep(2)
        month_y1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'month_year'))
        )
        select_y1 = Select(month_y1)
        select_y1.select_by_value(nowyear)
        month_m1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'month'))
        )
        select_m1 = Select(month_m1)
        choice = ["1","2","3","4","5","6","7","8","9","10","11","12",]
        random_choice = random.choice(choice)
        select_m1.select_by_value(random_choice)
        month_y2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'month_year1'))
        )   
        select_y2 = Select(month_y2)
        select_y2.select_by_value(nowyear)
        month_m2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'month1'))
        )
        select_m2 = Select(month_m2)
        random_choice = random.choice(choice)
        select_m2.select_by_value(random_choice)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report3'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "開課統計 - 月報表" in driver.page_source:
            print("\033[32m搜尋開課統計(月報表)成功\033[0m")
        else:
            print("\033[31m搜尋開課統計(月報表)失敗\033[0m")
        # 年報表
        time.sleep(2)
        year1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'year_year'))
        )
        select = Select(year1)
        select.select_by_value(nowyear)
        year2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'year_year1'))
        )   
        select = Select(year2)
        select.select_by_value(nowyear)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report4'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "開課統計 - 年報表" in driver.page_source:
            print("\033[32m搜尋開課統計(年報表)成功\033[0m")
        else:
            print("\033[31m搜尋開課統計(年報表)失敗\033[0m")

        # 登入次數統計------------------------------------        
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"登入次數統計")]'))
        ).click()
        # 單日報表
        oneday = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'single_day'))
        )          
        oneday.click()
        oneday.clear()
        oneday.send_keys(nowdatetime) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click()
        time.sleep(2)
        if "平台人次統計報表 - 單日報表" in driver.page_source:
            print("\033[32m搜尋登入次數統計(單日報表)成功\033[0m")
        else:
            print("\033[31m搜尋登入次數統計(單日報表)失敗\033[0m")
        # 日報表
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'daily_from_date'))
        )          
        day1.click()
        day1.clear()
        day1.send_keys(nowdatetime) 
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'daily_over_date'))
        )          
        day2.click()
        day2.clear()
        day2.send_keys(nowdatetime) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report5'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click()
        time.sleep(2)
        if "平台人次統計報表 - 日報表" in driver.page_source:
            print("\033[32m搜尋登入次數統計(日報表)成功\033[0m")
        else:
            print("\033[31m搜尋登入次數統計(日報表)失敗\033[0m")
        # 週報表
        time.sleep(2)
        week1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'en_begin_date'))
        )
        week1.click()
        week1.clear()
        week1.send_keys(nowdatetime)
        week2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'en_end_date'))
        )   
        week2.click()
        week2.clear()
        week2.send_keys(nowdatetime)     
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report2'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "平台人次統計報表 - 週報表" in driver.page_source:
            print("\033[32m搜尋登入次數統計(週報表)成功\033[0m")
        else:
            print("\033[31m搜尋登入次數統計(週報表)失敗\033[0m")
        # 月報表
        time.sleep(2)
        month_y1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'month_year'))
        )
        select_y1 = Select(month_y1)
        select_y1.select_by_value(nowyear)
        month_m1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'month'))
        )
        select_m1 = Select(month_m1)
        choice = ["1","2","3","4","5","6","7","8","9","10","11","12",]
        random_choice = random.choice(choice)
        select_m1.select_by_value(random_choice)
        month_y2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'month_year1'))
        )   
        select_y2 = Select(month_y2)
        select_y2.select_by_value(nowyear)
        month_m2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'month1'))
        )
        select_m2 = Select(month_m2)
        random_choice = random.choice(choice)
        select_m2.select_by_value(random_choice)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report3'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "平台人次統計報表 - 月報表" in driver.page_source:
            print("\033[32m搜尋登入次數統計(月報表)成功\033[0m")
        else:
            print("\033[31m搜尋登入次數統計(月報表)失敗\033[0m")
        # 年報表
        time.sleep(2)
        year1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'year_year'))
        )
        select = Select(year1)
        select.select_by_value(nowyear)
        year2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'year_year1'))
        )   
        select = Select(year2)
        select.select_by_value(nowyear)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'type_report4'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "平台人次統計報表 - 年報表" in driver.page_source:
            print("\033[32m搜尋登入次數統計(年報表)成功\033[0m")
        else:
            print("\033[31m搜尋登入次數統計(年報表)失敗\033[0m")

        # 上課次數統計------------------------------------
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"上課次數統計")]'))
        ).click() 
        # 學校所有課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "上課次數統計報表 - 單日報表" in driver.page_source:
            print("\033[32m搜尋上課次數統計(所有課程)成功\033[0m")
        else:
            print("\033[31m搜尋上課次數統計(所有課程)失敗\033[0m")          
        # 某個課程群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check pe-5 d-flex pb-1"]//input[@name="ck_course_rang"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'group_affiliation'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[normalize-space()="圖書館系"]'))
        ).click()    
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click()                                 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "上課次數統計報表 - 單日報表" in driver.page_source:
            print("\033[32m搜尋上課次數統計(指定群組)成功\033[0m")
        else:
            print("\033[31m搜尋上課次數統計(指定群組)失敗\033[0m")
        # 某個課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[1]/div[2]/div/div[3]/div/input[1]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check pe-5 pb-1"]//button[@id="group_affiliation"]'))
        ).click()   
        # 找到對應的 text-start 元素
        text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'td.text-start'))
        )
        data_name = text_element.text
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'input.form-check-input.wm6_radio[data-name="{data_name}"]'))
        ).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_course_submit'))
        ).click()                                 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "上課次數統計報表 - 單日報表" in driver.page_source:
            print("\033[32m搜尋上課次數統計(指定課程)成功\033[0m")
        else:
            print("\033[31m搜尋上課次數統計(指定課程)失敗\033[0m")
        # 使用者人數統計------------------------------------
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"使用者人數統計")]'))
        ).click()
        # 學校所有課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2) 
        if "性別比例" in driver.page_source and "課程角色比例" in driver.page_source:
            print("\033[32m搜尋使用者人數統計(所有課程)成功\033[0m")
        else:
            print("\033[31m搜尋使用者人數統計(所有課程)失敗\033[0m")         
        # 某個課程群組
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="2"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'group_affiliation'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[normalize-space()="圖書館系"]'))
        ).click()  
        time.sleep(5)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click()                                 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2) 
        if "性別比例" in driver.page_source and "課程角色比例" in driver.page_source:
            print("\033[32m搜尋使用者人數統計(指定群組)成功\033[0m")
        else:
            print("\033[31m搜尋使用者人數統計(指定群組)失敗\033[0m")  
        # 某個課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="3"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="form-check pe-5 pb-1"]//button[@id="group_affiliation"]'))
        ).click()   
        # 找到對應的 text-start 元素
        text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'td.text-start'))
        )
        data_name = text_element.text
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'input.form-check-input.wm6_radio[data-name="{data_name}"]'))
        ).click()
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_course_submit'))
        ).click()                                 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'save_btn'))
        ).click() 
        time.sleep(2)
        if "性別比例" in driver.page_source and "課程角色比例" in driver.page_source:
            print("\033[32m搜尋使用者人數統計(指定課程)成功\033[0m")
        else:
            print("\033[31m搜尋使用者人數統計(指定課程)失敗\033[0m")  
        # 教材閱讀統計------------------------------------
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"教材閱讀統計")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'lastBtn1'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請點選一門課程" in alert_text:
            print("\033[32m未選課程不可以查詢\033[0m")
        else:
            print("\033[31m未選課程可以查詢\033[0m")  
        alert.accept()
        time.sleep(2)
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//tr[td[contains(text(), '{course_name}')]]//input[@type='radio']"))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'lastBtn1'))
        ).click()   
        time.sleep(2)
        if "閱讀時數" in driver.page_source and "平均時數" in driver.page_source:
            print("\033[32m查詢教材閱讀紀錄成功\033[0m")
        else:
            print("\033[31m查詢教材閱讀紀錄失敗\033[0m")   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"回上頁")]'))
        ).click()   
        time.sleep(2) 
        coursename = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'cour_name'))
        ) 
        coursename.click()
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        coursename.send_keys(course_name) 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()    
        time.sleep(2)
        course_name = os.getenv('TEST_COURSE_NAME')
        # print(f"環境變數 TEST_COURSE_NAME: {course_name}")
        if course_name in driver.page_source:
            print("\033[32m課程名稱搜尋成功\033[0m")
        else:
            print("\033[31m課程名稱搜尋失敗\033[0m") 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"教材閱讀統計")]'))
        ).click()
        # 每頁數量 
        time.sleep(2)
        page_num = driver.find_element(By.ID, "page_num")
        page_num.click()
        select = Select(page_num)
        options = {"每頁10筆":10, "每頁20筆":20, "每頁50筆":50}
        random_option_text = random.choice(list(options.keys()))
        random_option_number = options[random_option_text]
        select.select_by_visible_text(random_option_text)
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
        tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        print(len(tr_elements))
        if len(tr_elements) == random_option_number+7:
            print("\033[32m每頁顯示數量正確\033[0m")
        else:
            print("\033[31m每頁顯示數量不正確\033[0m")
        # Userlog統計------------------------------------
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"User log 統計")]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請填寫至少一項查詢條件" in alert_text:
            print("\033[32m未填條件不可搜尋\033[0m")
        else:
            print("\033[31m未填條件可以搜尋\033[0m")
        alert.accept()
        time.sleep(2)
        functionid = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'function_id'))
        ) 
        functionid.click()
        functionid.send_keys("2500100200") 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()
        time.sleep(2)
        if "進入教室" in driver.page_source:
            print("\033[32m功能編號搜尋成功\033[0m")
        else:
            print("\033[31m功能編號搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"清除篩選條件")]'))
        ).click()
        if "進入教室" not in driver.page_source:
            print("\033[32m清除篩選條件成功\033[0m")
        else:
            print("\033[31m清除篩選條件失敗\033[0m")

        # 硬碟空間使用率------------------------------------
        time.sleep(2)
        # 檢查硬碟空間使用率按鈕是否存在
        elements = driver.find_elements(By.XPATH, '//a[contains(text(),"硬碟空間使用率")]')
        time.sleep(2)
        if elements:  # 如果元素存在

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"硬碟空間使用率")]'))
            ).click()
        else:  # 如果元素不存在，先點擊箭頭按鈕
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="arrow_forward_ios"]'))
            ).click()
            time.sleep(2)
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//a[contains(text(),"硬碟空間使用率")]'))
            ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_list_btn'))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請選擇課程群組" in alert_text:
            print("\033[32m未選擇課程群組不可查詢\033[0m")
        else:
            print("\033[31m未選擇課程群組可以查詢\033[0m")
        alert.accept()
        time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//input[@value="1"]'))
        # ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"選擇群組")]'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//label[normalize-space()="圖書館系"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_submit'))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_list_btn'))
        ).click()  
        time.sleep(2)
        if "自動化測試" in driver.page_source:
            print("\033[32m查詢指定群組硬碟空間使用率成功\033[0m")
        else:
            print("\033[31m查詢指定群組硬碟空間使用率失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@class="col-sm-10"]//div[1]//div[1]//input[1]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"選擇課程")]'))
        ).click()   
        # 找到對應的 text-start 元素
        text_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.modal-content .modal-body .wm6-scrollbar td.text-start'))
        )
        print(text_element)
        data_name = text_element.text
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'input.form-check-input.wm6_radio[data-name="{data_name}"]'))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_course_submit'))
        ).click() 
        time.sleep(5)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="2"][name="single_all"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'search_btn'))
        ).click()  
        time.sleep(2)
        if data_name in driver.page_source:
            print("\033[32m查詢指定課程硬碟空間使用率成功\033[0m")
        else:
            print("\033[31m查詢指定課程硬碟空間使用率失敗\033[0m")

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