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
import time
from selenium_driver import initialize_driver


def test_featured_courses(driver):
    try:
        print("測試：首頁-精選課程")
        time.sleep(2)
        title = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swiper.swiper-coverflow.swiper-3d.swiper-initialized.swiper-horizontal.swiper-pointer-events"))
        )
        if title:
            driver.execute_script("arguments[0].scrollIntoView(true);", title)
        else:
            print("\033[31m未找到元素，請檢查元素定位\033[0m")
        time.sleep(2)
        if "精選課程" in driver.page_source:
            print("\033[32m滾動到精選課程成功\033[0m")
        else:
            print("\033[31m滾動到精選課程失敗\033[0m")

        # 熱門課程
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),' 熱門課程 ')]"))   
        ).click()
        time.sleep(2)
        if "測試課程" in driver.page_source:
            print("\033[32m切換熱門課程成功\033[0m")
        else:
            print("\033[31m切換熱門課程失敗\033[0m")
        
        # 最新課程
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),' 最新課程 ')]")) 
        ).click()
        time.sleep(2)
        if "2026年的課程" in driver.page_source:
            print("\033[32m切換最新課程成功\033[0m")
        else:
            print("\033[31m切換最新課程失敗\033[0m")

        # 點選課程
        time.sleep(2)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swiper-slide-next .card img")) 
        ).click()
        time.sleep(2)
        if "課程簡介" in driver.page_source:
            print("\033[32m點選課程成功\033[0m")
        else:
            print("\033[31m點選課程失敗\033[0m")

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "header__logo"))
        ).click()

        # 左右移動
        time.sleep(2)
        title = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".swiper.swiper-coverflow.swiper-3d.swiper-initialized.swiper-horizontal.swiper-pointer-events"))
        )
        if title:
            driver.execute_script("arguments[0].scrollIntoView(true);", title)
        else:
            print("\033[31m未找到元素，請檢查元素定位\033[0m")
        time.sleep(2)
        right = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//section[@id='landing-page-courses']/div/div/swiper/div[2]"))    
        )
        right.click()
        right.click()
        if right:
            print("\033[32m右滑課程成功\033[0m")
        else:
            print("\033[31m右滑課程失敗\033[0m")
        time.sleep(2)
        left = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//section[@id='landing-page-courses']/div/div/swiper/div")) 
        )
        left.click()
        left.click()
        if right:
            print("\033[32m左滑課程成功\033[0m")
        else:
            print("\033[31m左滑課程失敗\033[0m")
        time.sleep(2)

        # 回首頁
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
