import argparse
from robobrowser import RoboBrowser

GEONAMES_HOMEPAGE = 'https://www.geonames.org'
GEONAMES_COUNTRIES = 'https://www.geonames.org/countries/'


def get_available_countries():
    browser = RoboBrowser(parser='html.parser')
    browser.open(GEONAMES_COUNTRIES)
    return [country_name.string.lower()
            for country_name in browser.select('.restable ')[0].find_all('a')
            if country_name.string is not None]


LIST_OF_AVAILABLE_COUNTRIES = get_available_countries()

current_given_country_name = ''
current_number_of_given_args = 0

def check_valid_country(given_partial_country_name):
    # if given_country_args.lower() not in LIST_OF_AVAILABLE_COUNTRIES:
    #     msg = "{} is not a valid country name.".format(given_country_args)
    #     raise argparse.ArgumentTypeError(msg)
    print(given_partial_country_name)
    global current_number_of_given_args
    global current_given_country_name
    print('got here')
    current_given_country_name += given_partial_country_name
    print(current_given_country_name)
    print([' '.join(country_name.split()[:current_number_of_given_args])
             for country_name in LIST_OF_AVAILABLE_COUNTRIES
             if len(country_name.split() > current_number_of_given_args)])

    if current_given_country_name.lower() not in LIST_OF_AVAILABLE_COUNTRIES \
        and current_given_country_name.lower() not in \
            [' '.join(country_name.split()[:current_number_of_given_args])
             for country_name in LIST_OF_AVAILABLE_COUNTRIES
             if len(country_name.split() > current_number_of_given_args)]:
        msg = "{} is neither a valid country name, nor a part of one.".format(given_partial_country_name)
        raise argparse.ArgumentTypeError(msg)
    current_number_of_given_args += 1
    return given_partial_country_name
