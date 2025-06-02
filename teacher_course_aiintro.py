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
import time
import langid
import jieba 
# jieba.set_dictionary("C:/Users/SGQA2/Desktop/Auto/sunnet_WM6/dict.txt.big") # 中文大型字典

traditional_words = set([
    "課程", "前導", "章節", "貓咪", "辦公", "日曆", "表", "教學", "練習", "示例",
    "進度", "學生", "成績", "管理", "資料", "測驗", "操作", "檢查", "進行", "更新",
    "匯入", "匯出", "學習", "紀錄", "編輯", "設定", "結束", "開始", "筆記", "考試",
    "成員", "討論", "互動", "問答", "教案", "連結", "保存", "選擇", "名稱", "目錄",
    "課表", "系統", "成就", "學分", "章節", "日曆", "網頁", "測試", "驗證", "會議",
    "提醒", "提示", "通知", "學期", "計畫", "教育", "學員", "書籍", "教材", "圖書",
    "創建", "刪除", "課堂", "備註", "資料夾", "資料庫", "模擬", "題庫", "選單", "功能",
    "編碼", "音訊", "視頻", "註冊", "系統", "設定", "選項", "清單", "文件"
])

simplified_words = set([
    "课程", "前导", "章节", "猫咪", "办公", "日历", "表", "教学", "练习", "示例",
    "进度", "学生", "成绩", "管理", "资料", "测验", "操作", "检查", "进行", "更新",
    "导入", "导出", "学习", "记录", "编辑", "设置", "结束", "开始", "笔记", "考试",
    "成员", "讨论", "互动", "问答", "教案", "链接", "保存", "选择", "名称", "目录",
    "课程表", "系统", "成就", "学分", "章节", "日历", "网页", "测试", "验证", "会议",
    "提醒", "提示", "通知", "学期", "计划", "教育", "学员", "书籍", "教材", "图书",
    "创建", "删除", "课堂", "备注", "文件夹", "数据库", "模拟", "题库", "菜单", "功能",
    "编码", "音频", "视频", "注册", "系统", "设置", "选项", "清单", "文件"
])

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

def teacher_course_aiintro(driver):
    try:
        print("測試：辦公室-課程管理-課程介紹(AI輔助輸入)")
        menu_expanded(driver, "課程管理", "課程設定")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='intro-tab']"))
        ).click()
        time.sleep(2)
        if "影片介紹" in driver.page_source:
            print("\033[32m進入課程介紹成功\033[0m")
        else:
            print("\033[31m進入課程介紹失敗\033[0m")

        # AI輔助輸入
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='AI_td_show']"))
        ).click()
        
        # 描述 (產出語言需與描述語言一樣)
        td = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='td']"))
        )
        td.clear() 
        td.send_keys("貓貓")       

        # 生成
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_generate']"))
        ).click()

        time.sleep(10) # 等待生成

        if "生成內容" in driver.page_source:
            print("\033[32m使用課程描述生成成功\033[0m")
        else:
            print("\033[31m使用課程描述生成失敗\033[0m")

        # 確定
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_certain']"))
        ).click()

        # 儲存
        driver.execute_script("save_step(2);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功 " in alert_text:
            alert.accept() 

        # 辨識語系
        scroll_top(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='intro-tab']"))
        ).click()        
        text = driver.find_element(By.XPATH, "//textarea[@id='content']").text
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

        # 教材
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='AI_td_show']"))
        ).click()
        time.sleep(2)
        td = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='td']"))
        )
        td.clear() 
        td.send_keys("")  
        time.sleep(2)  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'教材檔案名稱')]"))
        ).click()   

        # 生成
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_generate']"))
        ).click()

        time.sleep(10) # 等待生成

        if "生成內容" in driver.page_source:
            print("\033[32m使用教材檔案生成成功\033[0m")
        else:
            print("\033[31m使用教材檔案生成失敗\033[0m") 

        # 確定
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_certain']"))
        ).click()

        # 儲存
        driver.execute_script("save_step(2);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功 " in alert_text:
            alert.accept() 

        # 辨識語系
        scroll_top(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='intro-tab']"))
        ).click()        
        text = driver.find_element(By.XPATH, "//textarea[@id='content']").text
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

        # 學習路徑
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='AI_td_show']"))
        ).click()
        time.sleep(2)
        td = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea[@id='td']"))
        )
        td.clear() 
        td.send_keys("")  
        time.sleep(2)  
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'學習路徑標題')]"))
        ).click()   

        # 生成
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_generate']"))
        ).click()

        time.sleep(10) # 等待生成

        if "生成內容" in driver.page_source:
            print("\033[32m使用學習路徑生成成功\033[0m")
        else:
            print("\033[31m使用學習路徑生成失敗\033[0m") 

        # 確定
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='td_certain']"))
        ).click()

        # 儲存
        driver.execute_script("save_step(2);")
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "修改課程成功 " in alert_text:
            alert.accept() 

        # 辨識語系
        scroll_top(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@id='intro-tab']"))
        ).click()        
        text = driver.find_element(By.XPATH, "//textarea[@id='content']").text
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