# Description

# Requirements

* Python 3.11.2

First we'll want to install pipenv.


```
brew install pipenv

# If you don't have brew, run this instead
python3 -m pip install --user pipenv
```

```
PYTHON_VER=3.11.2
pyenv install $PYTHON_VER
pyenv virtualenv $PYTHON_VER user_mgt
```

install dependencies.
```
pipenv install --dev
```
