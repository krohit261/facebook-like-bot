from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")



class facebook():

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

        self.browser.set_window_size(1120, 1120)
        
    def login(self):
        self.browser.get('https://www.instagram.com/')
        time.sleep(5)
        
        emailinput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        print("found")
        passwinput = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
        username = os.environ.get('fbuser')
        password = os.environ.get('fbpass')
        print(username)
        self.browser.get('https://www.facebook.com/')
        time.sleep(10)
        self.browser.save_screenshot("screen.png")
        passinp =self.browser.find_element_by_xpath('//*[@id="pass"]')
        emailinp = self.browser.find_element_by_xpath('//input[@id="email"]')
        
        
        print("iam here")
        emailinp.send_keys(username)
        passinp.send_keys(password)
        loginbut = self.browser.find_element_by_xpath('//*[@id="u_0_b"]')
        loginbut.click()
        time.sleep(5)
        print("logged in")

    def pageopen(self):
        self.browser.get('https://www.facebook.com/NavodayaKrantiPariwar')
        time.sleep(8)
        print("page opened")

    def likeimg(self , b):
        for j in range(15):
            a=1
            while a < 2:
                try :
                    print("iamhere")
                    likebut = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div/div[1]/div/div[4]/div[2]/div/div[2]/div[2]/div/div/div['+str(j+1)+']/div/div/div/div/div/div/div/div/div/div/div[2]/div[4]/div/div/div[1]/div[2]/div/span[1]/div/div/span/div[1]/div')
                    print("ias")
                    
                    styletxt = likebut.get_attribute("style")
                    if styletxt == "color: rgb(32, 120, 244);" :
                        a=3
                        
                        
                    else :
                        a=3
                        likebut.click()
                        print('picture liked')
                        

                            
                        
                    time.sleep(8)
                    
                    
                except NoSuchElementException :
                    self.browser.execute_script('window.scrollTo(0,'+str(250*b)+')')
                    print('pagescrolled')
                    time.sleep(2)
                    a=1
               # except ElementNotInteractableException :
               #     self.browser.execute_script('window.scrollTo(0,'+str(250*(b-1) + 10)+')')
               #     a=1
               #     time.sleep(1)
               #     print('scrolled a bit ')

                b=b+1
        print("time to sleep")
        time.sleep(36000)
        print("i am upss")
            

    def closebrowser(self):
        self.browser.close()
            


    

x=facebook()
x.login()
x.pageopen()
inf =1 

while inf < 2 :

    x.likeimg(1)

x.closebrowser()