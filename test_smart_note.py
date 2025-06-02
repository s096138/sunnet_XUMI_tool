from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementClickInterceptedException,
    StaleElementReferenceException,
    ElementNotInteractableException,
    WebDriverException
)
from pywinauto import Application

from selenium import webdriver
from datetime import datetime
import time
import os

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

download_directory = "c:\\Users\\SGQA2\\Downloads"
options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": download_directory,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": False,  # 允許不安全下載

}
options.add_experimental_option("prefs", prefs)
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--disable-gpu')
options.add_argument('--disable-blink-features=AutomationControlled')

def get_downloaded_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

def test_smart_note(driver):
    try:
        print("測試：首頁-會員專區-智匯筆記")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'智匯筆記')]"))
        ).click()
        time.sleep(2)
        if "歡迎來到智匯筆記" in driver.page_source:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增筆記本 +')]"))
            ).click()
            time.sleep(2)
            input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='title-for-files']"))
            )
            input.click()
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='cgust-dialog__title ng-star-inserted']"))
            ).click()
            time.sleep(2)
            if "此欄必填" in driver.page_source:
                print("\033[32m筆記本名稱必填\033[0m")
            else:
                print("\033[31m筆記本名稱不必填\033[0m")
            input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='title-for-files']"))
            )
            input.send_keys("自動化測試用")
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
            ).click()
        time.sleep(2)
        if "搜尋筆記本名稱" in driver.page_source:
            print("\033[32m進入智匯筆記成功\033[0m")
            if "自動化測試用" not in driver.page_source:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'新增筆記本')]"))
                ).click()
                time.sleep(2)
                input = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@id='title-for-files']"))
                )
                input.click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[@class='cgust-dialog__title ng-star-inserted']"))
                ).click()
                time.sleep(2)
                if "此欄必填" in driver.page_source:
                    print("\033[32m筆記本名稱必填\033[0m")
                else:
                    print("\033[31m筆記本名稱不必填\033[0m")
                input = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@id='title-for-files']"))
                )
                input.send_keys("自動化測試用")
                time.sleep(2)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
                ).click()
        else:
            print("\033[31m進入智匯筆記失敗\033[0m")
        
        # 驗證筆記本
        time.sleep(2)
        if "自動化測試用" in driver.page_source and nowdatetime in driver.page_source:
            print("\033[32m新增筆記本成功\033[0m")
        else:
            print("\033[31m新增筆記本失敗\033[0m")
        
        # 新增標籤
        time.sleep(2)
        if "自動化測試標籤" in driver.page_source:
            print("\033[32m標籤已存在\033[0m")         
        else:
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
            ).click()
            time.sleep(2)
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'標籤')]"))
            ).click()
            time.sleep(2)
            if "自動化測試標籤" in driver.page_source:
                print("\033[32m標籤已存在\033[0m")
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'自動化測試標籤')]"))
                ).click()
            else:
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'管理標籤')]"))
                ).click()
                time.sleep(2)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'新增標籤')]"))
                ).click()
                title = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='title']"))
                )
                title.click()
                title.click()
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'標籤管理')]"))
                ).click()
                time.sleep(2)
                if "此欄必填" in driver.page_source:
                    print("\033[32m標籤名稱必填\033[0m")
                else:
                    print("\033[31m標籤名稱不必填\033[0m")
                time.sleep(2)
                title = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//input[@formcontrolname='title']"))
                )
                title.click()
                title.send_keys("自動化測試標籤")    
                WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
                ).click()
                time.sleep(2)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
                ).click()
                time.sleep(2)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'標籤')]"))
                ).click()
                time.sleep(2)
                WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'自動化測試標籤')]"))
                ).click()
        driver.refresh()
        time.sleep(2)           
        if "自動化測試標籤" in driver.page_source:
            print("\033[32m新增標籤成功\033[0m")
        else:
            print("\033[31m新增標籤失敗\033[0m")

        # 筆記列表
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試用')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source and "輸入關鍵字搜尋" in driver.page_source:
            print("\033[32m進入筆記列表成功\033[0m")
        else:
            print("\033[31m進入筆記列表失敗\033[0m")
        
        # 新增筆記
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='card-actions']"))
        ).click()
        time.sleep(2)
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='note-title']"))
        )
        title.click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='cgust-dialog__title ng-star-inserted']"))
        ).click()
        time.sleep(2)
        if "此欄必填" in driver.page_source:
            print("\033[32m筆記主旨必填\033[0m")
        else:
            print("\033[31m筆記主旨不必填\033[0m")
        title = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='note-title']"))
        )
        title.click()
        title.send_keys("114年辦公日曆表")
        WebDriverWait(driver, 20).until(    
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'選擇檔案')]"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\114年辦公日曆表.pdf") #可替換
        time.sleep(2)
        dlg['開啟'].click()

        # 智能摘要
        time.sleep(5)
        scroll_bottom(driver)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'智能摘要')]"))
        ).click()
        time.sleep(10) # 等待生成
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'儲存')]"))
        ).click()
        time.sleep(2) 
        driver.refresh() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試用')]"))
        ).click()
        time.sleep(2)
        article_text = driver.find_element(By.XPATH, "//article[@class='notePage__body embedded-html']").text
        if article_text:
            print("\033[32m生成內容成功\033[0m")
        else:
            print("\033[31m生成內容失敗\033[0m")         
        time.sleep(2) 
        if "114年辦公日曆表" in driver.page_source:
            print("\033[32m新增筆記成功\033[0m")
        else:
            print("\033[31m新增筆記失敗\033[0m")

        # 編輯筆記
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'114年辦公日曆表')]"))
        ).click()
        time.sleep(2)
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[contains(@title, 'editor')]"))
        )
        driver.switch_to.frame(iframe)
        time.sleep(2)
        content = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//body[contains(@aria-label, 'editor')]//p"))
        )
        content.click()
        content.clear()
        content.send_keys("自動化測試用筆記") 
        time.sleep(2)
        driver.switch_to.default_content()
        time.sleep(2)
        # driver.execute_script("document.body.click();")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        ).click()
        time.sleep(2)
        driver.refresh() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試用')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用筆記" in driver.page_source:
            print("\033[32m編輯筆記成功\033[0m")
        else:
            print("\033[31m編輯筆記失敗\033[0m")

        # 更多操作-音檔
        time.sleep(2)
        initial_files = get_downloaded_files(download_directory)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'音檔')]"))
        ).click()
        time.sleep(10) # 等待生成
        final_files = get_downloaded_files(download_directory)
        time.sleep(2)
        if len(final_files) > len(initial_files):
            print("\033[32m音檔下載成功\033[0m")
        else:
            print("\033[31m音檔下載失敗\033[0m")

        # 更多操作-置頂
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='ng-star-inserted']"))
        ).click()
        time.sleep(2)
        if WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//mat-icon[@aria-label='置頂筆記']"))
        ):
            print("\033[32m置頂筆記成功\033[0m")
        else:
            print("\033[31m置頂筆記失敗\033[0m")

        # AI生成題目
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//mat-checkbox[contains(@class, 'mat-checkbox mat-accent')]//input[@type='checkbox']")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        scroll_bottom(driver)
        elements = driver.find_elements(By.TAG_NAME, "span")
        selected_element = next((el for el in elements if '已選取' in el.text), None)
        text_value = selected_element.text if selected_element else ''
        time.sleep(2)
        if "已選取 1 個來源" in text_value:
            print("\033[32m正確勾選、來源數量+1\033[0m")
        else:
            print("\033[31m未正確勾選、來源數量錯誤\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'AI生成題目')]"))
        ).click()
        time.sleep(10) # 等待生成
        if "請幫我生成練習題目" in driver.page_source:
            print("\033[32mAI生成題目中\033[0m")
            time.sleep(5)
            result = driver.execute_script("""
            return document.body.innerHTML.includes("當然沒問題!交給我吧!") &&
                document.body.innerHTML.includes("題目已經準備好囉!來練習看看吧!");
            """)
            time.sleep(15) # 五秒會失敗
            if result:
                print("\033[32mAI生成題目成功\033[0m")
            else:
                print("\033[31mAI生成題目失敗\033[0m")
            time.sleep(2)
        else:
            print("\033[31mAI生成題目失敗\033[0m")

        # 開始練習
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'開始練習')]"))
        ).click()
        time.sleep(2)
        if "開始練習吧!" in driver.page_source:
            print("\033[32m練習題顯示成功\033[0m")
        else:
            print("\033[31m練習題顯示失敗\033[0m")
        practice_time = driver.find_element(By.XPATH, "//span[@class='cgust-dialog__practiceTtime']").text
        title_content = practice_time.split("標題:")[1].strip() if "標題:" in practice_time else ""
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'我完成了!')]"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'關閉')]"))
        ).click()

        # 收合
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='展開對話']"))
        ).click()
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//mat-checkbox[contains(@class, 'mat-checkbox-checked')]")
        driver.execute_script("arguments[0].click();", element)
        driver.execute_script("var event = new Event('change', { bubbles: true }); arguments[0].dispatchEvent(event);", element)
        time.sleep(2)
        elements = driver.find_elements(By.TAG_NAME, "span")
        selected_element = next((el for el in elements if '已選取' in el.text), None)
        text_value = selected_element.text if selected_element else ''
        time.sleep(2)
        if "已選取" not in text_value: 
            print("\033[32m取消勾選、且來源數量-1\033[0m")
            time.sleep(2)
            if driver.find_element(By.XPATH, "//button[contains(text(),'AI生成題目')]").get_attribute("disabled"):
                print("\033[32mAI生成題目按鈕disabled\033[0m")
            else:
                print("\033[31mAI生成題目按鈕enabled\033[0m")
        else:
            print("\033[31m未取消勾選、來源數量錯誤\033[0m")

        # # 回列表
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
        # ).click()
        # driver.refresh()
        # time.sleep(2)
        # if "練習筆記本" in driver.page_source and "自動化測試用" in driver.page_source:
        #     print("\033[32m回列表成功\033[0m")
        # else:
        #     print("\033[31m回列表失敗\033[0m")
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'練習筆記本')]"))
        # ).click()
        time.sleep(2)
        driver.refresh() 
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'自動化測試用')]"))
        ).click()
        time.sleep(2)
        if "練習題" in driver.page_source:
            print("\033[32m練習紀錄生成成功\033[0m")
        else:
            print("\033[31m練習紀錄生成失敗\033[0m")
        time.sleep(2)
        element = driver.find_element(By.XPATH, "//div[contains(text(), '練習題') and contains(@class, 'card-title')]")
        element.click()
        time.sleep(2)
        if "成績" in driver.page_source and "查看詳解" in driver.page_source:
            print("\033[32m查看練習紀錄成功\033[0m")
        else:
            print("\033[31m查看練習紀錄失敗\033[0m")

        # 關閉
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='關閉圖示']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'回列表')]"))
        ).click()

        # 搜尋
        time.sleep(2)
        input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='搜尋筆記本名稱']"))
        )
        input.click()
        input.send_keys("自動化測試用")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source and "自動化測試主課程" not in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")
        time.sleep(2)
        input = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='搜尋筆記本名稱']"))
        )
        driver.execute_script("arguments[0].value = '';", input)
        driver.refresh()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'搜尋')]"))
        ).click()
        time.sleep(2)
        if "自動化測試用" in driver.page_source and "自動化測試主課程" in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")

        #  更多操作-刪除
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'刪除')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'確定')]"))
        ).click()
        time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='更多操作']//*[name()='svg']"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'刪除')]"))
        # ).click()
        # time.sleep(2)
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'確定')]"))
        # ).click()
        time.sleep(2)
        if "自動化測試用" not in driver.page_source and "自動化測試主課程" in driver.page_source:
            print("\033[32m刪除筆記本成功\033[0m")
        else:
            print("\033[31m刪除筆記本失敗\033[0m")

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