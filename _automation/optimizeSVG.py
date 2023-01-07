from pathlib import Path
from os import listdir
from os.path import isfile, join

from selenium import webdriver
import time

main_path = Path(__file__).parent.parent
logos_folder = 'teams/logo'
src_path = (main_path / logos_folder).resolve()
onlyfiles = [join(src_path, f) for f in listdir(src_path) if isfile(join(src_path, f))]

driver = webdriver.Chrome()
driver.get("https://www.svgviewer.dev/")

driver.maximize_window()
time.sleep(5)

uploadInput = driver.find_element("xpath", "//input[@type = 'file']")
downloadbutton = driver.find_element("xpath", "(//button [@type = 'submit'])[8]")
for file in onlyfiles: 
    print(file)
    uploadInput.send_keys(file)
    time.sleep(1)
    optimizeButton = driver.find_element("xpath", "(//button [@type = 'submit'])[3]")
    optimizeButton.click()
    time.sleep(1)
    downloadbutton.click()
    time.sleep(2)