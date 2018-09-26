import config
import random


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
        Starts the game
        """
        self.set_vars(args=args)
        while True:
            self.play_game(args=args)
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

    def randomize_country(self):
        self.country = random.choice(config.LIST_OF_AVAILABLE_COUNTRIES)

    def play_game(self, args):
        pass
