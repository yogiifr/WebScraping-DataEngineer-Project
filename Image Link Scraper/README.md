# Scraping and Downloading Images from Websites

## Project Description
This project involves the development of a specialized tool for scraping and downloading images from a designated website, specifically [https://www.pngmart.com/](https://www.pngmart.com/). The objective is to retrieve all images in PNG format to curate a dataset tailored for machine learning purposes. The extracted dataset will be utilized for training and enhancing machine learning models.

## Steps
1. **Estimate Total Images:** An initial rough calculation for the total number of images on the entire website was performed, revealing approximately 11,924 pages with around 20 images per page. This suggests a total of approximately 238,480 images on the website.

2. **Locate Sitemap:** The sitemap of the website was identified, consisting of over 200 indexes, each containing a list of images. Each index comprises 1,000 image URLs.

3. **Retrieve Image URLs:** The script extracts image URLs from the sitemap, aiming to collect a comprehensive list of image locations.

4. **Download Images:** The collected image URLs are then used to download PNG images from the website. The script iterates through the URLs, retrieves the images, and stores them locally.

5. **Document Images into CSV:** The script now includes a section to document the downloaded images into a CSV file. This step involves creating a CSV file and recording relevant information such as image title, source URL, and any additional metadata.

## Video Reference
For a visual guide and additional insights, you can refer to the following video:

**Title:** Python Upwork web scraper - Easy step by step guide | How to make money with Python Episode 2

**Link:** [Watch Video](https://www.youtube.com/watch?v=Al20Pyuc5Ck&list=PLq1YsG1H2jMWSjtGMsfGH48DvPQX1VP-I&index=2)
