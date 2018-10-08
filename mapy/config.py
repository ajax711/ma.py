import argparse
from robobrowser import RoboBrowser

GEONAMES_HOMEPAGE = 'https://www.geonames.org'
GEONAMES_COUNTRIES = 'https://www.geonames.org/countries/'


def get_available_countries():
    """
    :return: list of countries as presented in url
             GEONAMES_COUNTRIES.
    """
    browser = RoboBrowser(parser='html.parser')
    browser.open(GEONAMES_COUNTRIES)
    return [country_name.string.lower()
            for country_name in browser.select('.restable ')[0].find_all('a')
            if country_name.string is not None]


LIST_OF_AVAILABLE_COUNTRIES = get_available_countries()

current_given_country_name = ''
current_number_of_given_args = 0


def invalid_country_exception(country_name,
                              msg="{} is neither a valid country name,"
                                  " nor a part of one."):
    """
    :param country_name: Country name of the current game's country.
    :param msg: Customized message.
    :return: argparse type error exception.
    """
    raise argparse.ArgumentTypeError(msg.format(country_name))


def check_valid_country(given_partial_country_name):
    """
    :param given_partial_country_name: The user's argument (country name)
           is given word by word.
           For example, if we call the function with `--country ivory coast`,
           then this method will be called twice: once with
           given_partial_country_name='ivory' and second time with 'coast'.
    :return: We return each time only the partial country name (only 'ivory'
             or 'coast'), where the entire country name read so far is saved
             in current_given_country_name.
    """
    global current_number_of_given_args
    global current_given_country_name
    if current_number_of_given_args == 0:
        current_given_country_name += given_partial_country_name
    else:
        current_given_country_name += ' ' + given_partial_country_name
    current_number_of_given_args += 1

    if current_given_country_name.lower() not in LIST_OF_AVAILABLE_COUNTRIES \
        and current_given_country_name.lower() not in \
            [' '.join(country_name.split()[:current_number_of_given_args])
             for country_name in LIST_OF_AVAILABLE_COUNTRIES
             if len(country_name.split()) > current_number_of_given_args]:
        invalid_country_exception(current_given_country_name)

    return given_partial_country_name
