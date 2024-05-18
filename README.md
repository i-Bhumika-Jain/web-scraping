**Project Overview**

This script is designed to extract image URLs from web pages specified in a LibreOffice Spreadsheet file. It utilizes the requests library to fetch HTML content from URLs and BeautifulSoup for parsing HTML. The extracted image URLs are then saved to an output LibreOffice Spreadsheet file for further analysis or usage.

**Key Features**

1. URL Scraper Functionality:
Uses the requests library to fetch HTML content from specified URLs.
Utilizes BeautifulSoup for parsing HTML content and extracting image URLs.

2. Input and Output Handling:
Reads input URLs from a LibreOffice Spreadsheet file (input_urls.ods).
Saves the extracted image URLs to an output LibreOffice Spreadsheet file (output_image_urls.ods).

3. Error Handling:
Handles various exceptions such as bad requests and file not found errors gracefully.
Provides informative error messages to aid in troubleshooting.

**Requirements**

Python 3.x ,
pandas ,
request ,
beautifulsoup4 

### Scrap authenticated sites

**Project Overview**

This project is a web scraper designed to automate the extraction of thread titles, links, and comments from the Microsoft Teams forum. The data is then stored in a CSV file for further analysis

**Key Features**

1. Automated Login:
Uses Selenium WebDriver to automate the login process on Microsoft’s authentication platform.
Handles username and password entry with dynamic waits for page elements.

2. Web Scraping:
Extracts thread titles, links, and comments from the Microsoft Teams forum.
Navigates through multiple pages and threads to gather comprehensive data.

3. Data Storage:
Stores the extracted data in a structured format using a Pandas DataFrame.
Saves the data to a CSV file for easy access and analysis.

4. Dynamic Web Elements Handling:
Uses Selenium’s WebDriverWait and ExpectedConditions to manage dynamic loading of web elements.
Incorporates appropriate waiting times to ensure all elements are fully loaded before interacting.

5. Customizable Options:
Provides options for running the Chrome browser in headless mode for faster execution and reduced resource usage.

**Requirements**

Python 3.x ,
Selenium , 
webdriver_manager ,
pandas

