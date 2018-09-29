import argparse
from robobrowser import RoboBrowser
import re

GEONAMES_HOMEPAGE = 'https://www.geonames.org'
GEONAMES_COUNTRIES = 'https://www.geonames.org/countries/'


def get_available_countries():
    browser = RoboBrowser()
    browser.open(GEONAMES_COUNTRIES)
    return [country_name.string.lower()
            for country_name in browser.select('.restable ')[0].find_all('a')
            if country_name.string is not None]


LIST_OF_AVAILABLE_COUNTRIES = get_available_countries()


def check_valid_country(given_country_name):
    if given_country_name.lower() not in LIST_OF_AVAILABLE_COUNTRIES:
        msg = "{} is not a valid country name.".format(given_country_name)
        raise argparse.ArgumentTypeError(msg)
    return given_country_name
