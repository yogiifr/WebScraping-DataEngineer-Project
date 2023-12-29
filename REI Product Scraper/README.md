# REI Product Scraper

## Project Description
The REI Product Scraper is a Python script designed for web scraping product information from the REI Outlet website (https://www.rei.com/f/scd-outlet). The purpose of this tool is to systematically collect key details about various products listed on the REI Outlet, including the product name, item number, price, and rating. By navigating through the pages of the outlet section, the script extracts valuable information, providing users with a comprehensive dataset for further analysis or insights into available products.

## Steps
### 1. Libraries and Modules

Imported necessary libraries and modules for web scraping and data processing.

### 2. Data Class 'Item'

Defined a data class to represent product information.

### 3. HTTP Request Function

Created a function to make HTTP requests and retrieve HTML content.

### 4. Search Page Parsing

Implemented a function to parse the search page and extract product URLs.

### 5. Data Cleaning

Developed a function to clean data by removing unwanted characters.

### 6. Text Extraction

Implemented a function to extract text from HTML using CSS selectors.

### 7. Item Page Parsing

Created a function to parse the item page and create 'Item' objects.

### 8. JSON Export

Defined a function to export product data to a JSON file.

### 9. CSV Export

Implemented functions to export product data to CSV files.

### 10. Main Execution

Constructed the main function to execute the entire data collection process.



## Video Reference
For a visual guide and additional insights, you can refer to the following video:

**Title:** Web Scraping with Python - John Watson Rooney

**Link:** [Watch PLaylist](https://www.youtube.com/playlist?list=PLRzwgpycm-FiTz9bGQoITAzFEOJkbF6Qp)
