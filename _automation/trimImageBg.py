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
driver.get("https://trimmy.io/")
driver.maximize_window()

time.sleep(5)

driver.find_element("xpath", "//button [@id='get_started']").click()
time.sleep(2)

for file in onlyfiles: 
    time.sleep(1)

    uploadInput = driver.find_element("xpath", "//input[@type = 'file']")
    uploadInput.send_keys(file)
    time.sleep(4)

    close = driver.find_element("xpath", "(//button [@title='Remove'])[2]")
    close.click()
    time.sleep(1)



driver.find_element("xpath", "//input [@type='button']").click()
time.sleep(1)

driver.find_element("xpath","//select [@id='target_color']/option[text()='Transparent']").click()
driver.find_element("xpath","//select [@id='output_filetype']/option[text()='png']").click()
driver.find_element("xpath", "//input [@id='saveForm']").click()
time.sleep(3)

driver.find_element("xpath","//a [@id='get_downloads']").click()


time.sleep(5)


