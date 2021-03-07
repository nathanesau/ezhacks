# ezhacks

EZHacks2021 hackathon at Simon Fraser University.

We built a web app. It is live at http://ezhacks2021.strangled.net:5000.

<!-- host ip: 138.197.155.240 -->

## Development Instructions

Requirements:

* [dataprep](https://github.com/sfu-db/dataprep)
* [flask](https://github.com/pallets/flask)
* [pandas](https://github.com/pandas-dev/pandas)
* [requests](https://github.com/psf/requests)

## Folder Structure

* data: contains the data, obtained using [finnhub](https://finnhub.io/) and [dataprep](https://github.com/sfu-db/dataprep)
* ezhacks-app: contains the flask app
* ezhacks-nginx: contains the nginx configuration
* scripts: contains scripts for creating graphs, populating db, etc.
