from bs4 import BeautifulSoup
from selenium import webdriver
import re
from datetime import datetime, timedelta

options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(options=options)

url = "https://www.bbc.com/innovation/technology"
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
driver.quit()

articles = soup.find_all("div", class_="sc-c6f6255e-0 eGcloy")

# Dictionary to store articles by month
articles_by_month = {}

for article in articles: 
    title_tag = article.find("h2", class_="sc-87075214-3 eywmDE")
    title = title_tag.text.strip() if title_tag else "None"
    
    date_tag = article.find("span", class_= "sc-6fba5bd4-1 heskfp")
    date_text = date_tag.text.strip() if date_tag else "None"

    if title == "None":
        continue

    date_real = datetime.now() # by default

    if date_text:
        # "X hrs ago" case
        match_hours = re.search(r"(\d+)\s*hrs? ago", date_text)
        if match_hours:
            hours_ago = int(match_hours.group(1))
            date_real = datetime.now() - timedelta(hours=hours_ago)
        
        # "X days ago" case
        match_days = re.search(r"(\d+)\s*days? ago", date_text)
        if match_days:
            days_ago = int(match_days.group(1))
            date_real = datetime.now() - timedelta(days=days_ago)
    
        month_name = date_real.strftime("%B")
        
        if month_name not in articles_by_month:
            articles_by_month[month_name] = []

        articles_by_month[month_name].append(f"{title} ({date_real.strftime('%Y-%m-%d')})")

for month, articles in sorted(articles_by_month.items()):
    print(f"\n{month}")
    print("-" * 30)
    for article in articles:
        print(article)

