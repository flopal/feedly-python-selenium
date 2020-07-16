# feedly-python-selenium
Somes python scripts with selenium package and feedly news RSS.

## Requirements

- python3 venv
- selenium
- geckodriver (webdriver mozilla firefox) : https://github.com/mozilla/geckodriver/releases

## Build project

```bash
git clone https://github.com/flopal/feedly-python-selenium.git
cd feedly-python-selenium/
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools
pip install selenium
```

## Run script

```bash
source venv/bin/activate
python fetch_title_and_url_all_feed.py
```

## Clean project

```bash
source venv/bin/activate
pip uninstall $(pip freeze) -y
deactivate
rm -fr venv/
```
