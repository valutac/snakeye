[![PyPI version](https://badge.fury.io/py/snakeye.svg)](https://badge.fury.io/py/snakeye)
<p align="center">
<img src="https://raw.githubusercontent.com/valutac/snakeye/master/assets/snakeye-logo.png" alt="Logo" width="60%">
  </p>
 
```
$ snakeye
Console Tool

Usage:
  command [options] [arguments]

Options:
  -h, --help                      Display this help message
  -q, --quiet                     Do not output any message
  -V, --version                   Display this application version
      --ansi                      Force ANSI output
      --no-ansi                   Disable ANSI output
  -n, --no-interaction            Do not ask any interactive question
  -v|vv|vvv, --verbose[=VERBOSE]  Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug

Available commands:
  build    Build Current Project
  create   Create New Project
  dep      List Dependencies of the Project
  help     Displays help for a command
  list     Lists commands
  publish  Publish Current Project
```

## Installation

Snakeye provide custom installer which you cand download from

```
XXXX
```


## What's inside

Snakeye allow user to handle dependencies installation needed to build and publish python package, the configuration used by snakeye follow the standard of PEP-518, it's standarized file for future python packaging called `pyproject.toml`, ehem! it replace the powerful `setup.py`,`setup.cfg` and of `pipfile`

Here's example of `pyproject.toml` used by Snakeye, at this stage Snakeye still use `flit`:

```
[build-system]
requires = ["flit"]
build-backend = "flit.buildapi"

[tool.flit.metadata]
module = "snakeye-dev"
author = "Duta"
author-email = "duta@mail.com"
home-page = "https://oonlab.com"
requires = [""]
requires-python = ">=3"
description-file = "README.md"


[tool.snakeye.metadata]
pkg_name = "snakeye-dev"
pkg_version = "0.1"
author = "Duta"
author_email = "duta@mail.com"
description = "short description"
long_description = "so long description"
url = "https://oonlab.com"
```

## Available Command

### Create

Create command will ask few question related to project:

```
What's version number: 0.1
Author Name: Rizky
Author Email: duta@mail.com
Description: Short Description
Long Description: So long description
URL/Homepage: http://oonlab.com
License (mit / apache / gpl / leave blank for empty license): mit
```

Snakeye then create following python project structure:

```
├── LICENSE
├── README.md
├── pyproject.toml
└── testproject
    └── __init__.py
```


### Dep

Dependencies command will list all installed dependencies

### Build
### Publish
### Install