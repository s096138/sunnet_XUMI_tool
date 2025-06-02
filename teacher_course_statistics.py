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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from pywinauto import Application
from menu_expanded import menu_expanded
import autoit
import time
import os
from selenium import webdriver

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

def teacher_course_statistics(driver):
    try:
        print("測試：辦公室-人員管理-到課統計")
        time.sleep(2)
        menu_expanded(driver, "人員管理", "到課統計")
        time.sleep(2)
        if "登入次數" in driver.page_source:
            print("\033[32m進入到課統計成功\033[0m")
        else:
            print("\033[31m進入到課統計失敗\033[0m")

        # 切換列表身分
        time.sleep(2)
        select_element  = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@id='role']"))
        )
        select = Select(select_element)
        select.select_by_visible_text("全部")

        # # 閱讀時數
        # time.sleep(2)
        # contentmain_elements = WebDriverWait(driver, 20).until(
        #     EC.presence_of_all_elements_located((By.XPATH, "//div[@class='contentmain p-4']//table[@id='studentListTable']"))
        # )
        # for person in contentmain_elements:
        #     read_element = person.find_element(By.XPATH, "//td[normalize-space()='yyytest']")
        #     if read_element:
        #         read_button = person.find_element(By.XPATH, "//a[contains(@href, 'viewDetail(4,')]")
        #         read_button.click()
        #         break

        # # 切換視窗
        # time.sleep(2)
        # WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        # driver.switch_to.window(driver.window_handles[1])
        # time.sleep(2)
        # # 設定 Chrome 選項
        # download_dir = r'C:\Users\SGQA2\Downloads'
        # chrome_options = Options()
        # # 設定 Chrome 的下載選項
        # prefs = {
        #     "download.default_directory": download_dir,
        #     "download.prompt_for_download": False,
        #     "download.directory_upgrade": True,
        #     "safebrowsing.enabled": True
        # }
        # time.sleep(1)
        # chrome_options.add_experimental_option("prefs", prefs)
        # download_button = driver.find_element(By.XPATH, "//button[@id='btn_add' and contains(text(), '下載全部')]")
        # download_button.click()
        # time.sleep(2)
        # if os.path.exists(download_dir) and os.path.getsize(download_dir) > 0:
        #     print("\033[32m下載閱讀時數成功\033[0m")
        # else:
        #     print("\033[31m下載閱讀時數失敗或文件不存在\033[0m")
        # WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, "//button[text()='關閉']"))
        # ).click()
        # driver.switch_to.window(driver.window_handles[0])
        
        # 上站動作
        contentmain_elements = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='contentmain p-4']//table[@id='studentListTable']"))
        )
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//tr[td[contains(text(),'yyytest')]]//a[contains(@href, 'viewLog(')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(2)
        if "yyytest-上站動作" in driver.page_source:
            print("\033[32m點選上站動作成功\033[0m")
        else:
            print("\033[31m點選上站動作失敗\033[0m")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='關閉']"))
        ).click()
        driver.switch_to.window(driver.window_handles[0])

        # 匯出本頁資料
        time.sleep(2)
        initial_files = get_downloaded_files(download_directory)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='form-check pe-5']//input[@id='sysRadioBtn2']"))
        ).click()
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'匯出本頁資料')]"))
        ).click()
        time.sleep(2)
        final_files = get_downloaded_files(download_directory)
        time.sleep(2)
        if len(final_files) > len(initial_files):
            print("\033[32m匯出本頁資料成功\033[0m")
        else:
            print("\033[31m匯出本頁資料失敗或文件不存在\033[0m")

        # 寄信給本頁勾選人員
        checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@value='yyytest']"))
        )
        driver.execute_script("arguments[0].click();", checkbox)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'寄信給本頁勾選人員')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "recipients"))
        )
        recipients = driver.find_element(By.ID, "recipients").text

        # 檢查收件者
        contains = 'yyytest' in recipients
        if contains:
            print("\033[32m勾選寄信人員成功\033[0m")
        else:
            print("\033[31m勾選寄信人員失敗\033[0m")

        # 主旨
        subject = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'subject'))
        )
        subject.send_keys('自動化測試用')

        # 內容
        # WebDriverWait(driver, 20).until(
        #     EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//iframe[@title='編輯器, content']"))
        # )
        editor_body = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.ql-editor"))
        )
        editor_body.send_keys('自動化測試用')
        # driver.switch_to.default_content()

        # 附檔
        WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.add-attachment-btn"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)
        if "蛙蛙.jpg" in driver.page_source:
            print("\033[32m附檔成功\033[0m")
        else:
            print("\033[31m附檔失敗\033[0m")

        # 刪除附檔
        attachment_items = driver.find_elements(By.ID, "attachment-div")
        for item in attachment_items:
            if '蛙蛙.jpg' in item.text:
                # 找到並點擊刪除按鈕
                remove_button = item.find_element(By.CLASS_NAME, 'remove-attachment')
                remove_button.click()
                print("\033[32m刪除附檔成功\033[0m")
                break
        time.sleep(2)
        WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.add-attachment-btn"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\蛙蛙.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(5)

        # 發送
        send_mail_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "send_mail"))
        )
        driver.execute_script("arguments[0].click();", send_mail_button)
        send_result_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'確定')]"))
        )
        driver.execute_script("arguments[0].click();", send_result_button)

        # 另開視窗
        time.sleep(10)
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m寄信給本頁人員成功\033[0m")
        else:
            print("\033[31m寄信給本頁人員失敗\033[0m")
        driver.close()
        driver.switch_to.window(windows[0])
        time.sleep(2)
        
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
