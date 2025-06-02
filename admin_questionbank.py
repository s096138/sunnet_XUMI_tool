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
from datetime import datetime
import string
import random
import time
import os

# 取得當前時間
nowdatetime = datetime.now().strftime("%Y-%m-%d %H:%M")

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

def admin_questionbank(driver):
    try:
        print("測試：管理者環境-問卷管理-題庫維護")
        menu_expanded(driver, "問卷管理", "題庫維護")
        time.sleep(2)
        if "題目敘述" in driver.page_source:
            print("\033[32m進入題庫維護成功\033[0m")
        else:
            print("\033[31m進入題庫維護失敗\033[0m") 

        # # 批次動作-複製
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="mainTable"]/tbody/tr[1]/td[1]/input'))
        # ).click()
        # driver.execute_script("process(4)")
        # scroll_bottom(driver)
        # WebDriverWait(driver, 10).until( #8頁
        #     EC.element_to_be_clickable((By.XPATH, '//span[normalize-space()="8"]'))
        # ).click()
        # time.sleep(2)
        # if "全身上下最敏感的觸覺受器在鼻尖與耳垂上" in driver.page_source:
        #     print("\033[32m批次動作-複製成功\033[0m")
        # else:
        #     print("\033[31m批次動作-複製失敗\033[0m")

        # # 批次動作-修改
        # time.sleep(2)
        # scroll_bottom(driver)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'[全身上下最敏感的觸覺受器在鼻尖與耳垂上]')]"))
        # ).click()
        # time.sleep(5)
        # # driver.switch_to.frame(0)
        # # WebDriverWait(driver, 10).until(
        # #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # # ).click()
        # editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        # driver.execute_script(f"arguments[0].innerHTML = '<p>自動化測試用</p>'", editable_body)
        # # driver.switch_to.default_content()
        # time.sleep(2)
        # WebDriverWait(driver, 10).until( 
        #     EC.element_to_be_clickable((By.XPATH, '//input[@value="確定修改"]'))
        # ).click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "儲存完畢" in alert_text:
        #     print("\033[32m批次動作-修改成功\033[0m")
        #     alert.accept()
        # else:
        #     print("\033[31m批次動作-修改失敗\033[0m")

        # # 批次動作-刪除
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//*[@id="mainTable"]/tbody/tr[7]/td[1]/input'))
        # ).click()
        # driver.execute_script("process(3)")
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert_text = alert.text
        # if "確定要刪除嗎？" in alert_text:
        #     alert.accept()
        #     time.sleep(2)
        #     alert = driver.switch_to.alert
        #     alert_text = alert.text
        #     if "刪除完成" in alert_text:
        #         print("\033[32m批次動作-刪除成功\033[0m")
        #         alert.accept()
        #         time.sleep(2) 
        # else:
        #     print("\033[31m批次動作-刪除失敗\033[0m")

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
        file_path = "c:\\Users\\SGQA2\\Desktop\\Auto\\test.side"
        if os.path.exists(file_path):
            upload_button.send_keys(file_path)
            print(f"帳號檔案已上傳：{file_path}")
        else:
            print(f"帳號檔案不存在：{file_path}")

        # 分類
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
        option_a_input.send_keys("A")

        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "render_choices[1]"))
        )
        option_b_input.click()
        option_b_input.send_keys("B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[2]'))
        )
        option_c_input.click()
        option_c_input.send_keys("C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.NAME, 'render_choices[3]'))
        )
        option_d_input.click()
        option_d_input.send_keys("D")

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
        option_a_input.send_keys("A")

        option_b_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[2]/div[2]/input[1]'))
        )
        option_b_input.click()
        option_b_input.send_keys("B")
        
        option_c_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[3]/div[2]/input[1]'))
        )
        option_c_input.click()
        option_c_input.send_keys("C")

        option_d_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm3"]/div/div[5]/div[4]/div[2]/input[1]'))
        )
        option_d_input.click()
        option_d_input.send_keys("D")

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

        # 填充----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab04"))
        ).click()

        random_cloze = generate_random_cloze()
        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[3])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_4 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>{random_cloze}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm4"]/div/div[5]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm4"]/div/div[5]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm4"]/div/div[5]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm4"]/div/div[5]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm4"]/div/div[5]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

        # 確定新增
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#tabContentForm4 .btn-wm-purple"))
        ).click()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "儲存完畢" in alert_text:
            print("\033[32m填充題建立成功\033[0m")
        else:
            print("\033[31m填充題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        # 簡答----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab05"))
        ).click()

        random_cloze = generate_random_cloze()
        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[4])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_5 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm5"]/div/div[5]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm5"]/div/div[5]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm5"]/div/div[5]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm5"]/div/div[5]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm5"]/div/div[5]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

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
        else:
            print("\033[31m簡答題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        # 配合----------------------------
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "tab06"))
        ).click()

        random_cloze = generate_random_cloze()
        # iframes = driver.find_elements(By.TAG_NAME, "iframe")
        # driver.switch_to.frame(iframes[5])
        editable = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#topic_6 .ql-editor"))
        )
        script = f"arguments[0].innerHTML = '<p>自動化測試用：{nowdatetime}</p>';"
        driver.execute_script(script, editable)
        # driver.switch_to.default_content()

        # 選項
        time.sleep(5)
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)  
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        random_number = random.choice(['1', '2'])

        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[1]/div[2]/div[2]/input[1]').click() #題目提示A
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[1]/div[2]/div[2]/input[1]').send_keys("提示一")
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[1]/div[3]/div[2]/input[1]').click() #題目提示B
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[1]/div[3]/div[2]/input[1]').send_keys("提示二")

        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[2]/div[2]/div[2]/input[1]').click() #待選項目1
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[2]/div[2]/div[2]/input[1]').send_keys("選項一號")
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[2]/div[3]/div[2]/input[1]').click() #待選項目2
        driver.find_element(By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[2]/div[1]/div[2]/div[3]/div[2]/input[1]').send_keys("選項二號")    
        
        # 分類
        version_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[3]/div[2]/input[1]'))
        )
        version_input.click()
        version = generate_random_class()
        version_input.send_keys(version)

        volume_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[3]/div[2]/input[2]'))
        )
        volume_input.click()
        volume = generate_random_class()
        volume_input.send_keys(volume)

        chapter_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[3]/div[2]/input[3]'))
        )
        chapter_input.click()
        chapter = generate_random_class()
        chapter_input.send_keys(chapter)

        paragraph_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[3]/div[2]/input[4]'))
        )
        paragraph_input.click()
        paragraph = generate_random_class()
        paragraph_input.send_keys(paragraph)

        section_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tabContentForm6"]/div/div[5]/div[3]/div[2]/input[5]'))
        )
        section_input.click()
        section = generate_random_class()
        section_input.send_keys(section)

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
        
        else:
            print("\033[31m配合題建立失敗\033[0m")
            time.sleep(5)
        alert.accept()

        #回題庫維護
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//form[@id='tabContentForm1']//input[@value='回列表']"))
        ).click()
        print("回列表")

        # 每頁數量 
        page_num = driver.find_element(By.ID, "page_num_result")
        page_num.click()
        select = Select(page_num)
        options = {"每頁10筆":10, "每頁20筆":20, "每頁50筆":50, "每頁100筆":100}
        random_option_text = random.choice(list(options.keys()))
        random_option_number = options[random_option_text]
        select.select_by_visible_text(random_option_text)
        time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tbody")))
        tr_elements = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        print(len(tr_elements))
        if len(tr_elements) == random_option_number+3:
            print("\033[32m每頁顯示數量成功\033[0m")
        else:
            print("\033[31m每頁顯示數量錯誤\033[0m")

        # 重複取得排序元素
        def get_version_text(driver, xpath):
            retries = 3
            while retries > 0:
                try:
                    element = WebDriverWait(driver, 10).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )      
                    return element.text
                except Exception as e:
                    print(f"Error: {e}")
                    retries -= 1
                    time.sleep(2)
            return None

        # 排序
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(5)"))
        ).click()
        version1 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[5]')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(5)"))
        ).click()
        version2 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[5]')
        print(version1,version2)
        if int(version1) == 0 and int(version2) == 9:
            print("\033[32m主題 排序成功\033[0m")
        else:
            print("\033[31m主題 排序失敗\033[0m")

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(6)"))
        ).click()
        volume1 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[6]')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(6)"))
        ).click()
        volume2 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[6]')  
        if int(volume1) == 9 and int(volume2) == 0:
            print("\033[32m分類 排序成功\033[0m")
        else:
            print("\033[31m分類 排序失敗\033[0m")

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(7)"))
        ).click()
        chapter1 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[7]')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(7)"))
        ).click()
        chapter2 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[7]')
        if int(chapter1) == 0 and int(chapter2) == 9:
            print("\033[32m版 排序成功\033[0m")
        else:
            print("\033[31m版 排序失敗\033[0m")

        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(8)"))
        ).click()
        paragraph1 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[8]')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mainTable .wm-table-sort:nth-child(8)"))
        ).click()
        paragraph2 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[8]')
        if int(paragraph1) == 9 and int(paragraph2) == 0:
            print("\033[32m冊 排序成功\033[0m")
        else:
            print("\033[31m冊 排序失敗\033[0m")
        
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainTable"]/thead/tr/th[9]'))
        ).click()
        section1 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[9]')
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="mainTable"]/thead/tr/th[9]'))
        ).click()
        section2 = get_version_text(driver, '//*[@id="mainTable"]/tbody/tr[1]/td[9]')
        if int(section1) == 0 and int(section2) == 9:
            print("\033[32m章 排序成功\033[0m")
        else:
            print("\033[31m章 排序失敗\033[0m")
        
        # 題型搜尋
        time.sleep(2)
        type = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='divSearchPanel']//select[@name='type']"))
        )
        select = Select(type)
        select.select_by_visible_text("配合")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@id="isType"])[2]'))
        ).click()
        driver.execute_script("do_search_item()")
        if "自動化測試用" in driver.page_source:
            print("\033[32m勾選題型搜尋成功\033[0m")
        else:
            print("\033[31m勾選題型搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@id="isType"])[2]'))
        ).click()
        driver.execute_script("do_search_item()")
        if "[1231]" not in driver.page_source:
            print("\033[32m未勾選題型搜尋成功\033[0m")
        else:
            print("\033[31m未勾選題型搜尋失敗\033[0m")

        # 關鍵字搜尋
        time.sleep(5)
        keyword = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '(//input[@placeholder="請在此輸入搜尋的關鍵字"])[2]'))
        )
        keyword.click()
        keyword.send_keys("1231")
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@id="isFulltext"])[2]'))
        ).click()
        driver.execute_script("do_search_item()")
        if "[1231]" in driver.page_source:
            print("\033[32m勾選關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m勾選關鍵字搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '(//input[@id="isFulltext"])[2]'))
        ).click()
        driver.execute_script("do_search_item()")
        if "[1231]" not in driver.page_source:
            print("\033[32m未勾選關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m未勾選關鍵字搜尋失敗\033[0m")

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

 