import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

email = 'pass100q\n'                  #change to your mail
password = 'pas12#$%\n'           #change to your pass  

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
#time.sleep(4)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(14)  
driver.find_element_by_xpath('/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button').click()
time.sleep(3)
driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item/div[2]/yt-formatted-string[1]').click()
time.sleep(5)
driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\Hp\Desktop\Bots\gmail auto send\charlie.mp4") #replace with your path where video available
time.sleep(20)                                                                                                                                  