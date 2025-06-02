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

def test_banner(driver):
    try:
        print("測試：首頁-Banner")
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']"))
        ).click()
        original_window_handles = driver.window_handles
        time.sleep(2)
        # 等待直到元素的 class 包含 'swiper-slide-active'
        banner = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'swiper-slide swiper-slide-active')]//img[@alt='同儕互評']"))
        )
        # 點擊 banner
        if banner.is_enabled() and banner.is_displayed():
            banner.click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
        new_window_handles = driver.window_handles
        time.sleep(2)
        if len(new_window_handles) > len(original_window_handles):
            new_window_handle = list(set(new_window_handles) - set(original_window_handles))[0]
            driver.switch_to.window(new_window_handle)
            
            # 檢查新分頁的網址
            time.sleep(2)
            current_url = driver.current_url
            expected_url = "https://www.google.com/"
            if current_url == expected_url:
                print("\033[32m點選Banner並跳轉成功一次\033[0m")
            else:
                print("\033[31m點選Banner失敗\033[0m")
        driver.close()
        driver.switch_to.window(original_window_handles[0])
        
        time.sleep(2)
        WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@class='swiper-pagination-bullet swiper-pagination-bullet-active']"))
        ).click()
        original_window_handles = driver.window_handles
        # 等待直到元素的 class 包含 'swiper-slide-active'
        banner = WebDriverWait(driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'swiper-slide swiper-slide-active')]//img[@alt='愛上互動']"))
        )
        # 點擊 banner
        if banner.is_enabled() and banner.is_displayed():
            banner.click()
        WebDriverWait(driver, 10).until(EC.new_window_is_opened(original_window_handles))
        new_window_handles = driver.window_handles

        if len(new_window_handles) > len(original_window_handles):
            new_window_handle = list(set(new_window_handles) - set(original_window_handles))[0]
            driver.switch_to.window(new_window_handle)
    
            # 檢查新分頁的網址
            time.sleep(2)
            current_url = driver.current_url
            expected_url = "https://www.sun.net.tw/?p=product_isunfudon"
            if current_url == expected_url:
                print("\033[32m點選Banner並跳轉成功二次\033[0m")
            else:
                print("\033[31m點選Banner失敗\033[0m")

        driver.close()
        driver.switch_to.window(original_window_handles[0])

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
