import pycountry
import argparse

LIST_OF_AVAILABLE_COUNTRIES = [country.name.lower()
                               for country in pycountry.countries]


def get_available_countries(given_country_name):
    if given_country_name.lower() not in LIST_OF_AVAILABLE_COUNTRIES:
        msg = "{} is not a valid country name.".format(given_country_name)
        raise argparse.ArgumentTypeError(msg)
    return given_country_name
