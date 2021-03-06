# Mastering the HigherLower-Game

A few days ago I stumbled upon the [HigherLower Game](https://www.higherlowergame.com/) and got instantly addicted in a strange way. The task is to tell if a term got googled more or less than another one.
But unfortunately I was realy bad. Like really. I had nothing else to do beside learning and assignments for uni. So basically a lot of free time (*nervous laugh*). 
Thus I wrote a `python` program wich should play for me and master the game.

## Approach
Since the game is a purly `javascript` generated website with only `javascript` links I went went with Selenium. Selenium is a suite of tools specifically for automating web browsers. For more informations: [www.seleniumhq.org](https://www.seleniumhq.org/).
For the sake of simplicity, the program learns all values by try and error. It reads the terms and their values and stores them in a dictionary. 

## The Code
The code is pretty much self-explaining. Just take a look in the files. For the sake of completeness I put in a 'Code'-Section anyway, just to look kind of professional :D.
### `hlc.py`
Contains a class which brings all the methods needed for learning the values and playing the game.

### `learn.py`
Contains the learning routine.

## Results
After one and a half day of learnig the program has played the game through. The total length of the dictionary is `1557`. The data is stored in `hlc.data` via the `pickle` module.

## Requirements
If you want to run it yourself for days, you must be stupid. A lot of them are dependencies of selnium. These are the python libs you need (i set up a python venv):
```bash
$ pip freeze
asn1crypto==0.24.0
bcrypt==3.1.5
certifi==2018.11.29
cffi==1.11.5
chardet==3.0.4
cryptography==2.4.2
idna==2.8
paramiko==2.4.2
pkg-resources==0.0.0
pyasn1==0.4.5
pycparser==2.19
PyNaCl==1.3.0
python-xlib==0.23
selenium==3.141.0
six==1.12.0
tldextract==2.2.0
urllib3>=1.24.2
```
Ater installing the requirements you migth get the following error:
`selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.`
Have a look at this StackOverflow question/answer ([Selenium using Python - Geckodriver executable needs to be in PATH ](https://stackoverflow.com/questions/40208051/selenium-using-python-geckodriver-executable-needs-to-be-in-path?answertab=votes#tab-top)) for further information and solution.
