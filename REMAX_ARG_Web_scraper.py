# Import libraries
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import csv
import re
from time import sleep

# Ignore certification validation
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create and set the structure of the file to be exported with scraped data
file = open('Real_estate_ARG.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(['Property_Type', 'Location', 'Price', 'Price_Currency', 'Total_Area_m2', 'Covered_Area_m2', 'Room_number', 'Bathroom_number', 'Expenses', 'Expenses_Currency'])

# Set the target URL to be scraped => Go to "https://www.remax.com.ar/" and do a manual search for properties of interest, then copy and paste its URL
url = f"https://www.remax.com.ar/listings/buy?page=0&pageSize=24&sort=-createdAt&in:operationId=1&in:typeId=14&filterCount=1&viewMode=list"
url = url.replace('Size=24','Size=100') # Override default number of items to be dispayed, from 24 to 100

# Set HTML parser
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Set the number of total pages to be scraped. Remax website default overwritten to 100 items in code above
pages = soup.find('h1')
pages = pages.text.split(' ')
pages = int(int(pages[0]) / 100) + 1 # Add 1 more page in the count to cover full range when iterating

# REGEX(s) to extract data from the properties' elements
propertyTypeRegEx = '\w+\s' # Used to retrieve only the first word from the description text, which is the type of property being sold
roomsRegEx = '\s\d\sambientes' # Used to retrieve the text containing the number of rooms
bathroomsRegEx = '\s\d\sba\wo' # Used to retrieve the text containing the number of bathrooms
locationRegEx = '\,\s[a-zA-Z0-9\s\,]+\s' # Used to retrieve the address (neighbourhood & Province) of the property from the description text

# Iterate through all pages with properties
for page in range(0, pages):
    print(page)
    # Parse and construct variable URL for each page
    url = re.sub("page=\d+", ('page=' + str(page)), url)
    
    # Open and read each page
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    sleep(1) # Wait 1 second for page to load
    infoCards = soup.find_all('div', class_='info-wrapper') # Assign all web elements containing all the data for each of the properties

    # Iterate through each element and store the data for each property
    for item in infoCards:
        propertyType = re.search(propertyTypeRegEx, item.text).group(0).strip()
        areaM2 = item.find('span', class_='bold-span').text.strip()
        try:
            coveredAreaM2 = item.find('span', class_='second-item bold-span').text.strip()
        except:
            coveredAreaM2 = 'N/A'
        try:
            expenses = item.find('p', id='expenses').text.strip()
            expenses = expenses.split(' ')
            expenseCurrency = expenses[2]
            expenses = expenses[1].replace('.', '')
        except:
            expenses = 'N/A'
            expenseCurrency = 'N/A'
        price = item.find('p', id='price').text.strip()
        price = price.split(' ')
        priceCurrency = price[1]
        price = price[0].replace('.', '')
        try:
            rooms = re.search(roomsRegEx, item.text).group(0)[0:2]
        except:
            rooms = 'N/A'
        try:
            bathrooms = re.search(bathroomsRegEx, item.text).group(0)[0:2]
        except:
            bathrooms = 'N/A'
        try:
            location = re.search(locationRegEx, item.text).group(0).strip()
            location = ''.join(location[2:]) # drop the beginning ', ' in the text
        except:
            location = 'N/A'
        
        # Write property data to the file in each of the columns
        writer.writerow([propertyType, location, price, priceCurrency, areaM2, coveredAreaM2, rooms, bathrooms, expenses, expenseCurrency])

file.close() # Save and close file

exit()