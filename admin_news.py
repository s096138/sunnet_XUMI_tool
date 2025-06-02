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
from pywinauto import Application
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
from dotenv import load_dotenv

nowdatetime = datetime.now().strftime("%Y-%m-%d")
nowmonth = datetime.now().strftime("%Y-%m")

def admin_news(driver):
    try:
        print("測試：管理者環境-公告管理-最新消息")
        menu_expanded(driver, "公告管理", "最新消息")
        time.sleep(2)
        if "瀏覽次數" in driver.page_source:
            print("\033[32m進入最新消息成功\033[0m")
        else:
            print("\033[31m進入最新消息失敗\033[0m") 

        # 新增
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'btn_add'))
        ).click()
        driver.execute_script("checkData()")
        time.sleep(2)
        if "標題請務必填寫" in driver.page_source:
            print("\033[32m未填標題不能新增\033[0m")
        else:
            print("\033[31m未填標題可以新增\033[0m")

        name = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="subject"]'))
        )
        name.click()
        name.send_keys("自動化測試用")
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
        day2.send_keys(f"{nowmonth}-01")
        time.sleep(2)
        # 結束日期不可小於起始日期
        driver.execute_script("checkData()")
        if "結束日期不可小於起始日期" in driver.page_source:
            print("\033[32m結束日期不可小於起始日期\033[0m")
            day2.click()
            day2.clear()
            day2.send_keys(nowdatetime)
        else:
            print("\033[31m結束日期可以小於起始日期\033[0m")
        # 未填本文
        driver.execute_script("checkData()")
        if "本文請務必填寫" in driver.page_source:
            print("\033[32m未填本文不可新增\033[0m")
        else:
            print("\033[31m未填本文可以新增\033[0m")

        # driver.switch_to.frame(0)
        # WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, '//html'))
        # ).click()
        editable_body = driver.find_element(By.CSS_SELECTOR, ".ql-editor")
        driver.execute_script("arguments[0].innerHTML = '<p>自動化測試用</p>'", editable_body)
        # driver.switch_to.default_content()
        time.sleep(2)
        photo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[3]/div/div[2]/button'))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\xumi@1x.png") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)

        # 確定
        driver.execute_script("checkData()")
        time.sleep(2)
        if "自動化測試用" in driver.page_source:
            print("\033[32m新增最新消息成功\033[0m")
        else:
            print("\033[31m新增最新消息失敗\033[0m")

        # 修改
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'自動化測試用')]/following-sibling::td/span[@class='material-icons-outlined opacity-60 studAction' and text()='edit']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[1]/div/input'))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[1]/div/input'))
        ).clear()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="fmEdit"]/div[1]/div/input'))
        ).send_keys("自動化測試修改用")
        driver.execute_script("checkData()")
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m修改最新消息成功\033[0m")
        else:
            print("\033[31m修改最新消息失敗\033[0m")

        # 轉寄
        load_dotenv()
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//tbody/tr[1]/td[8]/span[1]'))
        ).click()
        alert = driver.switch_to.alert
        alert.send_keys(os.getenv("TEST_EMAIL"))
        alert.accept()
        time.sleep(2)
        alert = driver.switch_to.alert
        alert_text = alert.text
        if "文章已寄出" in alert_text:
            print("\033[32m轉寄文章成功\033[0m")
        else:
            print("\033[31m轉寄文章失敗\033[0m")
        alert.accept()

        # 刪除
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//td[contains(text(),'自動化測試修改用')]/following-sibling::td/span[@class='material-icons-outlined opacity-60 studAction' and text()='delete']"))
        ).click()

        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "您確定要刪除嗎?"
        alert.accept()

        time.sleep(2)
        alert = driver.switch_to.alert
        assert alert.text == "刪除成功"
        alert.accept()

        time.sleep(2)
        if "自動化測試修改用" not in driver.page_source:
            print("\033[32m刪除最新消息成功\033[0m")
        else:
            print("\033[31m刪除最新消息失敗\033[0m")

        # 另開視窗
        driver.execute_script("window.open('');")
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        driver.get(f"https://www.mailinator.com/v4/public/inboxes.jsp?to=yyytest")
        time.sleep(2)
        if "自動化測試修改用" in driver.page_source:
            print("\033[32m轉寄最新消息收到信件\033[0m")
        else:
            print("\033[31m轉寄最新消息未收到信件\033[0m")
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