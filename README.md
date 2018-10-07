# ma.py
*ma.py* is a CLI (command-line interface) game that utilizes your operating system's terminal (be it Command Line in Windows or Terminal in Apple's OS X, Linux) to quiz you on your geographical knowledge.

## Table of contents
 - [Introduction](#introduction)
 - [Installation](#installation)
 - [Usage](#usage)
 - [Feedback](#feedback)

## Introduction
ma.py runs on your terminal, and tests you with an almost infinite database (yes, 196 is close to infinity! Or at least [I'd like to think so](https://math.stackexchange.com/questions/443099/when-does-it-make-sense-to-say-that-something-is-almost-infinite)), consisting of all of the world's countries, even including the [newest ones](https://www.washingtonpost.com/news/worldviews/wp/2014/09/16/the-9-newest-countries-in-the-world/?noredirect=on&utm_term=.e39e47881d5d).
I'm tired of trivia-like games on geography, that keep testing me on [capital cities of countries](https://www.jetpunk.com/quizzes/name-world-capitals), [naming all of the U.S states](https://www.sporcle.com/games/g/states) and last but not least -- [which continent does a country belong to](https://www.sporcle.com/games/Gneath/100-countries-which-continent-is-that-country-in)!! Yuck.

**ma.py** tests you on pieces of knowledge you wouldn't had found anywhere else, such as;
 - What is the country's official currency name? (Did you know how many countries [don't even have a currency of their own?!](https://qz.com/260980/meet-the-countries-that-dont-use-their-own-currency/))
  - Which countries are neighbors (share borders) with which countries?
  ... and more to come!
  
  ## Installation
  The only prerequisite is having [Python 3](https://www.python.org/downloads/) installed.
  Running the game is simple as:
   - Clone the git repository to your desired folder: `git clone https://github.com/tsehori/ma.py`
   - From the folder you downloaded the repository to, go to the folder *ma.py*, using your operating system's terminal: `cd ma.py`
   - Install the requirements described in [requirements.txt]() as [described here](https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a).
   - Go to the folder mapy `cd mapy`
   The program should now be installed completely. To check whether everything is okay, check out [usage](#usage).
   
   ## Usage
   To run the game, you have two options at the moment:
   - Either run it with no options: `python main.py` or `python3 main.py` (whichever works). This should run the game without a pre-chosen country; the program will randomly choose a country for you to be quizzed on.
   - Run it with the `-c` or `--country` option: `python main.py -c country_name` (in *country_name*, enter a name of a country you want to be quizzed on). If the country you wrote isn't recognized by the game, take a look in [geonames' list of countries](https://www.geonames.org/countries/), to see how it is spelled. (The game is **insensitive** to capital letters; do not worry about it!)
   
   Regardless of the option you choose, after testing you on the first country, the game will randomly generate the next countries, so you can keep on improving your knowledge (instead of your [country-spelling-skills](https://en.wikipedia.org/wiki/Djibouti); definitiely an important skill, but still).
   
   ## Techy details
   Throughout structuring and developing *ma.py*, I have run into many obstacles and challenges. This is my first 'big' Python project, in which I tried to implement best practices and 'Pythonic' code; incorporating [OOP](https://en.wikipedia.org/wiki/Object-oriented_programming) design, using diverse Python libraries (both from the [standard library](https://docs.python.org/3/library/) and 3rd party) and more.
   
   **Most used and vital libraries used in the project:**
   - *[argparse](https://docs.python.org/3/library/argparse.html)* from the standard library. I mainly used it to make a user-friendly CLI. In the progress, I've used many of the library's methods, and by chance, turned into some of the advanced methods to fit the program's needs.
   An example for such a case can be found [here](https://github.com/tsehori/ma.py/blob/master/mapy/mapy.py#L37). In short; I didn't want to make the user choose from the [library's choices method](https://docs.python.org/3/library/argparse.html#choices), because, if the user was to mis-spell a country name (from the list of 196~ countries), he'd get an enormous, unfriendly message issued by an argparse exception. I chose to make use of the [type method](https://docs.python.org/3/library/argparse.html#type), and pass a custom [function](https://github.com/tsehori/ma.py/blob/master/mapy/config.py#L28) to it.
   
   ## Feedback
   Please, give me your harshest feedback! Feel free to [file an issue](https://github.com/tsehori/ma.py/issues/new), ask for a new feature, [open a pull request](https://github.com/tsehori/ma.py/pulls) for a cool new feature (or a bug fix!), and if you feel generous, [star](https://commons.wikimedia.org/wiki/File:Pluto_in_True_Color_-_High-Res.jpg#/media/File:Pluto_in_True_Color_-_High-Res.jpg) this repo :star:.
