# Billboard 200 Python Scraper

This program, created in Python using BeautifulSoup, accesses and scrapes data from the most recent Billboard 200 chart, available at https://www.billboard.com/charts/billboard-200/. The scraper accesses information from both the chart page itself and the artist's individual page, before placing the information in a CSV file.

## What is being scraped?

Within the chart page, I scraped the following:
- The album title
- The artist name
- The album's peak rank
- How many weeks the album has been on the chart
- The artist URL

All information except for the URL is listed in the CSV file. Within the individual page, I grabbed:
- The artist's number of 'No. 1 Hits' in their discography
- The artist's number of 'Top 10 hits' in their discography

Both pieces of information were placed into variables and are included in the CSV file.

## How was the information scraped?

1. In order to get all the information, I first visited https://www.billboard.com/charts/billboard-200/, where I inspected the page to find the aforementioned data I listed above. 
2. In order to access and scrape ALL information, I needed to use the requests Python package and different headers to avoid any restrictions. This would also be the case when accessing information from the individual artists' pages.
3. From there, I scraped the aforementioned chart information and placed them into variables. The artist URL acquired was then used for the get_additional_information function, where it was concatenated into the string within a requests.get() function to access the individual page.
4. After acquiring the data from the individual pages, all variables were placed in a Python list. The python list was accessed using a writerow function to list an individual artist's data in its own row.
5. For every 20 items acquired, I executed a time.sleep function that contained a random duration using the random.randint function. This approach would preventany indication of a scraping bot and prevent any additional restrictions on the scraper.

## What problems did I find?

Initially, I found that certain artists:
1. Were listed as 'various_artists' or 'soundtrack,' which would take the user to a general page including ALL albums that had ever been listed under those artist names. This would be problematic for accessing data in individual pages.
2. Did not have their own URLs, which would eliminate the ability to access their pages entirely.

As a result, I needed to create a try/except that would list the URL variable as 'N/A.' I then created an if/then function to detect any album listings whose artist's variable was 'N/A' and listed the numOneHits and topTenHits variables as 'N/A.' 

Within the individual pages and in the chart, I found that certain pieces of information were inaccessible despite it's availablility on the page. This was the result of the original developers stylesheet, which made acquiring data inaccessible through the program I created. As a result, I was unable to acquire the rank direction and date peaked.

In addition, some individual pages did not contain the number of albums, number of top 10 hits or number 1 hits. As a result, I reformatted the program to only grab the 'top 10 hits' and 'No. 1 hits,' which were more often found in the artists' individual pages.
