from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException



def solveCaptcha_pro(driver):
    while True:
        try:
            # sleep(3)
            # g_recaptcha = driver.find_elements(By.CLASS_NAME, 'my-10')[0]
            
            driver.implicitly_wait(10)
            outerIframe = driver.find_element(By.TAG_NAME, 'iframe')
            sleep(2)
            outerIframe.click()
            break
        except:
            print("waiting to load captcha")

    while True:
        try:
            while True:
                try:
                    iframe = driver.find_element(By.XPATH, "//iframe[@title='recaptcha challenge expires in two minutes']")
                    driver.switch_to.frame(iframe)
                    break
                except Exception as err:
                    print("recaptcha challenge expires in two minutes")
            while True:
                sleep(1)
                try:
                    # driver.switch_to.frame(iframes)
                    # db = driver.find_element(By.XPATH, '/html/body/div/div/div[3]/div[2]/div[1]/div[1]/div[4]//button')
                    db = driver.find_element(By.CLASS_NAME, "help-button-holder")
                    db.click()
                    sleep(7)
                    try:
                        driver.implicitly_wait(0.1)
                        reloadbtn = driver.find_element(By.ID, "recaptcha-reload-button")
                        reloadbtn.click()
                    except:
                        break
                except Exception as e:
                    print('captcha solve btn not found')
                    # outerIframe = driver.find_element(By.TAG_NAME, 'iframe').click()
    
    
            print("Captcha Solved")
            break
        except Exception as err:
            print(err)


