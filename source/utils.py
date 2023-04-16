import requests
import builtwith
import whois
from bs4 import BeautifulSoup
import re
import pandas as pd

def get_HTML(url):
        '''
        Returns the HTML file of a webpage by its link

        Parameters
        ----------
            url (str): link of the webpage

        Returns
        -------
            HTML file of the webpage
        '''
        # First, we need to request the contents of the webpage
        page = requests.get(url)
        
        # Then we return its HTML file
        return BeautifulSoup(page.content, features="lxml")


def get_links(html, scrape_type):
        """
        Returns a list of the links from Countries or Cities to be scraped from the main webpage

        Parameters
        ----------
            html (str): HTML code of the original page
            scrape_type (bool): True if the scraping is for Cities, False for Countries

        Returns
        -------
            List of string values which are the links to the pages

        """
        if scrape_type:
            # From the HTML file, we collect all the <td> tags that have a class = "city-name"
            td_tags = html.find_all('td', {"class": "city-name"})
        else:
            # From the HTML file, we collect all the <td> tags that have a class = "country-name"
            td_tags = html.find_all('td', {"class": "country-name"})

        # Then, for every <td> tag, we get the hyperlink in its <a> tag and add the extra currency reference
        cities_links = [td.find('a').get('href') + "?currency=EUR" for td in td_tags]
        return cities_links


def get_ranking_pos(html, num_digits):
        """
        Returns the ranking position of a particular Country

        Parameters
        ----------
            html (str): HTML code of the Country's page
            num_digits (int): 3 if the scraping is for Cities, 2 for Countries

        Returns
        -------
            Number of the position in string format

        """
        # First, we get all <li> tags that have a class = "key-point"
        li_tags = html.findAll('li', {'class': 'key-point'})
        
        # For every <li> tag
        for li in li_tags:
            # If the word "World" is in its text
            if 'World' in li.text:
                # We split the whole text by the word "World", keeping the side after it
                text = li.text.split("World", 1)[1].strip()
                # From the remaining text we get the first 1 or 2 digits that appear for Countries
                # and 1 to 3 for Cities
                pattern = r'\b(\d{1,' + str(num_digits) + r'})\b'
                pos = re.search(pattern, text).group(1)
                
        return pos

    
def saving(file_name, dataset):
        """
        Creates a Pandas Dataframe from the scraped data to save it as a CSV dataset

        Parameters
        ----------
            file_name (str): name for teh CSV file
            dataset (str): JSON that contains all the scraped information

        """
        # Let's create a Pandas Dataframe with the obtained dataset
        expatistan_df = pd.DataFrame(dataset)
        
        # Now we save it as a CSV file with no index column
        expatistan_df.to_csv(file_name, index = False)
        
        print("\nDataset {} saved as CSV file!".format(file_name))