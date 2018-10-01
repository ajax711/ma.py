# All rights to data gathered from the website geonames.org belongs
# to geonames.
# The work is licenced under Attribution 4.0 International (CC BY 4.0)
# to be found here https://creativecommons.org/licenses/by/4.0/legalcode
# Further information can be found under LICENSE and geonames.org.

import config
import random
from robobrowser import RoboBrowser
import re


class Country:
    def __init__(self, name):
        self.name = name
        self.capital = None
        self.neighbors = list()


class Mapy:
    def __init__(self, parser):
        self.country = None
        self.args = self.add_arguments_to_parser(parser=parser)

    def add_arguments_to_parser(self, parser):
        """
        All user given arguments to ma.py
        """
        parser.add_argument('--country', '-c', action='store',
                            help='You may enter a country '
                                 'name to test yourself!',
                            type=config.check_valid_country)
        args = parser.parse_args()
        return args

    def run(self, args):
        """
        Runs the program
        """
        self.set_vars(args=args)
        while True:
            self.init_country_details()
            play_or_not = input('\nDo you want to play another game? (y\\n)\n')
            if play_or_not != 'y':
                break
            self.randomize_country()

    def set_vars(self, args):
        """
        Sets command line variables passed into instance variables
        """
        if args.country:
            self.country = Country(name=args.country)
        else:
            self.randomize_country()
        self.country.name = self.country.name.lower()

    def randomize_country(self):
        # print(config.LIST_OF_AVAILABLE_COUNTRIES)
        self.country = Country(name=random.choice(
            config.LIST_OF_AVAILABLE_COUNTRIES))

    def init_country_details(self):
        self.get_neighboring_countries()

    def get_neighboring_countries(self):
            # Initialize a browser object and open Geonames countries page
            browser = RoboBrowser()
            browser.open(config.GEONAMES_COUNTRIES)

            # Look for the link to the desired country page
            formatted_country_name = self.country.name.replace(' ', '-')
            country_details_page = config.GEONAMES_HOMEPAGE + \
                                       browser.select('.restable')[0].\
                                       find('a', href=re.compile(formatted_country_name))['href']
            browser.open(country_details_page)
            self.country.neighbors.extend([
                country_tag.string for country_tag in browser.find_all('a')
                if str(country_tag.string).lower() in config.LIST_OF_AVAILABLE_COUNTRIES
                and str(country_tag.string).lower() != self.country.name])

            # neighbor_countries = [
            #     country_tag.string for country_tag in browser.find_all('a')
            #     if str(country_tag.string).lower() in config.LIST_OF_AVAILABLE_COUNTRIES
            #     and str(country_tag.string).lower() != self.country]
            # return neighbor_countries

    def determine_relationship(self, other):
        pass
