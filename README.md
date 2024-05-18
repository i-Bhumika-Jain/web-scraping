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
