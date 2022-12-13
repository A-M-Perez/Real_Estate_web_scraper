# REMAX Real Estate Web Scraping

REMAX is one of the main Real Estate (Agent) companies in Argentina, with a significant portion of the market under scope and which manages most of its marketing through a website (https://www.remax.com.ar).

## Project objective

This project aims to build a web scraper, using Python with BeautifulSoup, to fetch data from the REMAX website and export the **main characteristics** of the searched properties to a local ".csv" file for further analysis.

## Libraries used

- urllib
- BeautifulSoup
- ssl
- csv
- re
- time

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
├── Real_estate_ARG.csv (sample output file for "Apartments" nationwide)

## Running instructions

>*DO NOT FORGET to check the https://www.remax.com.ar/robots.txt file to ensure compliance with the website's search engine crawlers policy*

To test or run this script, please:

- Clone the repository or download the file "REMAX_ARG_Web_scraper.py"
- Import the file "REMAX_ARG_Web_scraper.py" to your favourite integrated development environment (IDE) supporting Python
- Go into the REMAX website (https://www.remax.com.ar) and do a search for the properties of interest
- Copy the obtained URL and paste it inside the ".py" file. Line code is commented with explanations
- Run the entire script

## How this project helped me grow:

One of the main challenges was to fetch data and segregate it to be exported into different columns. I was able to overcome this by properly applying Regular Expressions (RegEx) to identify the different characteristics of these data.

I also learnt how to create, populate and export CSV files using Python, and was able to apply iteration statements with try and except.

## Final considerations

As stated above, this project aims at scraping some of the main characteristics of the properties for further analysis and therefore it is intended to export a clean dataset that could be easily plugged in to other tools.

The project does not consider all the possible combinations of filters and there could be errors when trying to fetch specific combinations. If this happens and you find a way to optimize my code, please feel to reach out and share it!