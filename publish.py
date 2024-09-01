from selenium import webdriver
import keyboard
import time

driver = webdriver.Firefox()
driver.maximize_window() # now screen top-left corner == browser top-left corner 
driver.get("https://studio.youtube.com/channel/xxxxxxxxxxxxxxx")


keyboard.write('xxxxx')
keyboard.press_and_release('enter')
time.sleep(5)
keyboard.write('xxxxxxx')
keyboard.press_and_release('enter')

time.sleep(10)
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('tab')
keyboard.press_and_release('enter')


