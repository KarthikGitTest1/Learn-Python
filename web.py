import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from pandas import ExcelWriter
import mysql.connector
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

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
data = []
for row in rows:
    cols = row.find_elements(By.XPATH, ".//td")
    cols = [col.text for col in cols]
    if ("Nephro" in col.text.lower() for col in cols):
        data.append(cols)

# Create a DataFrame
df = pd.DataFrame(data, columns=columns)

# Save data to Excel file
with ExcelWriter("data.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, index=False)

# Save data to MySQL database
# Establish MySQL connection using details from the config file
conn = mysql.connector.connect(
    host=db_config["host"],
    user=db_config["user"],
    password=db_config["password"],
    database=db_config["database"]
)
cursor = conn.cursor()

# Insert data into the table in batches
table_name = db_config["table_name"]
batch_size = 100
for i in range(0, len(data), batch_size):
    batch = data[i:i + batch_size]
    cursor.executemany(f"""
        INSERT INTO {table_name} ({', '.join(columns)})
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, batch)

# Commit changes and close connection
conn.commit()
cursor.close()
conn.close()

# Close the web driver
driver.quit()
