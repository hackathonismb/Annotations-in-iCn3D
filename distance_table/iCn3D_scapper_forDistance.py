########################################################################
# Script name: iCn3D_scapper_forDistance.py                            #
# Created by Li Chuin Chong                                            #
# Function: to extract information of distance of protein structure    #
# Last update: 13 July 2022                                            #
########################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
import pandas as pd

# initialize chrome driver
driver_exec_path = r"/mnt/c/Program Files (x86)/chromedriver.exe"
browser = webdriver.Chrome(driver_exec_path)

target_pdb_id = '7JMO'
browser.get("https://www.ncbi.nlm.nih.gov/Structure/icn3d/full.html?mmdbid="+target_pdb_id+"&bu=1")
time.sleep(3)

parent = browser.current_window_handle
uselessWindows = browser.window_handles
for winId in uselessWindows:
    if winId != parent: 
        browser.switch_to.window(winId)
        browser.close()

# Click on Analysis > Distance > Among Many Sets
browser.find_element(By.ID, "div0_accordion5").click() # analysis
browser.find_element(By.ID, "ui-id-368").click() # distance
time.sleep(2)
browser.find_element(By.ID, "ui-id-371").click() # among many sets

# select all options in first set
first_set = browser.find_element(By.ID, "div0_atomsCustomDistTable2")
for first_option_set in first_set.find_elements(by=By.TAG_NAME, value='option')[0:]:
    ActionChains(browser).key_down(Keys.CONTROL).click(first_option_set).key_up(Keys.CONTROL).perform()
    
# select all options in second set
second_set = browser.find_element(By.ID, "div0_atomsCustomDistTable")
for second_option_set in second_set.find_elements(by=By.TAG_NAME, value='option')[1:]:
    ActionChains(browser).key_down(Keys.CONTROL).click(second_option_set).key_up(Keys.CONTROL).perform()

# click 
browser.find_element(By.ID, "div0_applydisttable").click()

distance_table = browser.find_element(By.ID, "div0_dl_disttable")
with open('distance_table_'+target_pdb_id+'.csv', 'w', newline='', encoding='utf-8') as csvfile:
    wr = csv.writer(csvfile)
    for row in distance_table.find_elements(by=By.CSS_SELECTOR, value='tr'):
        wr.writerow([d.text for d in row.find_elements(by=By.CSS_SELECTOR, value='td')])
                
# Closes the current window
browser.close()
