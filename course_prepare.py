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
import string
import random
import time
import os
from datetime import datetime
from teacher_enter import teacher_enter

nowdatetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def scroll_bottom(driver):
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2) 
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

def scroll_half(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        # 滾動到頁面的1/3
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight / 3);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# 隨機生成分類
def generate_random_class(length=1):
    return str(random.randint(0, 9))

# 填充題
def generate_random_cloze(length=20):    
    letters = string.ascii_letters + string.digits
    content = ''.join(random.choice(letters) for _ in range(length - 8))

    position1 = random.randint(0, len(content) - 1)
    content = content[:position1] + '((' + content[position1:]
    position2 = random.randint(position1 + 3, len(content) + 1)
    content = content[:position2] + '))' + content[position2:]
    return content

def course_prepare(driver):
    try:  
        print("課程資料建置")
        teacher_enter(driver)

        # # 課程章節
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程管理')]"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'學習路徑管理')]"))
        # ).click()

        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_add']"))
        # ).click()
        # time.sleep(2)
        # title = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@id='title[Big5]'])[1]"))
        # )       
        # title.clear()   
        # title.send_keys("114年辦公日曆表")    
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'引用教材')]"))
        # ).click()
        # time.sleep(2)
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'上傳檔案')])[1]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='upload_file']"))
        # ).send_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳檔案']"))
        # ).click()
        # driver.switch_to.window(windows[0])
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='setting_btn']"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_add']"))
        # ).click()
        # time.sleep(2)
        # title = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@id='title[Big5]'])[1]"))
        # )       
        # title.clear()   
        # title.send_keys("202410旭航v4")    
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'引用教材')]"))
        # ).click()
        # time.sleep(2)
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'上傳檔案')])[1]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@id='upload_file']"))
        # ).send_keys(r"C:\Users\SGQA2\Downloads\202410旭航v4.mp4") #可替換
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@value='上傳檔案']"))
        # ).click()
        # driver.switch_to.window(windows[0])
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='setting_btn']"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btn_save']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存成功" in alert_text: 
        #     alert.accept() 
        # if "114年辦公日曆表" in driver.page_source and "202410旭航v4" in driver.page_source:
        #     print("\033[32m新增節點成功\033[0m")
        # else:
        #     print("\033[31m新增節點失敗\033[0m")        

        # # 課程公告
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'教室管理')]"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'課程公告板')]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[@title='課程公告板']//a[@class='cssAnchor'][contains(text(),'課程公告板')]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'張貼')]"))
        # ).click()
        # time.sleep(2)
        # title = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
        # )
        # title.send_keys("公告1")
        # editor = WebDriverWait(driver, 20).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@class='ql-editor ql-blank']"))
        # )
        # editor.send_keys("自動化測試用")
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[@id='btnSubmit']"))
        # ).click()
        # time.sleep(2)
        # if "公告1" in driver.page_source:
        #     print("\033[32m新增課程公告成功\033[0m")
        # else:
        #     print("\033[31m新增課程公告失敗\033[0m")

        # # 作業
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'作業管理')])[1]"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'題庫維護')])[1]"))
        # ).click()

        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        # ).click()    

        # # 是非----------------------------
        # time.sleep(2)
        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # print(f"頁面上的 iframe 數量: {len(iframes)}")
        # # driver.switch_to.frame(iframes[0])

        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_1 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 題目附檔
        # time.sleep(2)
        # upload_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//form[@id="tabContentForm1"]//input[contains(@id,"topic_files")]'))
        # )
        # file_path = "C:\\Users\\SGQA2\\Downloads\\蛙蛙.jpg"
        # if os.path.exists(file_path):
        #     upload_button.send_keys(file_path)
        #     print(f"\033[32m附檔已上傳：{file_path}\033[0m")
        # else:
        #     print(f"\033[31m檔案不存在：{file_path}\033[0m")

        # # 分類
        # scroll_bottom(driver)
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)
        
        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm1'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # scroll_bottom(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m是非題建立成功\033[0m")
        # else:
        #     print("\033[31m是非題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 單選----------------------------
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "tab02"))
        # ).click()

        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # driver.switch_to.frame(iframes[1])
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_2 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 選項
        # scroll_bottom(driver)
        # time.sleep(5)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # scroll_bottom(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # option_a_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, "render_choices[0]"))
        # )
        # option_a_input.click()
        # option_a_input.send_keys("單選A")

        # option_b_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, "render_choices[1]"))
        # )
        # option_b_input.click()
        # option_b_input.send_keys("單選B")
        # scroll_bottom(driver)
        # option_c_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, 'render_choices[2]'))
        # )
        # option_c_input.click()
        # option_c_input.send_keys("單選C")

        # option_d_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, 'render_choices[3]'))
        # )
        # option_d_input.click()
        # option_d_input.send_keys("單選D")

        # # 答案
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysRadioBtn1'))
        # ).click()

        # # 分類
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)

        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm2'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m單選題建立成功\033[0m")
        # else:
        #     print("\033[31m單選題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 多選----------------------------
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "tab03"))
        # ).click()

        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # driver.switch_to.frame(iframes[2])
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_3 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 選項
        # time.sleep(5)
        # scroll_bottom(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        # ).click()
        # scroll_bottom(driver)
        # option_a_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[0]'])[2]"))
        # )
        # option_a_input.click()
        # option_a_input.send_keys("多選A")
        
        # option_b_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[1]'])[1]"))
        # )
        # option_b_input.click()
        # option_b_input.send_keys("多選B")
        
        # option_c_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[2]'])[1]"))
        # )
        # option_c_input.click()
        # option_c_input.send_keys("多選C")

        # option_d_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[3]'])[1]"))
        # )
        # option_d_input.click()
        # option_d_input.send_keys("多選D")

        # # 答案
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn1'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn2'))
        # ).click()

        # # 分類
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)

        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm3'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m多選題建立成功\033[0m")
        # else:
        #     print("\033[31m多選題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 回列表
        # time.sleep(2)
        # scroll_bottom(driver)
        # time.sleep(2)
        # driver.execute_script("return_list('')")
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'作業維護')]"))
        # ).click()   

        # # 新增
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        # ).click()

        # # 作業資訊
        # time.sleep(2)
        # name = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        # )
        # name.click()
        # name.clear()
        # name.send_keys("作業一")
        # WebDriverWait(driver, 20).until( # 發布
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn7"))
        # ).click()
        # time.sleep(2)
        # driver.execute_script("switchTab(1);")   

        # # 挑選題目
        # WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='開始搜尋']"))
        # ).click()        
        # scroll_bottom(driver)
        # WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_ck"))
        # ).click()            
        # WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.XPATH, "//td[@align='right']//input[@value='選取']"))
        # ).click()  
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "請按【下一步】到排列與配分去" in alert_text:
        #     print("\033[32m挑選題目成功\033[0m")
        # else:
        #     print("\033[31m挑選題目失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()
        # driver.execute_script("switchTab(2);")
        
        # # 排列與配分
        # WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.XPATH, "//input[@value='平均配分']"))
        # ).click() 
        # score = WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.XPATH, "//input[@name='score']"))
        # )
        # score.click()
        # score.clear()
        # score.send_keys("100") 
        # WebDriverWait(driver, 20).until( 
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'確定')])[2]"))
        # ).click() 
        # driver.execute_script("switchTab(4);")

        # # 作業預覽
        # driver.execute_script("saveContent();")
        # time.sleep(2)
        # td1 = driver.find_element(By.XPATH, "//*[@id='displayPanel']/tbody/tr/td[5]").text
        # if "作業一" in driver.page_source:
        #     print("\033[32m新增作業成功\033[0m")
        # else:
        #     print("\033[31m新增作業失敗\033[0m")

        # # 測驗
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'測驗管理')]"))
        # ).click()
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'題庫維護')])[2]"))
        # ).click()        
        # # 題庫
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        # ).click()   

        # # 新增
        # time.sleep(2)
        # driver.execute_script("process(1);")
        # time.sleep(2)       

        # # 是非----------------------------
        # time.sleep(2)
        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # print(f"頁面上的 iframe 數量: {len(iframes)}")
        # # driver.switch_to.frame(iframes[0])

        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_1 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 題目附檔
        # time.sleep(2)
        # upload_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//form[@id='tabContentForm1']//input[contains(@id,'topic_files')]"))
        # )
        # file_path = "C:\\Users\\SGQA2\\Downloads\\蛙蛙.jpg"
        # if os.path.exists(file_path):
        #     upload_button.send_keys(file_path)
        #     print(f"\033[32m附檔已上傳：{file_path}\033[0m")
        # else:
        #     print(f"\033[31m檔案不存在：{file_path}\033[0m")

        # # 分類
        # scroll_bottom(driver)
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)
        
        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm1'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m是非題建立成功\033[0m")
        # else:
        #     print("\033[31m是非題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 單選----------------------------
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "tab02"))
        # ).click()

        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # driver.switch_to.frame(iframes[1])
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_2 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 選項
        # time.sleep(5)
        # # current_height = driver.execute_script("return document.body.scrollHeight")
        # # print(current_height)
        # scroll_half(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        # ).click()
        # option_a_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, "render_choices[0]"))
        # )
        # option_a_input.click()
        # option_a_input.send_keys("單選A")

        # option_b_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, "render_choices[1]"))
        # )
        # option_b_input.click()
        # option_b_input.send_keys("單選B")
        # option_c_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, 'render_choices[2]'))
        # )
        # driver.execute_script("arguments[0].click();", option_c_input)
        # option_c_input.send_keys("單選C")

        # option_d_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.NAME, 'render_choices[3]'))
        # )
        # driver.execute_script("arguments[0].click();", option_d_input)
        # option_d_input.send_keys("單選D")

        # # 答案
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysRadioBtn1'))
        # ).click()

        # # 分類
        # scroll_bottom(driver)
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)

        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm2'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m單選題建立成功\033[0m")
        # else:
        #     print("\033[31m單選題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 多選----------------------------
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, "tab03"))
        # ).click()

        # # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # # driver.switch_to.frame(iframes[2])
        # editable = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_3 .ql-editor"))
        # )
        # script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        # driver.execute_script(script, editable)
        # # driver.switch_to.default_content()

        # # 選項
        # time.sleep(5)
        # scroll_half(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        # ).click()
        # option_a_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[0]'])[2]"))
        # )
        # option_a_input.click()
        # option_a_input.send_keys("多選A")
        
        # option_b_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[1]'])[1]"))
        # )
        # option_b_input.click()
        # option_b_input.send_keys("多選B")
        
        # option_c_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[2]'])[1]"))
        # )
        # option_c_input.click()
        # option_c_input.send_keys("多選C")

        # option_d_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[3]'])[1]"))
        # )
        # option_d_input.click()
        # option_d_input.send_keys("多選D")

        # # 答案
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn1'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn2'))
        # ).click()

        # # 分類
        # scroll_bottom(driver)
        # version_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='version']"))
        # )
        # version_input.click()
        # version = generate_random_class()
        # version_input.send_keys(version)

        # volume_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='volume']"))
        # )
        # volume_input.click()
        # volume = generate_random_class()
        # volume_input.send_keys(volume)

        # chapter_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='chapter']"))
        # )
        # chapter_input.click()
        # chapter = generate_random_class()
        # chapter_input.send_keys(chapter)

        # paragraph_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='paragraph']"))
        # )
        # paragraph_input.click()
        # paragraph = generate_random_class()
        # paragraph_input.send_keys(paragraph)

        # section_input = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='section']"))
        # )
        # section_input.click()
        # section = generate_random_class()
        # section_input.send_keys(section)

        # # 難易度
        # select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm3'] select[name='level']")
        # select = Select(select_element)
        # options = ["1", "2", "3", "4", "5"]
        # random_value = random.choice(options)
        # select.select_by_value(random_value)

        # # 確定新增
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[value='確定新增']"))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m多選題建立成功\033[0m")
        # else:
        #     print("\033[31m多選題建立失敗\033[0m")
        #     time.sleep(5)
        # alert.accept()

        # # 回列表
        # time.sleep(2)
        # scroll_bottom(driver)
        # time.sleep(2)
        # driver.execute_script("return_list('')")
        # time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'測驗管理')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'試卷維護')]"))
        ).click()

        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        ).click()

        # 測驗資訊
        time.sleep(2)
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("測驗一")
        WebDriverWait(driver, 20).until( # 發布
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn7"))
        ).click()
        driver.execute_script("switchTab(1);")   

        # 挑選題目
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn10"))
        ).click() 
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@value='開始搜尋']"))
        ).click() 
        scroll_bottom(driver)     
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@id='search_ck']"))
        ).click()
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//td[@align='right']//input[@value='選取']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請按【下一步】到排列與配分去" in alert_text:
            print("\033[32m挑選題目成功\033[0m")
        else:
            print("\033[31m挑選題目失敗\033[0m")
            time.sleep(5)
        alert.accept()
        driver.execute_script("switchTab(2);")

        # 排列與配分
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@value='平均配分']"))
        ).click() 
        score = WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//input[@name='score']"))
        )
        score.click()
        score.clear()
        score.send_keys("100") 
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'確定')])[2]"))
        ).click() 
        driver.execute_script("switchTab(4);")   

        # 測驗預覽
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "測驗一" in driver.page_source:
            print("\033[32m新增測驗成功\033[0m")
        else:
            print("\033[31m新增測驗失敗\033[0m")

        # 問卷
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'問卷管理')])[1]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'題庫維護')])[3]"))
        ).click()

       # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        ).click()
        time.sleep(2)     

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
            print(f"\033[32m附檔已上傳：{file_path}\033[0m")
        else:
            print(f"\033[31m檔案不存在：{file_path}\033[0m")

        # 分類
        scroll_bottom(driver)
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[value='確定新增']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m是非題建立成功\033[0m")
            alert.accept()
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
        scroll_bottom(driver)
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
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm2'] input[value='確定新增']"))
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
        option_a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[0]'])[2]"))
        )
        option_a_input.click()
        option_a_input.send_keys("多選A")
        
        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[1]'])[1]"))
        )
        option_b_input.click()
        option_b_input.send_keys("多選B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[2]'])[1]"))
        )
        option_c_input.click()
        option_c_input.send_keys("多選C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[3]'])[1]"))
        )
        option_d_input.click()
        option_d_input.send_keys("多選D")

        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm3'] input[value='確定新增']"))
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
        time.sleep(2)
        scroll_bottom(driver)
        time.sleep(2)
        driver.execute_script("return_list('')")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'問卷管理')]"))
        ).click() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'問卷維護')]"))
        ).click()  

        # 新增
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(text(),"新增")]'))
        ).click()

        # 問卷資訊
        time.sleep(2)
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("問卷一")
        WebDriverWait(driver, 20).until( # 發布
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn7"))
        ).click()
        # WebDriverWait(driver, 20).until( # 開放作答時間
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_begin_time"))
        # ).click()
        driver.execute_script("switchTab(1);")   

        # 挑選題目
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='開始搜尋']"))
        ).click()
        scroll_bottom(driver)        
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_ck"))
        ).click() 
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.CSS_SELECTOR, "td[align='right'] input[value='選取']"))
        ).click()   
        time.sleep(2) 
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "請按【下一步】到排列調整去" in alert_text:
            print("\033[32m挑選題目成功\033[0m")
            alert.accept()
        else:
            print("\033[31m挑選題目失敗\033[0m")
            time.sleep(5)
            alert.accept()
        driver.execute_script("switchTab(2);")
        driver.execute_script("switchTab(4);")

        # 作業預覽
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "問卷一" in driver.page_source:
            print("\033[32m新增問卷成功\033[0m")
        else:
            print("\033[31m新增問卷失敗\033[0m")

        # 同儕作業
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'同儕作業管理')]"))
        ).click()
        WebDriverWait(driver, 20).until( 
            EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'作業維護')])[2]"))
        ).click()
        time.sleep(2)

        # 新增
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增作業')]"))
        ).click()       
        name = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='title[Big5]']"))
        )
        name.click()
        name.clear()
        name.send_keys("同儕作業一")

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#sysRadioBtn4"))
        ).click()  
        time.sleep(2)

        scroll_bottom(driver)
        # WebDriverWait(driver, 20).until(
        #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, rating_criteria_1']"))
        # )
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, 'body'))
        # ).click()
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, '.cke_editable'))
        # ).click()
        # driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", driver.find_element(By.CSS_SELECTOR, '.cke_editable'))
        # driver.switch_to.default_content()
        editables = driver.find_elements(By.CSS_SELECTOR, ".ql-editor")
        editables[1].click()
        editables[1].clear()
        editables[1].send_keys("自動化測試用")
        time.sleep(2)
        driver.execute_script("saveContent(4);")
        time.sleep(2)
        driver.execute_script("saveContent();")
        time.sleep(2)
        if "同儕作業一" in driver.page_source:
            print("\033[32m新增同儕作業成功\033[0m")
        else:
            print("\033[31m新增同儕作業失敗\033[0m") 

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