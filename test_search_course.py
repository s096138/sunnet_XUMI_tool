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
from selenium_driver import initialize_driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

def test_search_course(driver):
    try:       
        print("測試：首頁-進階搜尋")
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='搜尋'] mat-icon[aria-label='放大鏡圖示']"))
        ).click()
        time.sleep(2)
        if "課程狀態" in driver.page_source:
            print("\033[32m進入進階搜尋成功\033[0m")
        else:
            print("\033[31m進入進階搜尋失敗\033[0m")
        
        # 搜尋
        first_row = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "cgust-course-card:nth-child(1) a:nth-child(1) div:nth-child(2) p:nth-child(1)"))
        ).text
        time.sleep(2)
        keyword = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='請輸入關鍵字搜尋']"))
        )
        keyword.send_keys("2026")
        keyword.send_keys(Keys.ENTER)
        time.sleep(2)
        if "2026年的課程" in driver.page_source:
            print("\033[32m關鍵字搜尋成功\033[0m")
        else:
            print("\033[31m關鍵字搜尋失敗\033[0m")
        keyword.clear()
        keyword.send_keys(" ")
        keyword.send_keys(Keys.ENTER)
        time.sleep(2)
        if first_row in driver.page_source:
            print("\033[32m空白搜尋成功\033[0m")
        else:
            print("\033[31m空白搜尋失敗\033[0m")

        # 課程狀態下拉選單
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "mat-select-value-1"))
        ).click()
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-option-5 > .mat-option-text"))
        ).click()
        state1 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-option-5 > .mat-option-text"))
        )
        driver.execute_script("arguments[0].click();", state1)
        time.sleep(2)
        if "2026年的課程" in driver.page_source:
            print("\033[32m課程狀態搜尋成功\033[0m")
        else:
            print("\033[31m課程狀態搜尋失敗\033[0m")
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "mat-select-value-1"))
        ).click()
        state2 = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#mat-option-2 > .mat-option-text"))
        )
        driver.execute_script("arguments[0].click();", state2)
    
        # 群組分類
        group = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, "mat-select-value-3"))
        )
        driver.execute_script("arguments[0].click();", group)
        time.sleep(2)
        options = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option .mat-option-text"))
        )
        found_course = False
        for i in range(len(options)):
            if i > 0:  # 第二次後須重新打開下拉選單
                group = WebDriverWait(driver, 30).until(
                    EC.element_to_be_clickable((By.ID, "mat-select-value-3"))
                )
                driver.execute_script("arguments[0].click();", group)
                time.sleep(2)
                options = WebDriverWait(driver, 20).until(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "mat-option .mat-option-text"))
                )
            option_text = options[i].text
            driver.execute_script("arguments[0].click();", options[i])
            
            actions = ActionChains(driver)
            actions.move_by_offset(0, 0).click().perform()
            time.sleep(2)
            group_text = driver.execute_script('''
                const element = document.querySelector('mat-icon[svgicon="home:landmark"]').parentElement;
                return element.textContent.split('群組分類')[1].trim();
            ''') 
            time.sleep(2)
            if "找不到符合的課程" not in driver.page_source:
                found_course = True
                print(f"\033[32m群組分類搜尋成功：測試群組 '{option_text}'\033[0m")
                break
            else:
                print(f"\033[33m群組 '{option_text}' 找不到課程，嘗試下一個群組\033[0m")
        if not found_course:
            print("\033[31m所有群組分類都找不到課程\033[0m")
            return  

        # 進入課程
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".col-span-full:nth-child(1) > .card .ng-star-inserted:nth-child(2)"))
        ).click()
        time.sleep(2)
        if "課程簡介" in driver.page_source:
            print("\033[32m進入課程成功\033[0m")
        else:
            print("\033[31m進入課程失敗\033[0m")  

        # 回首頁
        time.sleep(2)
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()
        print('回首頁')

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
