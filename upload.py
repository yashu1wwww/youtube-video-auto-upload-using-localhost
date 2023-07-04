from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress","localhost:8080")

driver = webdriver.Chrome(options=option)
time.sleep(2)
driver.get("https://www.youtube.com/upload")
time.sleep(6)
driver.find_element_by_xpath('//input[@type="file"]').send_keys(r"C:\Users\Hp\Desktop\nest\videos\video is good.mp4") #replace to your video location path & what the video title in path is the title fpr video 
time.sleep(3)
driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-video-description/div/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div").send_keys("new video good video") #description change for yours.
time.sleep(3)
driver.find_element_by_id("offRadio").click() #for kids it will tick..
time.sleep(5)
driver.find_element_by_xpath("/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/div[1]/div/div/ytcp-icon-button").click()
time.sleep(20)