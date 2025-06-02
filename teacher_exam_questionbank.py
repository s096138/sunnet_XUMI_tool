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
from menu_expanded import menu_expanded_with_sibling    
from selenium_driver import initialize_driver
from datetime import datetime
import random
import string
import time
import os

# 取得當前時間
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

def teacher_exam_questionbank(driver):
    try:
        print("測試：辦公室-測驗管理-題庫維護")
        menu_expanded_with_sibling(driver, "測驗管理", "題庫維護")
        time.sleep(2)
        if "題庫分享中心" in driver.page_source:
            print("\033[32m進入題庫維護成功\033[0m")
        else:
            print("\033[31m進入題庫維護失敗\033[0m") 
        
        # 題庫
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        ).click()   

        # 新增
        time.sleep(2)
        driver.execute_script("process(1);")
        time.sleep(2)
        if "是非" in driver.page_source:
            print("\033[32m進入新增頁面成功\033[0m")
        else:
            print("\033[31m進入新增頁面失敗\033[0m")        

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
            EC.presence_of_element_located((By.XPATH, "//form[@id='tabContentForm1']//input[contains(@id,'topic_files')]"))
        )
        file_path = "c:\\Users\\SGQA2\\Desktop\\Auto\\test.side"
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
        
        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm1'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

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
        time.sleep(5)
        # current_height = driver.execute_script("return document.body.scrollHeight")
        # print(current_height)
        scroll_half(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[1]"))
        ).click()
        option_a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "render_choices[0]"))
        )
        option_a_input.click()
        option_a_input.send_keys("A")

        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "render_choices[1]"))
        )
        option_b_input.click()
        option_b_input.send_keys("B")
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[2]'))
        )
        driver.execute_script("arguments[0].click();", option_c_input)
        option_c_input.send_keys("C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[3]'))
        )
        driver.execute_script("arguments[0].click();", option_d_input)
        option_d_input.send_keys("D")

        # 答案
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'sysRadioBtn1'))
        ).click()

        # 分類
        scroll_bottom(driver)
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

        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm2'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

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
            alert.accept()
        else:
            print("\033[31m單選題建立失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 多選----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab03"))
        ).click()

        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[3])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_3 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 選項
        time.sleep(5)
        scroll_half(driver)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'][contains(text(),'更多選項')])[2]"))
        ).click()
        option_a_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[0]'])[2]"))
        )
        option_a_input.click()
        option_a_input.send_keys("A")
        
        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[1]'])[1]"))
        )
        option_b_input.click()
        option_b_input.send_keys("B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[2]'])[1]"))
        )
        option_c_input.click()
        option_c_input.send_keys("C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//input[@name='render_choices[3]'])[1]"))
        )
        option_d_input.click()
        option_d_input.send_keys("D")

        # 答案
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn1'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'sysCheckboxBtn2'))
        ).click()

        # 分類
        scroll_bottom(driver)
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

        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm3'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

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
            alert.accept()
        else:
            print("\033[31m多選題建立失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 填充----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab04"))
        ).click()

        random_cloze = generate_random_cloze()
        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[8])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_4 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>{random_cloze}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 分類
        scroll_bottom(driver)
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm4'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm4'] input[value='確定新增']"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m填充題建立成功\033[0m")
            alert.accept()
        else:
            print("\033[31m填充題建立失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 簡答----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab05"))
        ).click()

        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[8])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_5 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 分類
        scroll_bottom(driver)
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm5'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm5'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm5'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm5'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm5'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "form[id='tabContentForm5'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabContentForm5 .btn-wm-purple"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m簡答題建立成功\033[0m")
            alert.accept()
        else:
            print("\033[31m簡答題建立失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 配合----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab06"))
        ).click()

        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[10])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_6 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 選項
        time.sleep(5)
        # random_number = random.choice(['1', '2'])
        scroll_half(driver)
        matching = driver.find_element(By.CSS_SELECTOR, "input[name='render1_choices[1]']")
        driver.execute_script("arguments[0].scrollIntoView(true);", matching)
        driver.find_element(By.CSS_SELECTOR, "input[name='render1_choices[0]']").click() #題目提示A
        driver.find_element(By.CSS_SELECTOR, "input[name='render1_choices[0]']").send_keys("提示一")
        driver.find_element(By.CSS_SELECTOR, "input[name='render1_choices[1]']").click() #題目提示B
        driver.find_element(By.CSS_SELECTOR, "input[name='render1_choices[1]']").send_keys("提示二")

        driver.find_element(By.CSS_SELECTOR, "input[name='render2_choices[0]']").click() #待選項目1
        driver.find_element(By.CSS_SELECTOR, "input[name='render2_choices[0]']").send_keys("選項一號")
        driver.find_element(By.CSS_SELECTOR, "input[name='render2_choices[1]']").click() #待選項目2
        driver.find_element(By.CSS_SELECTOR, "input[name='render2_choices[1]']").send_keys("選項二號") 

        driver.find_element(By.XPATH, "//div[normalize-space()='A']//input[@title='請填【待選項目】之數字題號']").click() #標準答案A
        driver.find_element(By.XPATH, "//div[normalize-space()='A']//input[@title='請填【待選項目】之數字題號']").send_keys("1")
        driver.find_element(By.XPATH, "//div[normalize-space()='B']//input[@title='請填【待選項目】之數字題號']").click() #標準答案B
        driver.find_element(By.XPATH, "//div[normalize-space()='B']//input[@title='請填【待選項目】之數字題號']").send_keys("2")      
        
        # 分類
        scroll_bottom(driver)
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='row mb-3'] input[name='version']"))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='row mb-3'] input[name='volume']"))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='row mb-3'] input[name='chapter']"))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='row mb-3'] input[name='paragraph']"))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div[class='row mb-3'] input[name='section']"))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)
        
        # 難易度
        select_element = driver.find_element(By.CSS_SELECTOR, "div[class='row mb-3'] select[name='level']")
        select = Select(select_element)
        options = ["1", "2", "3", "4", "5"]
        random_value = random.choice(options)
        select.select_by_value(random_value)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabContentForm6 .btn-wm-purple"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m配合題建立成功\033[0m")
            alert.accept()
        else:
            print("\033[31m配合題建立失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 回列表
        time.sleep(2)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "form[id='tabContentForm1'] input[value='回列表']"))
        ).click()
        time.sleep(2)
        if "題庫分享中心" in driver.page_source:
            print("\033[32m回列表成功\033[0m")
        else:
            print("\033[31m回列表失敗\033[0m") 

        # 題型搜尋 簡配版是form1
        time.sleep(2)
        type = driver.find_element(By.CSS_SELECTOR, "form[id='form1'] select[name='type']")
        select = Select(type)
        select.select_by_value("6")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isType']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        if "1-1 筆" in driver.page_source:
            print("\033[32m勾選題型搜尋正確\033[0m")
        else:
            print("\033[31m勾選題型搜尋錯誤\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isType']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        if "1-6 筆" in driver.page_source:
            print("\033[32m未勾選題型搜尋正確\033[0m")
        else:
            print("\033[31m未勾選題型搜尋錯誤\033[0m")

        # 難易度搜尋
        time.sleep(2)
        type = driver.find_element(By.CSS_SELECTOR, "form[id='form1'] select[name='level']")
        select = Select(type)
        select.select_by_value("3")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isLevel']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        td1 = driver.find_element(By.XPATH, "//*[@id='mainTable']/tbody/tr/td[10]").text
        if td1 == "適中" or "查無相關資料" in driver.page_source:
            print("\033[32m勾選難易度搜尋正確\033[0m")
        else:
            print("\033[31m勾選難易度搜尋錯誤\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isLevel']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        if "1-6 筆" in driver.page_source:
            print("\033[32m未勾選難易度搜尋正確\033[0m")
        else:
            print("\033[31m未勾選難易度搜尋錯誤\033[0m")

        # 關鍵字搜尋
        time.sleep(5)
        keyword = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "form[id='form1'] input[placeholder='請在此輸入搜尋的關鍵字']"))
        )
        keyword.click()
        keyword.send_keys(random_cloze)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isFulltext']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        if "1-1 筆" in driver.page_source:
            print("\033[32m勾選關鍵字搜尋正確\033[0m")
        else:
            print("\033[31m勾選關鍵字搜尋錯誤\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='divSearchPanel']//input[@id='isFulltext']"))
        ).click()
        driver.execute_script("do_search_item()")
        time.sleep(2)
        if "1-6 筆" in driver.page_source:
            print("\033[32m未勾選關鍵字搜尋正確\033[0m")
        else:
            print("\033[31m未勾選關鍵字搜尋錯誤\033[0m")  

        # 分享
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_box"))
        ).click() 
        driver.execute_script("process(6);")   
        time.sleep(2)     
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "感謝您" in alert_text:
            print("\033[32m分享題目成功\033[0m")
            alert.accept()
        else:
            print("\033[31m分享題目失敗\033[0m")
            time.sleep(5)
            alert.accept()

        # 複製
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        # ).click()  
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "body > div:nth-child(4) > div:nth-child(1) > div:nth-child(2) > div:nth-child(7) > div:nth-child(2) > div:nth-child(3) > form:nth-child(1) > table:nth-child(7) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > input:nth-child(1)"))
        ).click()  
        driver.execute_script("process(4);") 
        time.sleep(2)  
        time.sleep(2)
        if "1-10 筆" in driver.page_source:
            print("\033[32m複製題目成功\033[0m")
        else:
            print("\033[31m複製題目失敗\033[0m") 

        # 刪除
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "#tab02"))
        # ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ck_box"))
        ).click()  
        driver.execute_script("process(3);") 
        time.sleep(2)    
        alert = driver.switch_to.alert
        alert_text = alert.text 
        if "確定要刪除嗎？" in alert_text:
            alert.accept()
            time.sleep(2)
            if "刪除成功" in driver.page_source:
                print("\033[32m刪除題目成功\033[0m")
                scroll_bottom(driver)
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id='btnReturn']"))
                ).click() 
            else:
                print("\033[31m刪除題目失敗\033[0m")
                time.sleep(5)        
        else:
            print("\033[31m刪除題目失敗\033[0m")
            time.sleep(5)
            alert.accept()

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