# ma.py
:earth_africa: *ma.py* is a CLI (command-line interface) game that utilizes your operating system's terminal (be it Command Line in Windows or Terminal in Apple's OS X, Linux) to quiz you on your geographical knowledge. :earth_asia:

## Table of contents
 - [Introduction](#introduction)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Techy details](#techy-details)
 - [License](#license)
 - [Feedback](#feedback)

## Introduction
ma.py runs on your terminal, and tests you with an almost infinite database (yes, 196 is close to infinity! Or at least [I'd like to think so](https://math.stackexchange.com/questions/443099/when-does-it-make-sense-to-say-that-something-is-almost-infinite)), consisting of all of the world's countries, even including the [newest ones](https://www.washingtonpost.com/news/worldviews/wp/2014/09/16/the-9-newest-countries-in-the-world/?noredirect=on&utm_term=.e39e47881d5d).
I'm tired of trivia-like games on geography, that keep testing me on [capital cities of countries](https://www.jetpunk.com/quizzes/name-world-capitals), [naming all of the U.S states](https://www.sporcle.com/games/g/states) and last but not least -- [which continent does a country belong to](https://www.sporcle.com/games/Gneath/100-countries-which-continent-is-that-country-in)!! Yuck.

**ma.py** tests you on pieces of knowledge you wouldn't had found anywhere else, such as;
 - What is the country's official currency name? (Did you know how many countries [don't even have a currency of their own?!](https://qz.com/260980/meet-the-countries-that-dont-use-their-own-currency/))
  - Which countries are neighbors (share borders) with which countries?
  ... and more to come!
  
  ## Why even create such a game?!
  If that was not clear enough by now, I'm pretty much a geography nerd; I like everything there is about countries and diplomatics! I enjoy reading and learning about relations between different countries, and games like these help me sharpen my trivia knowledge. I used to be so interested in diplomatics, that I even had the chance to take a university course in Introduction to [International Relations](https://en.wikipedia.org/wiki/International_relations). I'm fun in parties, [I swear](https://upload.wikimedia.org/wikipedia/commons/8/85/HHGTHG_1979_ICA_Stage_Production_Flyer.jpg)!
  
  ## Installation
  The only prerequisite is having [Python 3](https://www.python.org/downloads/) installed.
  Running the game is simple as:
   - Clone the git repository to your desired folder: `git clone https://github.com/tsehori/ma.py`
   - From the folder you downloaded the repository to, go to the folder *ma.py*, using your operating system's terminal: `cd ma.py`
   - Install the requirements described in [requirements.txt](https://github.com/tsehori/ma.py/blob/master/requirements.txt) as [described here](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a).
   - Go to the folder mapy `cd mapy`
   The program should now be installed completely. To check whether everything is okay, check out [usage](#usage).
   
   ## Usage
   To run the game, you have two options at the moment:
   - Either run it with no options: `python main.py` or `python3 main.py` (whichever works). This should run the game without a pre-chosen country; the program will randomly choose a country for you to be quizzed on.
   - Run it with the `-c` or `--country` option: `python main.py -c country_name` (in *country_name*, enter a name of a country you want to be quizzed on). If the country you wrote isn't recognized by the game, take a look in [geonames' list of countries](https://www.geonames.org/countries/), to see how it is spelled. (The game is **insensitive** to capital letters; do not worry about it!)
   
   Regardless of the option you choose, after testing you on the first country, the game will randomly generate the next countries, so you can keep on improving your knowledge (instead of your [country-spelling-skills](https://en.wikipedia.org/wiki/Djibouti); definitiely an important skill, but still).
   
   ## Techy details
   Throughout structuring and developing *ma.py*, I have run into many obstacles and challenges. This is my first 'big' Python project, in which I tried to implement best practices and 'Pythonic' code; incorporating [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) design, using diverse Python libraries (both from the [standard library](https://docs.python.org/3/library/) and 3rd party) and using [virtualenv](https://virtualenv.pypa.io/en/stable/) to create an isolated Python environment, that allowed me to work on ma.py independent from other projects and repositories.
   
   Moreover, during the project, I incorporated some of [Git](https://git-scm.com/)'s main functionalities: initializing the git repository and pushing it remotely into GitHub, adding relevant parts to each commit, documenting all commits explicitly, branching, pull requesting, etc.
   
   **Most used and vital libraries used in the project:**
   - [*argparse*](https://docs.python.org/3/library/argparse.html) from the standard library. I mainly used it to make a user-friendly CLI. In the progress, I've used many of the library's methods, and by chance, turned into some of the advanced methods to fit the program's needs.
   An example for such a case can be found [here](https://github.com/tsehori/ma.py/blob/master/mapy/mapy.py#L37). In short; I didn't want to make the user choose from the [library's choices method](https://docs.python.org/3/library/argparse.html#choices), because, if the user was to mis-spell a country name (from the list of 196~ countries), he'd get an enormous, unfriendly message issued by an argparse exception. I chose to make use of the [type method](https://docs.python.org/3/library/argparse.html#type), and pass a custom [function](https://github.com/tsehori/ma.py/blob/master/mapy/config.py#L28) to it.
   - [*RoboBrowser*](https://github.com/jmcarp/robobrowser), a 3rd party library I've found in GitHub. Essentially, RoboBrowser allows to browse the web without a standalone web browser; it is capable of entering pages, filling forms and submitting them, etc. Furthermore, I think it's best ability is how it incorporates the wonderful library [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/); BS allows for "easy" web scraping, which is useful especially in cases where a website does not have a proper API. In this case, the website [geonames.org](https://www.geonames.org/) does have an [API](http://www.geonames.org/export/web-services.html), and there even exists a [geonames Python wrapper](https://pypi.org/project/geonames/) and a [another one](https://gist.github.com/Markbnj/e1541d15699c4d2d8c98), but using all of the above, in my opinion, where far more complicated than using BeautifulSoup on its own.
   - [*re*](https://docs.python.org/3/howto/regex.html) from the standard library. I won't get into much deatil about regular expressions and their applications; in ma.py, I've used them mainly together with BeautifulSoup, to locate some text patterns in the webpages of geonames, in order to make use of them in the program.
   - [*random*](https://docs.python.org/3/library/random.html) from the standard library; used in order to randomize country selection to be automated.
   - [*pyfiglet*](https://github.com/pwaller/pyfiglet) was used to create a pretty ASCII title for the game. I'm a fan of ASCII art, but ain't much of an artist myself :art:
   
   ## License
   Full license is written [here](https://github.com/tsehori/ma.py/blob/master/LICENSE). All rights to data gathered from geonames.com belongs to them and them only; you can read all the relevant details in lines [1](https://github.com/tsehori/ma.py/blob/master/LICENSE#L1) to 7.
   
   ## Feedback
   Please, give me your harshest feedback! Feel free to [file an issue](https://github.com/tsehori/ma.py/issues/new), ask for a new feature, [open a pull request](https://github.com/tsehori/ma.py/pulls) for a cool new feature (or a bug fix!), and if you feel generous, [star](https://commons.wikimedia.org/wiki/File:Pluto_in_True_Color_-_High-Res.jpg#/media/File:Pluto_in_True_Color_-_High-Res.jpg) this repo :star:
