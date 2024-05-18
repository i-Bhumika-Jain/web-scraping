import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Authentication credentials
USERNAME = 'bhumika.jain@braneenterprises.com'
PASSWORD = 'lovemom@4'

# Initialize Chrome webdriver with necessary options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # Run in headless mode (no browser window)
options.add_argument('--disable-gpu')  # Disable GPU acceleration
options.add_argument('--window-size=1920x1080')  # Set window size

# Initialize the Chrome driver with WebDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Wait for the login page to load
driver.get('https://login.microsoftonline.com/common/oauth2/v2.0/authorize?client_id=a81d90ac-aa75-4cf8-b14c-58bf348528fe&redirect_uri=https%3A%2F%2Fanswers.microsoft.com&response_type=code%20id_token&scope=openid%20profile&state=OpenIdConnect.AuthenticationProperties%3D2MV7KwAaRH3m9QIfy3B1fRgx-NuW-mQRwruh-zRwWKkD8tQRmDORNEb119Gk0rHLZ7YSmlLv5GZ6ts1K7TV6Tvvf1qtSt7PJRgULNL1LPxhikouNBugIgGLubbLtDC4oOlp1U0YikFkF2Tz12rU_iR30VPzXP934FYJlBACVb9hLMivmMBWmdC5D0ZnR7NXjxuA5EWae6Zcbe1qgwR82hD76hDiebQ6PVzJAslpKm6vYfGEwAfj6vL2SOVKJJem7ENF4zgzZqAnxV5IQrrRvmCrOgRVcJiRNWFYZU9N8760sXTSQt9bZTnIJzW5U4qB8oZe9AdyPzjT82z10krrVhV1kW4rwB9o9FHWI6kqLxZofgpGbjzd_PjRijAAWlh8R4C-AsklLEo2jPgL_mqlwh3p4G94Lf9NVgm2Vv02LaMgKVU8A5gVxLJd4mAoFvyhs&response_mode=form_post&nonce=638441118534315816.MTU2ZTIzZjctZDA5ZS00OTM3LWIxYjctMjBmODZjYmJkZmRjOWE4N2NlOWEtYjZhOS00YWJmLWE3NDUtODVkOWFlNDU5NTg4&nopa=2&prompt=select_account&x-client-SKU=ID_NET472&x-client-ver=6.17.0.0')

# Wait for the username input field to be located using class name
username_input = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.form-control.ltr_override.input.ext-input.text-box.ext-text-box')))
username_input.send_keys(USERNAME)
username_input.send_keys(Keys.RETURN)

# Wait for the password input field to be located using ID
password_input = WebDriverWait(driver, 90).until(EC.presence_of_element_located((By.ID, 'i0118')))
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.RETURN)

# Wait for the login process to complete
time.sleep(5)

# Navigate to the desired page to scrape
driver.get('https://answers.microsoft.com/en-us/msteams/forum?sort=LastReplyDate&dir=Desc&tab=All&status=all&mod=&modAge=&advFil=&postedAfter=&postedBefore=&threadType=All&isFilterExpanded=true&page=1')

# Wait for the page to load completely
time.sleep(5)

# Initialize lists to store thread titles, links, and comments
thread_titles = []
thread_links = []
thread_comments = []

# Extract thread titles and links
for thread_link in driver.find_elements(By.CSS_SELECTOR, 'a.c-hyperlink[data-bi-id="thread-link"]'):
    thread_titles.append(thread_link.text.strip())
    thread_links.append(thread_link.get_attribute('href'))

# Extract comments from each thread
for link in thread_links:
    driver.get(link)
    time.sleep(5)  # Wait for the page to load
    
    # Extract comments
    comments = []
    for comment_element in driver.find_elements(By.CSS_SELECTOR, 'div.thread-message-content-body-text.thread-full-message'):
        comments.append(comment_element.text.strip())
    thread_comments.append(comments)

# Close the browser
driver.quit()

# Create DataFrame to store the data
data = {
    "Thread Titles": thread_titles,
    "Thread Comments": thread_comments
}

# Save to CSV
df = pd.DataFrame(data)
df.to_csv('microsoft_teams_forum_data.csv', index=False)

print('CSV file saved successfully.')