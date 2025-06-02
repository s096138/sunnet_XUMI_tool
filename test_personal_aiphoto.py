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
from google.cloud import vision
from pywinauto import Application
import base64
import os 
import requests
import time

from test_news import scroll_bottom
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/SGQA2/Desktop/Auto/qa-test-439407-8c2381db526d.json"

def is_base64_image(image_src):
    return image_src.startswith("data:image")

# def download_image_via_webdriver(image_element, download_path):
#     image_src = image_element.get_attribute("src")
#     if is_base64_image(image_src):
#         image_data = image_src.split(",")[1]
#         with open(download_path, "wb") as f:
#             f.write(base64.b64decode(image_data))
#         print(f"圖片已保存至: {download_path}")
#         return download_path
#     else:
#         print(f"無法處理圖片 URL: {image_src}")
#         return None
    
def download_image_with_cookies(image_src, driver):
    # 從 WebDriver 獲取 cookies
    cookies = driver.get_cookies()
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    # 使用 session 發送請求
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = session.get(image_src, headers=headers)
    if response.status_code == 200:
        with open("downloaded_image.jpg", "wb") as file:
            file.write(response.content)
        print("圖片下載成功！")
        return "downloaded_image.jpg"
    else:
        print(f"下載失敗，HTTP 狀態碼: {response.status_code}")
        return None

def analyze_image(image_src, driver=None):
    download_path = "downloaded_image.jpg"

    if is_base64_image(image_src):
        # 如果是 base64 編碼的圖片，使用 WebDriver 保存圖片
        if download_path is None:
            return False
    else:
        # 如果不是 base64 編碼，嘗試通過 cookies 下載圖片
        if driver:
            download_path = download_image_with_cookies(image_src, driver)
            if not download_path:
                return False
        else:
            # 使用 HTTP 直接下載圖片
            response = requests.get(image_src)
            if response.status_code != 200:
                print(f"下載失敗，HTTP 狀態碼: {response.status_code}")
                return False
            with open(download_path, "wb") as f:
                f.write(response.content)
            print(f"圖片已下載至: {download_path}")

    # 初始化 Google Cloud Vision 客戶端
    client = vision.ImageAnnotatorClient()

    # 打開已下載的圖片文件
    with open(download_path, "rb") as image_file:
        content = image_file.read()

    # 將圖片內容傳遞給 Vision API
    image = vision.Image(content=content)

    # 調用 Vision API 進行標籤檢測
    response = client.label_detection(image=image)

    # 確認 API 是否返回錯誤
    if response.error.message:
        raise Exception(f"API Error: {response.error.message}")

    # 檢查是否有返回任何標籤
    labels = response.label_annotations
    if not labels:
        print("No labels detected.")
        return False

    # 顯示檢測的標籤
    print('Labels in the image:')
    for label in labels:
        print(f'{label.description} (score: {label.score})')

    # 檢查是否有符合 "cat" 和 "cartoon" 等關鍵字的標籤
    for label in labels:
        if 'cat' in label.description.lower() or 'cartoon' in label.description.lower():
            print("\033[32mAI生成人像成功\033[0m")
            return True

    print("\033[31mAI生成人像失敗\033[0m")
    return False

def test_personal_aiphoto(driver):
    try:
        # print(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
        print("測試：首頁-會員專區-個人資料(AI生成人像)")
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "mat-button-wrapper"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[span/text()='個人資料']"))
        ).click()
        time.sleep(2)
        if "個人資料" in driver.page_source:
            print("\033[32m進入個人資料成功\033[0m")
        else:
            print("\033[31m進入個人資料失敗\033[0m")

        # 魔法棒
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//label[2]/span"))
        ).click()
        time.sleep(2)
        scrollable_element = driver.find_element(By.CLASS_NAME, "cgust-dialog__content")
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scrollable_element)
        time.sleep(2)

        # 風格選項
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='style']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'漫畫')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='hairStyle']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'中分短髮')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='hairColor']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'黑色')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='wear']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'學生制服')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='action']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'比YA')]"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-select[@formcontrolname='background']"))
        ).click()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'學校')]"))
        ).click()
        time.sleep(2)

        # 等待生成
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator btn btn--primary upload-dialog__btn mat-button mat-button-base']"))
        ).click()
        time.sleep(30) # 等待生成
        
        # image_src = ("https://wm6-dev-svn.sgrd.elearn.com.tw//user/j/o/joy09/image_temp/tmp_image.jpg")
        # analyze_image(image_src, driver)

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator btn btn--primary upload-dialog__btn mat-button mat-button-base ng-star-inserted']"))
        ).click()        

        try:
            slider_element = driver.find_element(By.XPATH, "//input[@class='cr-slider' and @type='range']")
            print("\033[32m下一步成功：調整尺寸中\033[0m")
        except NoSuchElementException:
            print("\033[31m下一步失敗\033[0m")        
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='mat-focus-indicator btn btn--primary upload-dialog__btn mat-button mat-button-base']"))
        ).click() 
        time.sleep(2)
        if "" in driver.page_source:
            print("\033[32m更換AI生成人像成功\033[0m")
        else:
            print("\033[31m更換AI生成人像失敗\033[0m")

        # 復原
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//mat-icon[@aria-label='編輯圖示']"))
        ).click()
        time.sleep(2)
        app = Application(backend="win32").connect(title_re=".*開啟.*")
        dlg = app.window(title_re=".*開啟.*")
        dlg.set_focus()
        dlg['Edit'].type_keys(r"C:\Users\SGQA2\Downloads\兔子.jpg") #可替換
        time.sleep(2)
        dlg['開啟'].click()
        time.sleep(2)   
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'確定')]"))
        ).click()
        time.sleep(2) 
        print("復原")

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