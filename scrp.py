import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import ExcelWriter
import mysql.connector
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time
from bs4 import BeautifulSoup

# Load configuration
with open("config.json", "r") as config_file:
    config = json.load(config_file)

web_url = config["web_url"]
db_config = config["db_config"]
columns = db_config["columns"]

# Set up the web driver
driver = webdriver.Chrome()  # or 'webdriver.Firefox()'

# Access the web page
driver.get(web_url)  # use the URL from the config file
driver.maximize_window()
time.sleep(1)
table_name=driver.find_element(By.XPATH,"//div/h3[contains(text(),'Transactions Summary by Hospitals')]")
actions = ActionChains(driver)
actions.move_to_element(table_name).perform()
reg_st_ele=driver.find_element(By.XPATH,"(//div/h3[contains(text(),'Transactions Summary by Hospitals')]/parent::div/div/div/div/select)[3]")
select=Select(reg_st_ele)
select.select_by_visible_text("Registered for DHIS")
time.sleep(3)
drp_dwn=driver.find_element(By.XPATH,"(//div[@class='selectCategory' and @style='min-width: 60px; max-width: 70px; margin-bottom: 20px;'])[2]/select")
actions = ActionChains(driver)
actions.move_to_element(drp_dwn).perform()
select=Select(drp_dwn)
select.select_by_visible_text("All")
time.sleep(5)
tablenmae="//div/h3[contains(text(),'Transactions Summary by Hospitals')]"
reg_stu="(//div/h3[contains(text(),'Transactions Summary by Hospitals')]/parent::div/div/div/div/select)[3]"
all_drp_dw="(//div[@class='selectCategory' and @style='min-width: 60px; max-width: 70px; margin-bottom: 20px;'])[2]/select"

# Fetch the table data (ignoring headers)
table = driver.find_element(By.XPATH, "(//table[@id='dhis-elg-trnx'])[2]")  # locate the first table on the page
rows = table.find_elements(By.XPATH, "(//table[@id='dhis-elg-trnx'])[2]/tbody/tr")[1:]  # skip the header row
# Locate the table using XPath
table_xpath = "(//table[@id='dhis-elg-trnx'])[2]"  # Replace with the XPath for your table
table_element = driver.find_element(By.XPATH,table_xpath)

# Extract the table's HTML
table_html = table_element.get_attribute("outerHTML")

# Parse the table using BeautifulSoup
soup = BeautifulSoup(table_html, "html.parser")

# Extract rows from the table, skipping the header row
data = []
rows = soup.find_all("tr")[1:]  # Skip the first row (headers)
for row in rows:
    cols = [col.text.strip() for col in row.find_all("td")]  # Get all 8 columns
    if len(cols) == 8:  # Ensure it has exactly 8 columns
    #if any("Nephro" in col.lower() for col in cols):
        data.append(cols)

# Convert data to Pandas DataFrame
#columns = ["Column1", "Column2", "Column3", "Column4", "Column5", "Column6", "Column7", "Column8"]
df = pd.DataFrame(data, columns=columns)
filtered_df=df[df[columns[1]].str.contains("Nephro",case=False,na=False)]
print("data",filtered_df.head())
# Export filtered data to an Excel file
filtered_df.to_excel("filt_data1.xlsx", index=False, engine="openpyxl")

# Close the Selenium driver
driver.quit()

print("Filtered data exported successfully to 'filtered_data.xlsx'.")

