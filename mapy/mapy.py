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
    """
    The Country class contains all the info about the country that's being
    played in the moment; either chosen by the user or selected randomly.
    """
    def __init__(self, name):
        self.name = name
        self.capital = None
        self.neighbors = list()
        self.currency = None


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
                                 'name to test yourself!', nargs='+',
                            type=config.check_valid_country)
        args = parser.parse_args()

        # Checks whether a --country argument was given
        if args.country is not None:
            args.country = ' '.join(args.country).lower()
            if args.country not in config.LIST_OF_AVAILABLE_COUNTRIES:
                config.invalid_country_exception(country_name=args.country,
                                                 msg="{} is an incomplete "
                                                     "country name!")
        return args

    prettify = lambda self, arg: \
        ' '.join([word[:1].upper() + word[1:]
                  if word.lower() not in ['and', 'of', 'the']
                  else word[:1].lower() + word[1:]
                  for word in re.split('\W+', arg)])

    def run(self, args):
        """
        Runs the program
        """
        self.set_vars(args=args)
        while True:
            # Game starts
            self.init_country_details()

            # Reformat fields to be pretty
            self.country.name = self.prettify(self.country.name)
            self.country.currency = self.prettify(self.country.currency)

            # Greeting
            print('Hello, welcome to {}!'.format(self.country.name))

            # Currency question
            currency_answer = input('What currency is used here? ')
            if currency_answer.lower() == self.country.currency.lower():
                print('You got it right! The currency is indeed {}!'.format(
                    self.country.currency))
            else:
                print("Whoops, you got it wrong!\nThe currency is not {}, "
                      "but {}!\nNot to worry, you'll get it next "
                      "time".format(currency_answer, self.country.currency))

            # Neighbors question
            print("It's time to test you with neighbors!\nLet's see if you"
                  " remember all of the countries that share a border with {}:"
                  "\n(enter them one by one. If the country has no neighbors, "
                  "write `none`.)\n".format(self.country.name))
            neighbors_list_so_far = list()

            if len(self.country.neighbors) != 0:
                for i in range(len(self.country.neighbors)):
                    neighbor_answer = input("Enter a neighbor country's name: ").lower()
                    if neighbor_answer in self.country.neighbors:
                        if neighbor_answer not in neighbors_list_so_far:
                            neighbors_list_so_far.append(neighbor_answer)
                            print("Yes! It is indeed a neighbor!")
                            if (i + 1) != len(self.country.neighbors):
                                print("Let's continue, we're not done yet.\n")
                        else:
                            print("You've already listed this country, try again!")
                            break
                    else:
                        print("Whoops, this country is not a neighbor! Sorry!")
                        break

            # If the number of neighbors is 0, then expecting 'none' from user
            else:
                no_neighbors_answer = input("Enter a neighbor country's name: ")
                if no_neighbors_answer.lower() != 'none':
                    print("This country has no neighbors at all! Next time,"
                          " write `none`.")
                else:
                    print("You're right!!")

            # Game ends
            play_or_not = input('\nDo you want to play another game? (y\\n): ')
            if play_or_not != 'y':
                break

            # Another game; get another country name to play
            self.randomize_country()

    def set_vars(self, args):
        """
        Sets command line variables passed into instance variables
        """
        if args.country:

            # args.country is either a list or a string; treat it accordingly
            if isinstance(args.country, list):
                self.country = Country(name=' '.join(args.country))
            else:
                self.country = Country(name=args.country)
        else:

            # Note that randomize_country also sets self.country to a value
            self.randomize_country()
        self.country.name = self.country.name.lower()

    def randomize_country(self):
        self.country = Country(name=random.choice(
            config.LIST_OF_AVAILABLE_COUNTRIES))

    def init_country_details(self):
        self.get_neighboring_countries()
        self.get_currency()

    def enter_country_details_page(self):
        # Initialize a browser object and open Geonames countries page
        browser = RoboBrowser(parser='html.parser')
        browser.open(config.GEONAMES_COUNTRIES)

        # Look for the link to the desired country page
        formatted_country_name = self.country.name.replace(' ', '')
        country_details_page = config.GEONAMES_HOMEPAGE + \
                               browser.select('.restable')[0]. \
                               find('a', href=re.compile \
                               (formatted_country_name))['href']
        browser.open(country_details_page)
        return browser

    def get_neighboring_countries(self):
        browser = self.enter_country_details_page()

        # Adding the current's country neighbors to the property neighbors
        self.country.neighbors.extend([
            country_tag.string.lower() for country_tag in browser.find_all('a')
            if str(country_tag.string).lower() in
               config.LIST_OF_AVAILABLE_COUNTRIES
            and str(country_tag.string).lower() != self.country.name])

    def get_currency(self):
        browser = self.enter_country_details_page()
        self.country.currency = ' '.join(str(browser.find(
            string=re.compile(r'\([A-Z]'))).split()[:-1]).lower()
