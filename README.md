# ezhacks

EZHacks2021 hackathon at Simon Fraser University.

We built a web app. It is live at http://ezhacks2021.strangled.net:5000.

<!-- host ip: 138.197.155.240 -->

## About

All our code was written in python. We got the data from finnhub. We used dataprep to pull the data. We used matplotlib to create the plots. We created the site using flask. The site allows you to view the graphs and the data that we used.

## Development Instructions

Requirements:

* [dataprep](https://github.com/sfu-db/dataprep)
* [flask](https://github.com/pallets/flask)
* [pandas](https://github.com/pandas-dev/pandas)
* [requests](https://github.com/psf/requests)

## Deployment Instructions

To run the site on DigitalOcean, use the following command(s):

```bash
# run the image
docker run -p 80:80 --name ezhacks-app -d nathanesau/ezhacks:ezhacks-app
```

## Folder Structure

* data: contains the data, obtained using [finnhub](https://finnhub.io/) and [dataprep](https://github.com/sfu-db/dataprep)
* dataprep-code: contains our dataprep-code
* ezhacks-app: contains the flask app
* ezhacks-nginx: contains the nginx configuration
* scripts: contains scripts for creating graphs, populating db, etc.
