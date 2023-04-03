# Running The Application

## Installation

setup a virtualenv with:

```
python -m virtualenv venv
python -m pip install -r requirements.txt
```

### Startup env post setup for development

Simply run `source ./python-venv.sh` to create your virtual environment you require
## Running the application for Development

Running the application can be done by calling one of the following commands

```
# for running in its own window
flet run -d -p 8560 main.py

# for running on the web browser
flet run -w -p 8560 main.py
```

# Packaging

To package the application for deployment run:

```
flet pack main.py --name Encapsulate --icon assets/cube.png
```