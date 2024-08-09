# Helpdesk API

## Description

Helpdesk API is a RESTful API built in Python using Flask that receives computer information from the Helpdesk Service to provide that information to users of the Helpdesk Tool. It is intended to be used in conjunction with the [Helpdesk Service](https://github.com/hdlane/helpdesk-service) and [Helpdesk Tool](https://github.com/hdlane/helpdesk-tool).

### Goal

The goal of the Helpdesk API is to make a RESTful API endpoint that can be used to quickly get data from computers to the Helpdesk Tool.

### Background

Having the Helpdesk Tool and Helpdesk Service communicate meant that a shared endpoint was needed. I wanted to provide an API that could be spun up quickly to be useful to a team. 

### Features

* Receives data from Helpdesk Service to create and read from SQLite database
* Sends JSON data to Helpdesk Tool when requested

## Installation

Clone repo down from Github.

```
git clone https://github.com/hdlane/helpdesk-api.git
```

Setup your Python virtualenv and install Flask. Then run `flask run`.

```
python -m venv .venv
source .venv/bin/activate
pip install flask
flask run
```

## Usage

## License

[MIT](https://choosealicense.com/licenses/mit/)
