from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
import time
import json
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return selenium_run()

def selenium_run():
    s = Service(ChromeDriverManager().install())
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome(service=s, options=op)
    url = "https://swishanalytics.com/optimus/mlb/batter-vs-pitcher-stats?date=" + str(date.today())

    # Setup ChromeDriver using webdriver

    try:
        # Open the URL
        driver.get(url)

        # Wait for the table to be present
        time.sleep(3)
        
        # Iterate over each row of the table
        rows = driver.find_elements(By.XPATH, '//*[@id="stat-table"]/tbody/tr')
        
        
        # Create empty array to load data 
        final_data = []
                
        for row in rows[0:]: 
            # Skip the header row
            try:
                batter = row.find_element(By.XPATH, './td[1]/span[1]').text
                pitcher = row.find_element(By.XPATH, './td[2]/span').text
                pa = row.find_element(By.XPATH, './td[3]').text
                ab = row.find_element(By.XPATH, './td[4]').text
                hits = row.find_element(By.XPATH, './td[5]').text
                singles = row.find_element(By.XPATH, './td[6]').text
                doubles = row.find_element(By.XPATH, './td[7]').text
                triples = row.find_element(By.XPATH, './td[8]').text
                hr = row.find_element(By.XPATH, './td[9]').text
                bb = row.find_element(By.XPATH, './td[10]').text
                so = row.find_element(By.XPATH, './td[11]').text
                avg = row.find_element(By.XPATH, './td[12]').text
                obp = row.find_element(By.XPATH, './td[13]').text
                slg = row.find_element(By.XPATH, './td[14]').text

                data = {
                    "Batter": batter,
                    "Pitcher": pitcher,
                    "PA": pa,
                    "AB": ab,
                    "Hits": hits,
                    "1B": singles,
                    "2B": doubles,
                    "3B": triples,
                    "HR": hr,
                    "BB": bb,
                    "SO": so,
                    "AVG": avg,
                    "OBP": obp,
                    "SLG": slg
                }
                
                final_data.append(data)
                
            except Exception as e:
                print(f"Error processing row: {e}")

    finally:
        # Save the data by iteration through final_data
        def save_data():
            newData = final_data[0:]
            
            return newData
            
        return save_data()
        # Close the WebDriver
        driver.quit()
                      
    
if __name__ == ("__main__"):
    app.run(debug=True)