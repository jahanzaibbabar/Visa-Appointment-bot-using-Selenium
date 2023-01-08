try:
    import time
    import os
    from selenium import webdriver
    from selenium.webdriver import Chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.chrome.service import Service
    from time import sleep
    from captcha_bypass import solveCaptcha_pro
    # print('all module are loaded')

except Exception as e:
    print("\nRequirements are not installed!")
    print("Error ->>>: {} ".format(e))
    exit()


# ***************** Functions *****************
def get_driver(is_proxy):

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-dev-shm-usage')
    
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-infobars")
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')
    # options.add_argument('--disk-cache-size=0')

    options.add_extension('ext.crx')
    if is_proxy.lower() == 'true':
        options.add_extension('ext_v.crx')

    return options


def use_proxy(driver):

    driver.get("chrome-extension://majdfhpaihoncoakbjgbdhglocklcgno/html/foreground.html")

    # driver.get("chrome-extension://omghfjlpggmjjaagoclmmobgdodcjboh/popup/popup.html")
    # sleep(5)
    # while True:
        # try:
        #     # driver.find_element(By.XPATH, "//*[contains(text(),  'OFF')]").click()
        #     driver.find_element(By.CLASS_NAME,"Inactive_Button").click()
        #     break
        # except Exception as er:
        #     sleep(5)
        #     print(er, "waiting for ext")
    # sleep(10)

    sleep(7)
    p = driver.window_handles[0]
    c = driver.window_handles[1]
    driver.switch_to.window(c)
    driver.close()

    driver.switch_to.window(p)
    
    sleep(1)

    driver.find_element(By.CLASS_NAME, "next").click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "next").click()
    sleep(3)
    driver.find_element(By.CLASS_NAME, "button-clicker").click()
    sleep(5)


# # ***************** Inputs *****************
# def get_input():
print("\n\n\t***** Welcome to Auto Visa Apply Bot! *****")
print("\t[For quit the program press = Ctrl + C, For Past the text press = Ctrl + V]\n")
email_address = input("Please Enter login Email address: ")
passwrd = input("Please enter login Password: ")

print('\n\t*** Visa Details ***')
first_name = input("Enter the first name: ")
last_name = input("Enter the last name: ")
gender = int(input("Gender: Enter 1 for Female, 2 for Male & 3 for Others: "))
# country =  input("Enter Country name correctly: ")
country = "Turkiye"
passport_no = input("Enter the Passport number: ")
country_code = input("Enter the country_code (44) :")
phone_no = input("Enter the phone number: ")
detail_email = input("Enter the Email address: ")


print('\n\t*** Appointment Details ***')
print("\nChoose your appointment category")
print("\t1 - National Visa (Type D)")
print("\t2 - Schengen Visa (Type C)")
print("\t3 - Reconsideration")
op1 = int(input("\nEnter the option number to select: "))

print("\nChoose your sub-category")
print("\t1 - Higher Education")
print("\t2 - Turkish Citizens - work permit")
print("\t3 - Foreigners- work permit")
print("4 - Long-Stay others")
op2 = int(input("\nEnter the option number to select: "))


print("\nChoose your Visa application centre")
op3 = int(input("\tEnter the number of centre (1 for 1st, 2 for 2nd, etc.): "))

print("\n\tThanks for providing information!!")







