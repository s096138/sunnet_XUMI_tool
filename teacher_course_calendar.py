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
from datetime import datetime
import time

nowdatetime = datetime.now().strftime("%Y-%m")

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

def check_last_month(driver, current_month):
    current_month_index = list(months_dict.keys()).index(current_month)
    driver.find_element(By.XPATH, "//span[@class='fc-icon fc-icon-left-single-arrow']").click()
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    ).text
    new_month = new_month_text.split(" ")[1]
    if current_month_index > 0 and new_month == list(months_dict.keys())[current_month_index - 1]:
        return True, new_month  # 成功
    else:
        return False, new_month  # 失敗
    
def check_next_month(driver, current_month):
    current_month_index = list(months_dict.keys()).index(current_month)
    driver.find_element(By.XPATH, "//span[@class='fc-icon fc-icon-right-single-arrow']").click()
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    ).text
    new_month = new_month_text.split(" ")[1]
    if current_month_index > 0 and new_month == list(months_dict.keys())[current_month_index + 1]:
        return True, new_month  # 成功
    else:
        return False, new_month  # 失敗   

def check_current_month(driver, expected_month):
    new_month_text = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h2"))
    ).text
    new_month = new_month_text.split(" ")[1].strip()
    if new_month == expected_month:
        return True, new_month  # 成功
    else:
        print(f"對比失敗，期望月份：{expected_month}，但獲取到的月份為：{new_month}")
        return False, new_month  # 失敗 

def teacher_course_calendar(driver):
    try:
        print("測試：辦公室-教室管理-課程行事曆")
        menu_expanded(driver, "教室管理", "課程行事曆")
        time.sleep(2)
        if "新增行事曆" in driver.page_source:
            print("\033[32m進入課程行事曆成功\033[0m")
        else:
            print("\033[31m進入課程行事曆失敗\033[0m") 

        # 切換月份
        time.sleep(2)
        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2"))
        ).text
        current_month = current_month_text.split(" ")[1]  # 假設格式為 "2024年 七月"
        success, new_month = check_last_month(driver, current_month)
        if success:
            print("\033[32m切換上個月成功\033[0m")
        elif new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) - 1) % 12]:
            print("\033[32m切換上個月成功\033[0m")
        else:
            print("\033[31m切換上個月失敗\033[0m")
        time.sleep(2)

        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2"))
        ).text
        current_month = current_month_text.split(" ")[1]  # 假設格式為 "2024年 七月"
        success, new_month = check_last_month(driver, current_month)
        if success:
            print("\033[32m切換上上個月成功\033[0m")
        elif new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) - 2) % 12]:
            print("\033[32m切換上上個月成功\033[0m")
        else:
            print("\033[31m切換上上個月失敗\033[0m")
            
        time.sleep(2)
        current_month_num = datetime.now().month
        current_month_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2"))
        ).text
        current_month = current_month_text.split(" ")[1]  # 假設格式為 "2024年 七月"
        success, new_month = check_next_month(driver, current_month)
        if success:
            print("\033[32m切換下個月成功\033[0m")
        elif new_month == list(months_dict.keys())[(list(months_dict.keys()).index(current_month) + 1) % 12]:
            print("\033[32m切換下個月成功\033[0m")
        else:
            print("\033[31m切換下個月失敗\033[0m")
        time.sleep(2)

        current_month_num = datetime.now().month
        # print(f"系統當前月份數字為: {current_month_num} (類型: {type(current_month_num)})")
        expected_month = None
        for month_name, month_num in months_dict.items():
            # print(f"正在檢查字典：{month_name} 對應 {month_num} (類型: {type(month_num)})")
            if month_num == current_month_num:
                expected_month = month_name
            else:
                # print(f"沒有匹配到：系統當前月份 {current_month_num} 與 {month_num} 不一致")
                pass
        if expected_month is None:
            print(f"錯誤：系統月份 {current_month_num} 無法匹配到字典中的中文月份！")
        else:
            pass
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'今天')]"))
        ).click()
        success, new_month = check_current_month(driver, expected_month)
        if success:
            print("\033[32m切換今天成功\033[0m")
        else:
            print("\033[31m切換今天失敗\033[0m")
        time.sleep(2)

        # 新增全天單一事件
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-add-calendar']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='toggleSwitch']"))
        ).click()
        date = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='memo_repeat_date']"))
        )
        date.click()
        date.send_keys(f"{nowdatetime}-10")  
        time.sleep(2)
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='subject']"))
        )
        subject.click()
        subject.clear()
        subject.send_keys("自動化測試全天單一事件")
        content = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='content']"))
        )
        content.click()
        content.clear()
        content.send_keys("自動化測試用")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'確定')])[1]"))
        ).click()
        time.sleep(2)
        if "自動化測試全天單一事件" in driver.page_source:
            print("\033[32m新增全天單一事件成功\033[0m")
        else:
            print("\033[31m新增全天單一事件失敗\033[0m")

        # 新增全天週期事件
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-add-calendar']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='repeat_choice'])[2]"))
        ).click()        
        time.sleep(2)
        date1 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='memo_repeat_date']"))
        )
        date1.click()
        date1.send_keys(f"{nowdatetime}-01") 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='toggleSwitch']"))
        ).click()
        date2 = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='memo_repeat_end']"))
        )
        date2.click()
        date2.send_keys(f"{nowdatetime}-15")   
        # repeat_frequency = Select(driver.find_element(By.ID, "repeat_frequency"))
        # repeat_frequency.select_by_value("day")  
         
        subject = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='subject']"))
        )
        subject.click()
        subject.clear()
        subject.send_keys("自動化測試全天週期事件")
        content = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@name='content']"))
        )
        content.click()
        content.clear()
        content.send_keys("自動化測試用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'確定')])[1]"))
        ).click()
        time.sleep(2)
        if "自動化測試全天週期事件" in driver.page_source:
            print("\033[32m新增全天週期事件成功\033[0m")
        else:
            print("\033[31m新增全天週期事件失敗\033[0m")

        # # 新增非全天單一事件
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-add-calendar']"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'非全天')]"))
        # ).click()
        # time.sleep(2)
        # begin = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='timeinput pull-left']//input[@name='time_begin']"))
        # )
        # begin.click()
        # begin.clear()
        # begin.send_keys("09:00")
        # end = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@class='timeinput pull-left']//input[@name='time_end']"))
        # )
        # end.click()
        # end.clear()
        # end.send_keys("自動化測試用")        
        # subject = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='subject']"))
        # )
        # subject.click()
        # subject.clear()
        # subject.send_keys("自動化測試用")
        # content = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//textarea[@name='content']"))
        # )
        # content.click()
        # content.clear()
        # content.send_keys("自動化測試用")
        # time.sleep(2)
        # if "自動化測試用" in driver.page_source:
        #     print("\033[32m新增非全天單一事件成功\033[0m")
        # else:
        #     print("\033[31m新增非全天單一事件失敗\033[0m")

        # 刪除全天單一事件
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試全天單一事件')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'刪除')])[1]"))
        ).click()                 
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        if "自動化測試全天單一事件" not in driver.page_source:
            print("\033[32m刪除全天單一事件成功\033[0m")
        else:
            print("\033[31m刪除全天單一事件失敗\033[0m")

        # 刪除全天週期事件
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), '自動化測試全天週期事件')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'刪除')])[1]"))
        ).click()                 
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
        if "自動化測試全天週期事件" not in driver.page_source:
            print("\033[32m刪除全天週期事件成功\033[0m")
        else:
            print("\033[31m刪除全天週期事件失敗\033[0m")

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