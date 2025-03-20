# For 'Shared Hosting' and 'WordPress Hosting'
# the price should be $0.20/mo more 

from bs4 import BeautifulSoup
from selenium import webdriver

# Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

# For not being consider as a bot
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36")

driver = webdriver.Chrome(options=options)

url = "https://www.inmotionhosting.com/"
driver.get(url)

# Parse the HTML
soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

hosting_plans = soup.find_all("div", class_="imh-rostrum-card")

if not hosting_plans:
    print("No weather data found! The site may be blocking bots.")
    exit()

print("Connection Successful!")

# Store data
hostings = []

for hosting in hosting_plans:
    # Plan name
    plan_name_tag = hosting.find("h3", class_="imh-rostrum-card-title")
    plan_name = plan_name_tag.text.strip() if plan_name_tag else "N/A"

    # Features
    features_tag = hosting.find("ul", class_="imh-rostrum-details-list")
    features = [li.text.strip() for li in features_tag.find_all("li")] if features_tag else ["N/A"]

    # Price
    price_tag = hosting.find("div", class_="imh-rostrum-starting-at-price-discounted")
    price = price_tag.text.strip() if price_tag else "N/A"


    # Add data
    if plan_name != "N/A" and features != ["N/A"]:
        if not any(hosting['Plan Name'] == plan_name for hosting in hostings):
            hostings.append({
                "Plan Name": plan_name,
                "Features": features,
                "Price": price
            })

    
for hosting in hostings:
    # Print the result
    print("\n", hosting["Plan Name"])
    print("Features:")
    for feature in hosting["Features"]:
        print(f"    - {feature}")
    print(f"Price: {hosting['Price']}\n")


# ======== Result ========

# Connection Successful!

#  Shared Hosting
# Features:
#     - Free Domain & SSL
#     - Free Website Builder
#     - Unlimited Bandwidth
#     - cPanel Included
#     - Unlimited Email Addresses
# Price: $3.19/mo


#  WordPress Hosting
# Features:
#     - Free Domain & SSL
#     - Free Website Builder
#     - Free Premium Themes & Plugins
#     - PHP-FPM Workers Included
#     - Unlimited Email Addresses
# Price: $3.69/mo


#  VPS Hosting
# Features:
#     - High-Availability Servers
#     - cPanel and Control Web Panel Available
#     - Free Website Transfers (with a Control Panel)
#     - Cloud-Powered Reliability
#     - Isolated Resources with Hardened Security
# Price: $4.49/mo


#  Dedicated Hosting
# Features:
#     - Configurable Server For Ultimate Flexibility
#     - Redundant Infrastructure With 99.99% Uptime
#     - Choose Between Managed With cPanel or Unmanaged Bare MetalPrice: $35.00/mo
# Price: $35.00/mo