from pathlib import Path
from os import listdir
from os.path import isfile, join

from selenium import webdriver
import time

# Get files 
main_path = Path(__file__).parent.parent
signatures_folder = '_automation/temp'
src_path = (main_path / signatures_folder).resolve()
onlyfiles = [join(src_path, f) for f in listdir(src_path) if isfile(join(src_path, f))]

# Browser driver config
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Open browser driver
driver.get("https://imgonline.tools/remove-white-background")
driver.maximize_window()

time.sleep(5)

for file in onlyfiles: 
    time.sleep(1)

    uploadInput = driver.find_element("xpath", "//input[@type = 'file']")
    uploadInput.send_keys(file)
    time.sleep(1)

    submitButton = driver.find_element("xpath", "//span[@class='ui green button']")
    submitButton.click()
    time.sleep(1)

    downloadButton = driver.find_element("xpath", "(//span[@class='ui blue small button'])[2]")
    downloadButton.click()

time.sleep(5)


