# It's working for 'title' and 'release_date' but
# it doesn't for 'score' even using JavaScript to extract
# text fromm a Shadow DOM


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Set up Selenium WebDriver and navigate to the Rotten Tomatoes page
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
options.add_argument("--no-sandbox")  # Bypass OS security model
options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.5481.178 Safari/537.36")

driver = webdriver.Chrome(options=options)

url = "https://www.rottentomatoes.com/browse/movies_at_home/critics:certified_fresh"
driver.get(url)

# Wait the page load
WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-track='scores']")))

# Extract the HTML content using driver.page_source
html = driver.page_source

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

#  Shadow DOM, component encapsulates
def get_shadow_text(driver, element, selector):
    # Javascript to retrieve text from a Shadow DOM
    try:
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
        shadow_element = shadow_root.find_element(By.CSS_SELECTOR, selector)
        return shadow_element.text.strip()
    except Exception as e:
        print(f"Error access Shadow DOM: {e}")
        return "N/A"
    

# Find and extract the desired movie information
movies = driver.find_elements(By.CSS_SELECTOR, "a[data-track='scores']")

for movie in movies:
    try:
        title = movie.find_element(By.CLASS_NAME, "p--small").text if movie.find_elements(By.CLASS_NAME, "p--small") else "N/A"
        release_date = movie.find_element(By.CLASS_NAME, "smaller").text if movie.find_elements(By.CLASS_NAME, "smaller") else "N/A"

        # score_element = movie.find_element(By.TAG_NAME, "score-pairs-deprecated")
        # score = get_shadow_text(driver, score_element, "rt-text[slot='criticsScore']").strip() if score_element else "N/A"

        score_element = movie.find_element(By.CSS_SELECTOR, "score-pairs-deprecated")
        score = get_shadow_text(driver, score_element, "rt-text[slot='criticsScore']").strip() if score_element else "N/A"
    
    except Exception as e:
        title, release_date, score = "N/A", "N/A", "N/A"
        print(f"Error: {e}")

    # Print the extracted data
    print(f"Title: {title}")
    print(f"Score: {score}")
    print(f"Release Date: {release_date}")
    print("--------------------")

# Close Selenium
driver.quit()
