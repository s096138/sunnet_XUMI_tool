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
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

weekday_translation = {
    "Monday": "週一",
    "Tuesday": "週二",
    "Wednesday": "週三",
    "Thursday": "週四",
    "Friday": "週五",
    "Saturday": "週六",
    "Sunday": "週日"
}

months_dict = {
    "一月": 1,
    "二月": 2,
    "三月": 3,
    "四月": 4,
    "五月": 5,
    "六月": 6,
    "七月": 7,
    "八月": 8,
    "九月": 9,
    "十月": 10,
    "十一月": 11,
    "十二月": 12
}

def parse_month_from_calendar_title(title):
    try:
        # 分割標題並取得月份部分
        parts = title.split("年")
        if len(parts) >= 2:
            month_str = parts[1].strip().replace("月", "")
            if month_str.isdigit():
                return int(month_str)  # 如果月份是數字，返回整數
            else:
                print(f"無法解析行事曆的標題：{title}")
                return None
        else:
            print(f"無法解析行事曆的標題：{title}")
            return None
    except Exception as e:
        print(f"解析行事曆標題時發生錯誤：{e}")
        return None
    
def check_last_month(driver, current_month):
    driver.find_element(By.XPATH, "//span[@class='fc-icon fc-icon-chevron-left']").click()
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
    ).text
    new_month = parse_month_from_calendar_title(new_month_text)
    if new_month and current_month > 1 and new_month == current_month - 1:
        return True, new_month  # 成功
    else:
        return False, new_month  # 失敗
    
def check_next_month(driver, current_month):
    driver.find_element(By.XPATH, "//span[@class='fc-icon fc-icon-chevron-right']").click()
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
    ).text
    new_month = parse_month_from_calendar_title(new_month_text)
    if new_month and current_month < 12 and new_month == current_month + 1:
        return True, new_month  # 成功
    else:
        return False, new_month  # 失敗    

def check_current_month(driver, expected_month):
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
    ).text
    new_month = parse_month_from_calendar_title(new_month_text)
    if new_month == expected_month:
        return True, new_month  # 成功
    else:
        print(f"對比失敗，期望月份：{expected_month}，但獲取到的月份為：{new_month}")
        return False, new_month  # 失敗 
    
