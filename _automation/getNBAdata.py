# python <program>.py <input_file_path>.json <output_file_path>.json

import argparse
from pathlib import Path
from selenium import webdriver
import time
import json


# Get path args 
parser = argparse.ArgumentParser()
parser.add_argument("input", type=Path)
parser.add_argument("output", type=Path)
arg_input = parser.parse_args().input
arg_output = parser.parse_args().output

# Read input file
with open(arg_input) as f:
    players = f.readlines()


# Browser driver config
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# Open browser driver
driver.get("https://www.nba.com/players")
driver.maximize_window()


# Web-Scrap data
data = []
for player in players: 
    try:
        search_player = driver.find_element("xpath", "(//input [@type='text'])[1]")
        search_player.clear()
        search_player.send_keys(player)
        time.sleep(2)
        driver.find_element("xpath", "(//a)[121]").click()

        ## Profile page

        # Split team/number/position
        team_number_position = driver.find_element("xpath", "//p [@class='PlayerSummary_mainInnerInfo__jv3LO']").text
        team_name = team_number_position.split(' | ')[0]
        number = team_number_position.split(' | ')[1].replace('#', '')
        position = team_number_position.split(' | ')[2]
        abv_position = list(''.join([c for c in position if c.isupper()]))


        # Get imperial measurements
        height_full = driver.find_element("xpath", "(//p [@class='PlayerSummary_playerInfoValue__JS8_v'][1])[1]").text
        height_imperial = height_full.split()[0]
        weight_full = driver.find_element("xpath", "(//p [@class='PlayerSummary_playerInfoValue__JS8_v'][1])[2]").text
        weight_imperial = int(weight_full.split('lb')[0])

        # Get numeric age
        age_text = driver.find_element("xpath", "(//p [@class='PlayerSummary_playerInfoValue__JS8_v'][1])[5]").text
        age_number = int(''.join([c for c in age_text if c.isdigit()]))

        new_player = {
            "name": {
                "first": player.split()[0],
                "last": player.split()[1]
            },
            "team": {
                "name": team_name,
                "number": number
            },
            "position": abv_position,
            "allStar": {
                "team": "Team 1",
                "role": "bench",
                "number": -1
            },
            "stats": {
                "pts": float(driver.find_element("xpath", "(//p [@class='PlayerSummary_playerStatValue___EDg_'][1])[1]").text),
                "reb": float(driver.find_element("xpath", "(//p [@class='PlayerSummary_playerStatValue___EDg_'][1])[2]").text),
                "ast": float(driver.find_element("xpath", "(//p [@class='PlayerSummary_playerStatValue___EDg_'][1])[3]").text)
            },
            "personalData": {
                "heightImperial": height_imperial,
                "weightImperial": weight_imperial,
                "age": age_number,
                "country": driver.find_element("xpath", "(//p [@class='PlayerSummary_playerInfoValue__JS8_v'][1])[3]").text
            }
        }

        print(new_player)
        data.append(new_player)
    except:
        print(f'Error at player {player}')

    driver.back()
    time.sleep(1)


# Saves data
output = {"data": data}
with open(arg_output, "w") as outfile:
    json.dump(output, outfile)

time.sleep(5)
