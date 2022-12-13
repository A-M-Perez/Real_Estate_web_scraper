# REMAX Real Estate Web Scraping

REMAX is one of the main Real Estate (Agent) companies in Argentina, with a significant portion of the market under scope and which manages most of its marketing through a website (https://www.remax.com.ar).

## Project objective

This project aims to build a web scraper, using Python with BeautifulSoup, to pull data from the REMAX website and export the **main characteristics** of the searched properties to a ".csv" file for further analysis.

## (Output) Data description

- ***Property_Type:*** refers to the type of property defined by the website filters, such as "House", "Apartment", "Office", etc.

- ***Location:*** refers to the neighbourhood and Province in which the property is located.

- ***Price:*** price of the property.

- ***Price_Currency:*** currency in which the price of the property is expressed (USD or ARS).

- ***Total_Area_m2:*** total size of the property, expressed in square meters. Total area = covered area + uncovered area.

- ***Covered_Area_m2:*** size of the covered area of the property, which is included in its total size, also expressed in square meters.

- ***Room_number:*** number of bedrooms in the property.

- ***Bathroom_number:*** number of bathrooms and toilets in the property.

- ***Expenses:*** approximate amount of monthly expenses (services, security, etc.) of the property.

- ***Expenses_Currency:*** currency in which the amount of expenses is expressed.

## Repository overview / structure

├── README.md\
├── REMAX_ARG_Web_scraper.py (web scraper code)\
├── Real_estate_ARG.csv (sample output file for "Apartments" nationwide)\

## Running instructions

>*DO NOT FORGET to check the https://www.remax.com.ar/robots.txt file to ensure compliance with the website's policy*

To test and run this script, please:

    * Import the file "REMAX_ARG_Web_scraper.py" to your favourite integrated development environment (IDE) supporting Python
    * Go into the REMAX website (https://www.remax.com.ar) and do a search for the properties of interest
    * Copy the obtained URL and paste it in the ".py" file. Line is commented with explanations
    * Run the entire script