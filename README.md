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

Enter the cloned repo and setup your Python virtualenv and install Flask. Then run `flask run`.

```
cd helpdesk-api
python -m venv .venv
source .venv/bin/activate
pip install flask
flask run
```

## Usage

When the API endpoint is running, it is listening for GET and POST requests. When a GET request is recieved, it will query the database and send that data in JSON format. When a POST request is received, it will validate the data, update computer records based on MAC address, and create a new record if it's not already present. 

## License

[MIT](https://choosealicense.com/licenses/mit/)