def test_calendar(driver):
    try:
        print("測試：首頁-會員專區-行事曆")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='行事曆']"))
        ).click()
        time.sleep(2)
        if "新增行事曆" in driver.page_source:
            print("\033[32m進入行事曆成功\033[0m")
        else:
            print("\033[31m進入行事曆失敗\033[0m")

        # 今天
        time.sleep(2)
        today_date = datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD
        today_weekday = datetime.now().strftime("%A") # 星期幾 
        today_weekday_chinese = weekday_translation[today_weekday]     
        date_element = driver.find_element(By.XPATH, "//h3[@class='event-list__date']").text
        expected_text = f"{today_date} {today_weekday_chinese}"
        time.sleep(2)
        if date_element == expected_text:
            print("\033[32m今日日期顯示正確\033[0m")
        else:
            print("\033[31m今天日期顯示錯誤\033[0m", expected_text)

        # 切換月份
        time.sleep(2)
        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
        ).text
        current_month = parse_month_from_calendar_title(current_month_text)
        if current_month is None:
            print("\033[31m無法解析當前月份\033[0m")
            return
        success, new_month = check_last_month(driver, current_month)
        if success:
            print("\033[32m切換上個月成功\033[0m")
        elif new_month and (new_month == 12 or new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) - 1) % 12]):
            print("\033[32m切換上個月成功\033[0m")
        else:
            print("\033[31m切換上個月失敗\033[0m")
        time.sleep(2)

        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
        ).text
        current_month = parse_month_from_calendar_title(current_month_text)
        success, new_month = check_last_month(driver, current_month)
        if success:
            print("\033[32m切換上上個月成功\033[0m")
        elif new_month and (new_month == 12 or new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) - 2) % 12]):
            print("\033[32m切換上上個月成功\033[0m")
        else:
            print("\033[31m切換上上個月失敗\033[0m")
        time.sleep(2)

        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[@class='fc-toolbar-title']"))
        ).text
        current_month = parse_month_from_calendar_title(current_month_text)
        success, new_month = check_next_month(driver, current_month)
        if success:
            print("\033[32m切換下個月成功\033[0m")
        elif (new_month == 1 and current_month == 12) or (new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) + 1) % 12]):
            print("\033[32m切換下個月成功\033[0m")
        else:
            print("\033[31m切換下個月失敗\033[0m")
        time.sleep(2)

        # 檢查當前月份是否是今天
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'今天')]"))
        ).click()
        current_month_num = datetime.now().month
        success, new_month = check_current_month(driver, current_month_num)
        if success:
            print("\033[32m切換今天成功\033[0m")
        else:
            print("\033[31m切換今天失敗\033[0m")
        time.sleep(2)

        # 新增行事曆
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增行事曆')]"))
        ).click()  

        # 單一事件 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open calendar'])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'28')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@formcontrolname="begin_time_hi"]'))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="9"]'))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="AM"]'))
        ).click()      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="OK"]'))
        ).click() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@formcontrolname="end_time_hi"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="6"]'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="PM"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="OK"]'))
        ).click()  
        time.sleep(2)    
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        )  
        subject.click()
        subject.send_keys("自動化單一事件")
        description = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='calendar-description']"))
        )  
        description.click()
        description.send_keys("自動化單一事件")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 
        # 查看
        time.sleep(2)
        if "自動化單一事件" in driver.page_source:
            print("\033[32m新增單一事件成功\033[0m")
        else:
            print("\033[31m新增單一事件失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//a[normalize-space()="28"])[1]'))
        ).click() 
        if "來自個人通知" in driver.page_source and "自動化單一事件" in driver.page_source:
            print("\033[32m右側列表正確顯示事件資訊\033[0m")
        else:
            print("\033[31m右側列表未正確顯示事件資訊\033[0m")  

        # 編輯
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="note__icon-action"]'))
        ).click() 
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        )  
        subject.clear()
        subject.click()
        subject.send_keys("自動化編輯")
        description = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//textarea[@id="calendar-description"]'))
        )  
        description.clear()
        description.click()
        description.send_keys("自動化編輯")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 
        time.sleep(2)
        if "自動化編輯" in driver.page_source:
            print("\033[32m編輯單一事件成功\033[0m")
        else:
            print("\033[31m編輯單一事件失敗\033[0m")

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="note__icon-action note__remove"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 
        time.sleep(2)
        driver.refresh()
        if "自動化編輯" not in driver.page_source:
            print("\033[32m刪除單一事件成功\033[0m")
        else:
            print("\033[31m刪除單一事件失敗\033[0m")

        # 新增行事曆
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增行事曆')]"))
        ).click()  

        #週期事件
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'週期事件')]"))
        ).click() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open calendar'])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'27')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@formcontrolname="begin_time_hi"]'))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="9"]'))
        ).click()  
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="AM"]'))
        ).click()      
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="OK"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@aria-label='Open calendar'])[2]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'28')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@formcontrolname="end_time_hi"]'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="6"]'))
        ).click()   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[normalize-space()="PM"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="OK"]'))
        ).click()  
        time.sleep(2)    
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        )  
        subject.click()
        subject.send_keys("自動化測試週期事件")
        description = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='calendar-description']"))
        )  
        description.click()
        description.send_keys("自動化測試週期事件")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        ).click() 
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 

        # 查看
        time.sleep(2)
        if "自動化測試週期事件" in driver.page_source:
            print("\033[32m新增週期事件成功\033[0m")
        else:
            print("\033[31m新增週期事件失敗\033[0m")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//a[normalize-space()="28"])[1]'))
        ).click() 
        if "來自個人通知" in driver.page_source and "自動化測試週期事件" in driver.page_source:
            print("\033[32m右側列表正確顯示事件資訊\033[0m")
        else:
            print("\033[31m右側列表未正確顯示事件資訊\033[0m")

        # 編輯
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='鉛筆圖示']"))
        ).click() 
        time.sleep(2)
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        )  
        subject.click()
        subject.send_keys("自動化編輯週期事件")
        description = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='calendar-description']"))
        )  
        description.click()
        description.send_keys("自動化編輯週期事件")       
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@id="calendar-subject"]'))
        ).click() 
        WebDriverWait(driver, 10).until(    
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 
        time.sleep(2)
        if "自動化編輯週期事件" in driver.page_source:
            print("\033[32m編輯週期事件成功\033[0m")
        else:
            print("\033[31m編輯週期事件失敗\033[0m")

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="note__icon-action note__remove"]'))
        ).click() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//span[contains(text(),"確定")]'))
        ).click() 
        time.sleep(2)
        driver.refresh()
        if "自動化測試週期事件" not in driver.page_source:
            print("\033[32m刪除週期事件成功\033[0m")
        else:
            print("\033[31m刪除週期事件失敗\033[0m")

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