# =====================================
def main():    
    
    #================================================================
    f = open('use_proxy.txt', 'r')
    is_proxy = f.read()

       
    path = os.path.join(os.getcwd(), './driver.exe')

    #================================================================

    # ser = Service("driver.exe")
    login_url = "https://visa.vfsglobal.com/tur/en/pol/login"
    options= get_driver(is_proxy)
    
    driver = webdriver.Chrome(executable_path=path, options=options)
    # driver = webdriver.Chrome(service=ser, options=options)
    driver.delete_all_cookies()
    
    if is_proxy.lower() == 'true':
        use_proxy(driver)


    driver.get(login_url)
    while True:
        try:

            while True:
                try:
                    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//input[@formcontrolname="username"]'))).send_keys(email_address)
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//input[@formcontrolname="password"]'))).send_keys(passwrd)
                    break
                except:
                    sleep(2)
                    print("waiting for website to load")
                    

            while True:
                try:
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))).click()
                    break
                except:
                    pass
            sleep(4)
            solveCaptcha_pro(driver)

            driver.switch_to.default_content()
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, '//input[@formcontrolname="password"]'))).send_keys(Keys.ENTER)
                
            print("1st page end")
            break
            #  == 1st page end ==
        except:
            sleep(2)
            print('Waiting for login')

    # sleep(2)
    # # check mark
    # if driver.current_url != "https://visa.vfsglobal.com/tur/en/pol/dashboard":
    #     login()

    
    while True:
        try:
            # sleep(8)
            driver.implicitly_wait(15)
            check = driver.find_elements(By.CLASS_NAME, "mat-checkbox-label")
            check[0].click()
            check[1].click()
            sleep(1)
            driver.find_element(By.XPATH, "/html/body/app-root/div/app-dashboard/section[1]/div/div[2]/button").click()
           
            print("2nd page end")
            break
            
        except Exception as err:
            print("waiting to load page 2")

            

    ## Page 3
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-checkbox-3"))).click()
    sleep(1)
    driver.find_element(By.CLASS_NAME, "mat-button-base").click()
    print("3rd page end")

    # page 4 started
    while True:
        try:
        
            WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.ID, 'mat-input-2'))).send_keys(first_name)

            driver.find_element(By.ID, "mat-input-3").send_keys(last_name)
            
            while True:
                try:
                    sleep(3)
                    # drop down 1
                    driver.implicitly_wait(5)
                    driver.find_element(By.ID, "mat-select-0").click()
                    gender_option = driver.find_elements(By.CLASS_NAME, "mat-option-text")
                    gender_option[gender-1].click()
                    # driver.find_element(By.ID, "mat-option-237").click()

                    driver.find_element(By.ID, "mat-select-2").click()
                    # driver.find_element(By.XPATH, f"//*[contains(text(), '{country}')]").click()
                    driver.find_element(By.ID, "mat-option-216").click()
                    break
                except Exception as err:
                    sleep(5)
                    print("Your provided Gender no. or Country Name is wrong.")

            driver.find_element(By.ID, "mat-input-4").send_keys(passport_no)
            driver.find_element(By.ID, "mat-input-5").send_keys(country_code)
            driver.find_element(By.ID, "mat-input-6").send_keys(phone_no)
            driver.find_element(By.ID, "mat-input-7").send_keys(detail_email)

            sleep(10)

            driver.find_element(By.XPATH, "//*[contains(text(), ' Save ')]").click()
            print('4th page end')
            break
        except Exception as err:
            print(err)


    ## page 5 
    while True:
        sleep(5)
        try:
            drop1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-select-value-5")))
            drop1.click()
            options1 = driver.find_elements(By.CLASS_NAME, "mat-option-text")
            options1[op1-1].click()

            sleep(2)
            while True:
                try:
                    drop2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-select-value-7")))
                    drop2.click()
                    options2 = driver.find_elements(By.CLASS_NAME, "mat-option-text")
                    options2[op2-1].click()
                    break
                except:
                    print('Waiting for selecting menu 1')

            while True:
                sleep(5)
                try:
                    drop3= driver.find_element(By.ID, "mat-select-value-9")
                    drop3.click()
                    options3 = driver.find_elements(By.CLASS_NAME, "mat-option-text")
                    options3[op3-1].click()
                    break
                except:
                    print('Waiting for selecting menu 2')

            while True:
                try:
                    # sleep(8)
                    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "mat-button-base"))).click()
                    break
                except:
                    sleep(5)
                    print("waiting for selecting menu 3")



            # ================= Embend the check point here =======================


            print("page 5 end")
            break

        except Exception as err:
            # driver.refresh()
            print(err)


    #  Page 6 =================

    while True:
        try:
            driver.implicitly_wait(10)
            driver.find_element(By.CLASS_NAME, "date-availiable").click()
            sleep(1)
            driver.find_element(By.ID, "STRadio1").click()
            sleep(1)
            driver.find_element(By.XPATH, "//*[contains(text(),  ' Continue ')]").click()
        
            break
        except Exception as err:
            sleep(5)
            print("Waiting for 6 page to load")


    # ===================== page 7 ===============
    while True:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  ' Continue ')]"))).click()
            break
        except Exception as err:
            sleep(3)
            print("Waiting for 7 page to load")
 
    # page 8

    while True:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "mat-checkbox-label"))).click()
            # driver.find_elements(By.CLASS_NAME, "mat-checkbox-label")

            break
        except Exception as err:
            print("Waiting for 8 page to load")

    sleep(1)
    try:
        # driver.find_element(By.ID, "mat-radio-6").click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  'E-mail')]"))).click()

        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  ' Continue ')]"))).click()
    except Exception as err:
        print("err in email radio")

    
    # page 9
    while True:
        try:
            payment = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "mat-select-12")))
            payment.click()
            # driver.find_element(By.ID, "mat-option-254").click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  'BANK')]"))).click()
            sleep(1)
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  ' Continue ')]"))).click()
            break
        except Exception as err:
            print(err, "Waiting for 9 page to load")
    
    # # page 10
    # while True:
    try: 
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),  ' Continue ')]"))).click()

        # break
    except Exception as err:
        print("Waiting for 10 page to load")


    print("\n*** Visa Applied Successfully! ***\n")

    sleep(10)
    driver.close()


if __name__ == "__main__":
    main()