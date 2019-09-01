##############################################################################################
#
# Welcome to the Billboard Hot 200 Web Scraper (Updated 08.27.19)
# Created by Angel Kennedy // University of Florida College of Journalism and Communications
# Created for the JOU4436 – Advanced Web Apps course by professor Mindy McAdams
#
##############################################################################################

from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import random
import time
import csv

# CSV file will contain information scraped from Billboard chart
csvfile = open("billboard_listings.csv", 'w', newline='', encoding='utf-8')
c = csv.writer(csvfile)
# write the header row for CSV file
c.writerow(['Rank on Chart', 'album', 'artist', 'peakRank', 'weeksOnChart', 'No. 1 Hits', 'Top 10 Hits'])


# Uses requests package to bypass Billboard site restrictions for bots
site = requests.get('https://www.billboard.com/charts/billboard-200/', headers = {'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'})
s = site.content
bs = BeautifulSoup(s, 'lxml')

# Current Chart Rank
chartRank = 1

# Begins initial scrape through Billboard 200 page:
billboardChart = bs.find('div', {'class':'chart-details'})

for chartSection in billboardChart.find_all('div', {'class':'chart-list chart-details__left-rail'}):
    for chartListing in chartSection.find_all('div', {'class':'chart-list-item'}):

        # Python list contains information on each Billboard listing
        billboard_listing = []

        # Get Album
        album = chartListing.find('div', {'class':'chart-list-item__title'}).get_text()

        # Get Artist
        artist = chartListing.find('div', {'class':'chart-list-item__artist'}).get_text()

        # Get Weeks on Chart
        extraStats = chartListing.find('div', {'class':'chart-list-item__stats'})
        weeksOnChart = extraStats.find('div', {'class':'chart-list-item__weeks-on-chart'}).get_text()

        # Get Peak Rank
        peakRank = extraStats.find('div', {'class':'chart-list-item__weeks-at-one'}).get_text()

        # Find URL
        artistName = chartListing.find('div', {'class':'chart-list-item__artist'})
        url = artistName.find('a')

        # Collect URL (try/except function included listings may not have a URL)
        try:

            if 'href' in url.attrs:
                artistUrl = ((str(url.attrs['href'])))
            else:
                artistUrl = 'N/A'

        except AttributeError:
            artistUrl = 'N/A'

        # Collect Date that Album Peaked
        if 'N/A' in artistUrl:
            numOneHits = 'N/A'
            topTenHits = 'N/A'

        elif '/music/soundtrack' in artistUrl:
            numOneHits = 'N/A'
            topTenHits = 'N/A'

        elif '/music/various-artists' in artistUrl:
            numOneHits = 'N/A'
            topTenHits = 'N/A'


        else:
            # Nested function collects data to place in peakDate variable
            def get_page_data(artistUrl):
                site = requests.get('https://www.billboard.com' + artistUrl + '/chart-history/billboard-200', headers = {'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'})
                s = site.content
                bs = BeautifulSoup(s, 'lxml')

                peakHistory = bs.find('div', {'class':'artist-section--chart-history__stats'})
                try:
                    numOneHits = peakHistory.find_all('span')[1].get_text()
                    topTenHits = peakHistory.find_all('span')[3].get_text()
                    return numOneHits, topTenHits
                except:
                    numOneHits = 'N/A'
                    topTenHits = 'N/A'
                    return numOneHits, topTenHits

            peakInfo = get_page_data(artistUrl)

        billboard_listing = [chartRank, album, artist, peakRank, weeksOnChart, peakInfo[0], peakInfo[1] ]
        c.writerow(billboard_listing)

        chartRank += 1
        if chartRank % 50 == 0:
            r = random.randint(1, 5)
            time.sleep(r)

        # Loading statement while scraping
        if chartRank == 20:
            print('20 listings scraped...')
        elif chartRank == 40:
            print('40 listings scraped...')
        elif chartRank == 60:
            print('60 listings scraped...')
        elif chartRank == 80:
            print('80 listings scraped...')
        elif chartRank == 100:
            print('100 listings scraped...')
        elif chartRank == 120:
            print('120 listings scraped...')
        elif chartRank == 140:
            print('140 listings scraped...')
        elif chartRank == 160:
            print('160 listings scraped...')
        elif chartRank == 180:
            print('180 listings scraped...')

csvfile.close()
print('Complete!')
