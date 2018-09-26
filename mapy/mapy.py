from config import get_available_countries


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
                            type=get_available_countries)
        args = parser.parse_args()
        return args

    def run(self, args):
        """
        Starts the game
        """
        # print(args)
        # print(LIST_OF_AVAILABLE_COUNTRIES)
        pass

    def set_vars(self, args):
        """
        Sets command line variables passed into instance variables
        """
        if args.country:
            self.country = args.country