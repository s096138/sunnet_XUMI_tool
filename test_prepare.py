from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
import time
import os
import string
import random
from datetime import datetime
from pywinauto import Application
from admin_enter import admin_enter
from menu_expanded import menu_expanded
from admin_management_center import admin_management_center

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
            
# 隨機生成分類
def generate_random_class(length=1):
    return str(random.randint(1, 9))

# 填充題
def generate_random_cloze(length=20):    
    letters = string.ascii_letters + string.digits
    content = ''.join(random.choice(letters) for _ in range(length - 8))
    position1 = random.randint(0, len(content) - 1)
    content = content[:position1] + '((' + content[position1:]
    position2 = random.randint(position1 + 3, len(content) + 1)
    content = content[:position2] + '))' + content[position2:]
    return content

def test_prepare(driver):
    try:
        print("首頁資料建置")
        admin_enter(driver)
        time.sleep(2)
        admin_management_center(driver)
        time.sleep(2)

        # 首頁下載專區
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'公告管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'首頁下載專區')]"))
        ).click()

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'title'))
        )
        name.click()
        name.send_keys("自動化測試用下載1")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_date'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_date'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'upload'))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        driver.execute_script("checkData()")

        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'title'))
        )
        name.click()
        name.send_keys("自動化測試用下載2")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_date'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_date'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'upload'))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\xumi@1x.png") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)
        driver.execute_script("checkData()")
        time.sleep(2)
        if "自動化測試用下載1" in driver.page_source and "自動化測試用下載2" in driver.page_source:
            print("\033[32m新增首頁下載專區成功\033[0m")
        else:
            print("\033[31m新增首頁下載專區失敗\033[0m") 

        # 最新消息
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'公告管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'最新消息')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="subject"]'))
        )
        name.click()
        name.send_keys("自動化測試用最新消息1")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_time'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_time'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script("arguments[0].innerHTML = '<p>自動化測試用最新消息1</p>'", editable_body)
        # driver.switch_to.default_content()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[3]/div/div[2]/button'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        time.sleep(2)
        driver.execute_script("checkData()")
        
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        time.sleep(2)
        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="subject"]'))
        )
        name.click()
        name.send_keys("自動化測試用最新消息2")
        time.sleep(2)
        day1 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'open_time'))
        )
        day1.click()
        day1.send_keys(nowdatetime)
        day2 = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'close_time'))
        )
        day2.click()
        day2.send_keys(nowdatetime)
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script("arguments[0].innerHTML = '<p>自動化測試用最新消息2</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[3]/div/div[2]/button'))
        # ).click()
        # time.sleep(2)
        # app = Application(backend="win32").connect(title_re=".*開啟.*")
        # dlg = app.window(title_re=".*開啟.*")
        # dlg.set_focus()
        # dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\xumi@1x.png") #可替換
        # time.sleep(2)
        # dlg['開啟'].click()
        # time.sleep(2)

        # 確定
        driver.execute_script("checkData()")
        time.sleep(2)
        if "自動化測試用最新消息1" in driver.page_source and "自動化測試用最新消息2" in driver.page_source:
            print("\033[32m新增最新消息成功\033[0m")
        else:
            print("\033[31m新增最新消息失敗\033[0m")

        # 常見問題
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'公告管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'常見問題')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='btn-edit-category']"))
        ).click()
        # 避免文章重複
        time.sleep(2)
        if "自動化測試用分類1" in driver.page_source and "自動化測試用分類2" in driver.page_source:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'del-txt') and preceding-sibling::input[@value='自動化測試用分類1']]"))
            ).click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept() 
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'del-txt') and preceding-sibling::input[@value='自動化測試用分類2']]"))
            ).click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept() 
        elif "自動化測試用分類1" in driver.page_source:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'del-txt') and preceding-sibling::input[@value='自動化測試用分類1']]"))
            ).click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept()
        elif "自動化測試用分類2" in driver.page_source:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(@class, 'del-txt') and preceding-sibling::input[@value='自動化測試用分類2']]"))
            ).click()
            time.sleep(2)
            alert = driver.switch_to.alert
            alert.accept() 
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增分類')]"))
        ).click()
        time.sleep(2)
        class_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='新分類'])[1]"))
        )
        class_name.send_keys("自動化測試用分類1")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增分類')]"))
        ).click()
        time.sleep(2)
        class_name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@placeholder='新分類'])[2]"))
        )
        class_name.send_keys("自動化測試用分類2")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='categories-submit']"))
        ).click()
        time.sleep(2)
        alert = alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        time.sleep(2)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()   
        time.sleep(2) 
        select = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'category'))
        ))
        select.select_by_visible_text("自動化測試用分類1")
        title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='subject']"))
        )
        title.click()
        title.send_keys("自動化測試用常見問題1")
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用常見問題1</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        driver.execute_script("checkData()")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()   
        time.sleep(2) 
        select = Select(WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'category'))
        ))
        select.select_by_visible_text("自動化測試用分類2")
        title = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='subject']"))
        )
        title.click()
        title.send_keys("自動化測試用常見問題2")
        time.sleep(2)
        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用常見問題2</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        driver.execute_script("checkData()")

        time.sleep(2)
        if "自動化測試用常見問題1" in driver.page_source:
            print("\033[32m新增常見問題成功\033[0m")
        else:
            print("\033[31m新增常見問題失敗\033[0m")

        # 問卷調查
        menu_expanded(driver, "問卷管理", "題庫維護")

        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="form1"]/div[2]/div[1]/div/div/div[1]/button'))
        ).click()

        # 是非----------------------------
        time.sleep(2)
        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # print(f"頁面上的 iframe 數量: {len(iframes)}")
        # driver.switch_to.frame(iframes[0])

        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_1 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 題目附檔
        time.sleep(2)
        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//form[@id="tabContentForm1"]//input[contains(@id,"topic_files")]'))
        )
        file_path = "C:\\Users\\SGQA2\\Downloads\\蛙蛙.jpg"
        if os.path.exists(file_path):
            upload_button.send_keys(file_path)
            print(f"題目附檔已上傳：{file_path}")
        else:
            print(f"題目附檔不存在：{file_path}")

        # 分類
        scroll_bottom(driver)
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm1"]/div/div[6]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm1"]/div/div[6]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm1"]/div/div[6]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm1"]/div/div[6]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm1"]/div/div[6]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='tabContentForm1']//input[@value='確定新增']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m是非題建立成功\033[0m")
        else:
            print("\033[31m是非題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        # 單選----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab02"))
        ).click()

        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[1])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_2 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 選項
        scroll_bottom(driver)
        time.sleep(5)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        option_a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "render_choices[0]"))
        )
        option_a_input.click()
        option_a_input.send_keys("單選A")

        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "render_choices[1]"))
        )
        option_b_input.click()
        option_b_input.send_keys("單選B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[2]'))
        )
        option_c_input.click()
        option_c_input.send_keys("單選C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[3]'))
        )
        option_d_input.click()
        option_d_input.send_keys("單選D")

        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm2"]/div/div[6]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm2"]/div/div[6]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm2"]/div/div[6]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm2"]/div/div[6]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm2"]/div/div[6]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabContentForm2 .btn-wm-purple"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m單選題建立成功\033[0m")
        else:
            print("\033[31m單選題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        # 多選----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab03"))
        ).click()

        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[2])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_3 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 選項
        time.sleep(5)
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        ).click()
        scroll_bottom(driver)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        option_a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[1]/div[2]/input[1]'))
        )
        option_a_input.click()
        option_a_input.send_keys("多選A")

        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[2]/div[2]/input[1]'))
        )
        option_b_input.click()
        option_b_input.send_keys("多選B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[3]/div[2]/input[1]'))
        )
        option_c_input.click()
        option_c_input.send_keys("多選C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[4]/div[2]/input[1]'))
        )
        option_d_input.click()
        option_d_input.send_keys("多選D")

        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[6]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[6]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[6]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[6]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[6]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabContentForm3 .btn-wm-purple"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m多選題建立成功\033[0m")
        else:
            print("\033[31m多選題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        # 回列表
        scroll_bottom(driver)
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='tabContentForm1']//input[@value='回列表']"))
        ).click()

        # 問卷維護
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'問卷維護')]"))
        ).click()

        # 新增
        driver.execute_script("executing(1)")

        # 問卷名稱
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "title[Big5]"))
        ).send_keys(Keys.BACK_SPACE * 10)
        driver.find_element(By.ID, "title[Big5]").send_keys("自動化測試用問卷")
        # 作答說明
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "notice"))
        ).send_keys("自動化測試用問卷")
        # 發布設定
        WebDriverWait(driver, 10).until(
             EC.element_to_be_clickable((By.ID, "sysRadioBtn7"))
        ).click()
        # 公布答案
        select = Select(driver.find_element(By.ID, "announce_type"))
        select.select_by_visible_text("作答完公布")

        # 挑選題目
        time.sleep(2)
        driver.execute_script("switchTab(1);")
        text = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='fulltext'])[1]"))
        )
        text.click()
        text.clear()
        text.send_keys("自動化測試用")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@value="開始搜尋"]'))
        ).click()
        scroll_bottom(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='search_ck']"))
        ).click()

        driver.execute_script("pickItem()")
        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "請按【下一步】到排列調整去，或繼續挑選題目"
        alert.accept()

        # 完成存檔
        driver.execute_script("switchTab(2);")
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "自動化測試用問卷" in driver.page_source:
            print("\033[32m新增問卷成功\033[0m")
        else:
            print("\033[31m新增問卷失敗\033[0m")

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