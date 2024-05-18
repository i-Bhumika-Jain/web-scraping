import pandas as pd
import requests
from bs4 import BeautifulSoup
import re  # Import the regular expression module

# Function to scrape images from a given URL
def scrape_images_from_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an exception for bad requests

        # Check if the response contains HTML content
        if 'text/html' not in r.headers.get('content-type', ''):
            print(f"Error: {url} does not contain HTML content.")
            return []

        soup = BeautifulSoup(r.content, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')

        # Extract image URLs
        image_urls = [img['src'] for img in img_tags]

        # Filter out non-HTTP image URLs using regular expressions
        http_image_urls = [img_url for img_url in image_urls if re.match(r'^https?://', img_url)]

        return http_image_urls
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return []
    except Exception as e:
        print(f"Error scraping images from {url}: {e}")
        return []

# Read input LibreOffice Spreadsheet file containing URLs
input_ods_file = "input_urls.ods"
try:
    df_input = pd.read_excel(input_ods_file, engine="odf")  # Use "odf" engine for LibreOffice Spreadsheet files
except FileNotFoundError:
    print(f"Error: File '{input_ods_file}' not found.")
    df_input = pd.DataFrame()  # Create an empty DataFrame in case of error

# Check if 'URL' column exists in DataFrame
if 'URL' not in df_input.columns:
    print("Error: 'URL' column not found in input file.")
    df_input = pd.DataFrame()  # Create an empty DataFrame if 'URL' column is missing

# Initialize a list to store results
results = []

# Scrape images for each URL in the input LibreOffice Spreadsheet file
for index, row in df_input.iterrows():
    url = row['URL']
    image_urls = scrape_images_from_url(url)
    for img_url in image_urls:
        results.append({'URL': url, 'Image URL': img_url})

# Create a DataFrame from the results
df_results = pd.DataFrame(results)

# Save the results to an output LibreOffice Spreadsheet file
output_ods_file = "output_image_urls.ods"
df_results.to_excel(output_ods_file, index=False, engine="odf")  # Use "odf" engine for LibreOffice Spreadsheet files

print(f"Results saved to {output_ods_file}")