# Running The Application

## Installation

setup a virtualenv with:

```
python -m virtualenv venv
python -m pip install -r requirements.txt

```
## Running the application for Development

Running the application can be done by calling one of the following commands

```
# for running in its own window
flet run -d

# for running on the web browser
flet run -p 8080 main.py
```

# Packaging

To package the application for deployment run:

```
flet pack main.py --name Encapsulate --icon assets/cube.png
```