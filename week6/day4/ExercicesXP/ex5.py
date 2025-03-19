# Attica Weather

from collections import Counter
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import time 

# Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# For not being consider as a bot
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36")

driver = webdriver.Chrome(options=options)

url = "https://www.accuweather.com/en/us/attica/30607/weather-forecast/2139413"
driver.get(url)

# Tme to load the page
# time.sleep(10)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(5)

# HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

# All daily forecast
forecast_days = soup.find_all("a", class_="daily-list-item")

if not forecast_days:
    print("No weather data found! The site may be blocking bots.")
    exit()

# Lists to store data
temperatures = []
conditions = []
humidity_values = []

for day in forecast_days:
    # Temperature
    temp_hi_tag = day.find("span", class_="temp-hi")
    if temp_hi_tag and temp_hi_tag.text.strip():
        temp_hi = int(temp_hi_tag.text.strip().replace("°", ""))
        temperatures.append(temp_hi)
    

    # Weather condition
    condition_tag = day.find("div", class_="phrase")
    if condition_tag:
        condition = condition_tag.find("p", class_="no-wrap")
        if condition and condition.text.strip():
            conditions.append(condition.text.strip())
        

    # Humidity
    humidity_tag = day.find("div", class_="precip")
    if humidity_tag and humidity_tag.text.strip():
        match = re.search(r"(\d+)%", humidity_tag.text)
        if match:
            humidity_values.append(int(match.group(1)))
        

print(f"Temperatures: {temperatures}")
print(f"Weather Condition: {conditions}")
print(f"Humidity: {humidity_values}")


# Average and condition 
average_temp = sum(temperatures) / len(temperatures) if temperatures else "N/A"
most_common_condition = Counter(conditions).most_common(1)[0][0] if conditions else "Unknown"
average_humidity = sum(humidity_values) / len(humidity_values) if humidity_values else "N/A"

# Analysis results
print("\n**Analysis results for Attica**")
print("-" * 40)
print(f"Average Temperature : {average_temp}°C")
print(f"Most common weather condition: {most_common_condition}")
print(f"Average Humidity: {average_humidity}%")



# ======== Result ========

# **Analysis results for Attica**
# ----------------------------------------
# Average Temperature : 21.0°C
# Most common weather condition: Sunny and pleasant        
# Average Humidity: 8.8%