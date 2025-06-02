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
from pywinauto import Application
import langid
import jieba 
import random
import time

traditional_words = set([
    "年", "月", "日", "時間", "日期", "星期", "週", "辦公", "日曆", "表", "行事曆", "計畫",
    "工作", "提醒", "假期", "節日", "休假", "開會", "安排", "備忘錄", "管理", "目標", "進度",
    "規劃", "會議", "任務", "記錄", "通知", "設定", "安排", "日程", "行程", "指派", "報告",
    "確認", "進行", "完成", "審核", "審批", "草稿", "版本", "修改", "分享", "簽署", "審查",
    "組織", "規範", "公告", "日報", "月報", "季報", "年報", "年度", "行動", "事項", "日誌",
    "紀錄", "目錄", "資料", "標記", "責任", "分配", "提交", "檢視", "範圍", "變更"
])

simplified_words = set([
    "年", "月", "日", "时间", "日期", "星期", "周", "办公", "日历", "表", "行事历", "计划",
    "工作", "提醒", "假期", "节日", "休假", "开会", "安排", "备忘录", "管理", "目标", "进度",
    "规划", "会议", "任务", "记录", "通知", "设置", "安排", "日程", "行程", "指派", "报告",
    "确认", "进行", "完成", "审核", "审批", "草稿", "版本", "修改", "分享", "签署", "审查",
    "组织", "规范", "公告", "日报", "月报", "季报", "年报", "年度", "行动", "事项", "日志",
    "记录", "目录", "资料", "标记", "责任", "分配", "提交", "查看", "范围", "变更"
])

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

# def fileupload(driver):
#     WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
#     ).click()
#     WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教材檔案管理')]"))
#     ).click()
#     time.sleep(2)

#     # 上傳檔案
#     WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab04"))
#     ).click()
#     time.sleep(2)
#     file = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='upload[]']"))
#     )
#     driver.execute_script("arguments[0].click();", file)
#     time.sleep(2)
#     app = Application(backend="win32").connect(title_re=".*開啟.*")
#     dlg = app.window(title_re=".*開啟.*")
#     dlg.set_focus()
#     dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
#     time.sleep(2)
#     dlg['開啟'].click()
#     time.sleep(5)
#     WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳']"))
#     ).click()
#     time.sleep(2)
#     if "上傳完成" in driver.page_source:
#         print("\033[32m上傳教材成功\033[0m")
#     else:
#         print("\033[31m上傳教材失敗\033[0m")

