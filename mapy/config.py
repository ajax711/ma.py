import pycountry
import argparse


def get_available_countries(given_country_name):
    list_of_available_countries = [country.name.lower()
                                   for country in pycountry.countries]
    if given_country_name.lower() not in list_of_available_countries:
        msg = "{} is not a valid country name.".format(given_country_name)
        raise argparse.ArgumentTypeError(msg)
    return given_country_name
