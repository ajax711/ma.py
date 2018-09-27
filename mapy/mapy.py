# All rights to data gathered from the website geonames.org belongs
# to geonames.
# The work is licenced under Attribution 4.0 International (CC BY 4.0)
# to be found here https://creativecommons.org/licenses/by/4.0/legalcode
# Further information can be found under LICENSE and geonames.org.

import config
import random
from robobrowser import RoboBrowser
import re


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
                            type=config.get_available_countries)
        args = parser.parse_args()
        return args

    def run(self, args):
        """
        Runs the program
        """
        self.set_vars(args=args)
        while True:
            self.play_game()
            play_or_not = input('\nDo you want to play another game? (y\\n)\n')
            if play_or_not != 'y':
                break
            self.randomize_country()

    def set_vars(self, args):
        """
        Sets command line variables passed into instance variables
        """
        if args.country:
            self.country = args.country
        else:
            self.randomize_country()
        self.country = self.country.lower()

    def randomize_country(self):
        self.country = random.choice(config.LIST_OF_AVAILABLE_COUNTRIES)

    def play_game(self):
        neighbor_countries = self.get_neighboring_countries()

    def get_neighboring_countries(self):
        browser = RoboBrowser()
        browser.open('https://www.geonames.org/countries/')
        country_details_page = config.GEONAMES_HOMEPAGE + \
                                   browser.select('.restable ')[0].\
                                   find('a', href=re.compile(self.country))['href']
        browser.open(country_details_page)
        # print(config.LIST_OF_AVAILABLE_COUNTRIES)
        neighbor_countries = [country_tag.string for country_tag in browser.find_all('a')
                              if str(country_tag.string).lower() in config.LIST_OF_AVAILABLE_COUNTRIES
                              and str(country_tag.string).lower() != self.country]
        # print(neighbor_countries)