def teacher_exam_aiquestion(driver):
    try:
        print("測試：辦公室-測驗管理-AI智能出題")
        # fileupload(driver)
        time.sleep(2)
        menu_expanded(driver, "測驗管理", "AI智能出題")
        time.sleep(2)
        if "../../public/images/robot.png" in driver.page_source:
            print("\033[32m進入AI智能出題成功\033[0m")
        else:
            print("\033[31m進入AI智能出題失敗\033[0m")

        # AI智能出題-step1
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'AI智能出題')]"))
        ).click()  
        time.sleep(2)
        if "請選擇需要AI智能出題的教材內容" in driver.page_source:
            print("第一步：選擇教材")
        else:
            print("\033[31m第一步載入失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='plus-icon']"))
        ).click()    
        time.sleep(2)    
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='file_114年辦公日曆表.pdf']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_submit']"))
        ).click()
        time.sleep(2)
        if "114年辦公日曆表.pdf" in driver.page_source:
            print("\033[32m選擇教材成功\033[0m")
        else:
            print("\033[31m選擇教材失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='next_setting']"))
        ).click()

        # AI智能出題-step2
        time.sleep(2)
        if "總題數" in driver.page_source:
            print("第二步：參數設定")
        else:
            print("\033[31m第二步載入失敗\033[0m")
        time.sleep(2)
        scroll_bottom(driver)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'生成題目')]"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "請選擇題數" in alert_text:
        #     print("\033[32m未設定題數不可生成\033[0m")
        # else:
        #     print("\033[31m未設定題數可以生成\033[0m")   
        # alert.accept() 
        time.sleep(2)
        single = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='single0']"))
        )
        single.clear()
        single.send_keys("1")  
        mulit = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='mulit0']"))
        )
        mulit.clear()
        mulit.send_keys("1")              
        yn = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='yn0']"))
        )
        yn.clear()
        yn.send_keys("1")   
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='description']"))
        ).click()
        time.sleep(2)
        span = driver.find_element(By.XPATH, "//span[@class='total-num']").text.strip()  # 去除空白
        time.sleep(2)
        if span == "3":
            print("\033[32m題數設定成功\033[0m") 
        else:
            print("\033[31m題數設定失敗\033[0m")     
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'生成題目')]"))
        ).click()

        # AI智能出題-step3
        time.sleep(10) # 等待生成
        if "生成題數" in driver.page_source:
            print("第三步：生成結果")
        else:
            print("\033[31m第三步載入失敗\033[0m")    
        time.sleep(2)
        span = driver.find_element(By.XPATH, "//label[@id='total_item_result']//span[@class='total-num']").text.strip()  # 去除空白
        if span == "3":
            print("\033[32m標題題數正確\033[0m")  
        else:
            print("\033[31m標題題數錯誤\033[0m")  
        time.sleep(2)
        bar0 = driver.find_element(By.XPATH, "//div[@id='bar0']").text
        bar1 = driver.find_element(By.XPATH, "//div[@id='bar1']").text
        bar2 = driver.find_element(By.XPATH, "//div[@id='bar2']").text
        bar3 = driver.find_element(By.XPATH, "//div[@id='bar3']").text
        bar4 = driver.find_element(By.XPATH, "//div[@id='bar4']").text
        time.sleep(2)
        if bar0 == "1" and bar1 == "1" and bar2 == "1" and bar3 == "0" and bar4 == "0":
            print("\033[32m題型題數正確\033[0m")  
        else:
            print("\033[31m題型題數錯誤\033[0m") 
        time.sleep(2)
        if "Q3" in driver.page_source and "Q4" not in driver.page_source:
            print("\033[32m生成題數正確\033[0m")
        else:
            print("\033[31m生成題數錯誤\033[0m")  
        time.sleep(2)
        css_selectors = [
            "div[id='single_choice_1'] textarea[name='question']",
            "div[id='multiple_choice_2'] textarea[name='question']",
            "div[id='true_false_3'] textarea[name='question']"
        ]
        chosen_selector = random.choice(css_selectors)
        text = driver.find_element(By.CSS_SELECTOR, chosen_selector).text
        language, _ = langid.classify(text)
        if language == "zh":
            
            words = jieba.cut(text)
            # 計算繁體與簡體的詞頻
            traditional_count = sum(1 for word in words if word in traditional_words)
            simplified_count = sum(1 for word in words if word in simplified_words)
    
            if traditional_count > simplified_count:
                print("\033[32m生成語系正確\033[0m")
            else:
                print("\033[32m生成語系錯誤, zh-cn\033[0m")
        else:
            print(f"\033[31m生成語系錯誤, {language}\033[0m")           
        
        # 加入草題
        scroll_bottom(driver)
        time.sleep(2)
        driver.execute_script("get('3', 'true_or_false')") 
        time.sleep(2)
        driver.execute_script("get('2', 'multiple_choice')") 
        time.sleep(2)       
        driver.execute_script("get('1', 'single_choice')") 

        # 結束
        time.sleep(5)
        if "謝謝您的參與!" in driver.page_source:
            print("\033[32m結束AI智能出題\033[0m")
        else:
            print("\033[31m結束AI智能出題失敗\033[0m")         

        span1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[3]/span").text
        time.sleep(2)
        if span1 == "3":
            print("\033[32m最終生成題數正確\033[0m")
        else:
            print("\033[31m最終生成題數錯誤\033[0m") 
        span2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[4]/span").text           
        time.sleep(2)
        if span2 == "3":
            print("\033[32m加入草題題數正確\033[0m")
        else:
            print("\033[31m加入草題題數錯誤\033[0m") 

        # 前往草題
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'前往草題')]"))
        ).click()         
        time.sleep(2)
        if "2025" in driver.page_source or "114" in driver.page_source:
            print("\033[32m草題檢視成功\033[0m")
        else:
            print("\033[31m草題檢視失敗\033[0m") 

        # 刪掉
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_box0"))
        ).click()  
        driver.execute_script("process(3);")               
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "確定要刪除嗎" in alert_text:
            alert.accept()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert_text = alert.text
            if "刪除完成" in alert_text:
                alert.accept()
                print("\033[32m草題刪除成功\033[0m")
        else:
            print("\033[31m草題刪除失敗\033[0m")  
             
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