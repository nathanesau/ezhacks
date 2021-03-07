"""
downloads data from finnhub api
creates winners plot
creates losers plot
creates dramatics plot
"""
import requests
from datetime import datetime
import os
import json
import pandas as pd
import matplotlib.pyplot as plt

BASEDIR = os.path.dirname(os.path.realpath(__file__))
DATA_FOLDER = f"{BASEDIR}/../data/company_data"

def get_company_data(company_name):
    # requests syntax
    response = requests.get((
        f"https://finnhub.io/api/v1/stock/candle?resolution=W&from={int(datetime(2020,1,1).timestamp())}"
        f"&to={int(datetime(2021,1,1).timestamp())}&symbol={company_name}&token=c11tv0v48v6p2grlkudg"
    ))
    data = response.json()
    return data

def get_company_names():
    companies = []
    # includes S and P 500 and Zoom
    with open(f"{BASEDIR}/../data/companies_list.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            companies.append(line.strip('\n'))
    return companies

def save_companies_data():
    companies = get_company_names()
    differences = []

    for company in companies:
        print(f"saving company: {company}")
        data = get_company_data(company)
        filePath = os.path.join(DATA_FOLDER, company.strip('\n'))
        saveToFile(filePath, data)

    return differences

def saveToFile(path, data):
    with open(path + ".csv", "w") as fp:
        fp.write(str(data))

def get_year_volatility(company_data):
    volatilityYear = 0

    if company_data.get('c'):
        volatilityYear = (max(company_data['c']) - min(company_data['c']))/company_data['c'][0]

    return float("{:.2f}".format(volatilityYear))

def get_year_difference(company_data):
    differenceYear = 0

    if company_data.get('c'):
        differenceYear = (company_data['c'][-1] - company_data['c'][0])/company_data['c'][0] * 100
    return float("{:.2f}".format(differenceYear))

def read_company_data(company):
    path = os.path.join(DATA_FOLDER, company)
    with open(path + ".csv", "r") as fp:
        return json.loads(fp.read().replace('\'','"'))

if __name__ == "__main__":

    # uncomment to collect all data
    # upload data to https://ezhacks.nyc3.digitaloceanspaces.com
    #path = os.path.join(DATA_FOLDER, "MC")
    #saveToFile(path, get_company_data("MC"))
    #path = os.path.join(DATA_FOLDER, "BRK.A")
    #saveToFile(path, get_company_data("BRK.A"))
    #save_companies_data()

    differences = []
    volatilities = []

    for company in get_company_names():
        company_data = read_company_data(company)
        volatility = get_year_volatility(company_data)
        volatilities.append({"company_name":company,"year_volatility":volatility})
        difference = get_year_difference(company_data)
        differences.append({"company_name":company,"year_difference":difference})
        print(f"reading company {company}")

    volatilities.sort(key=lambda el: el["year_volatility"], reverse=True)
    differences.sort(key=lambda el: el["year_difference"], reverse=True)

    print(f"Top Winners : {differences[:30]}")
    print(f"Top Losers : {differences[-1:-30:-1]}")

    winners = [e["company_name"] for e in differences[:10]]
    for winner in winners:
        company_data = read_company_data(winner)
        data = company_data['c']
        initial = data[0]
        for i in range(len(data)): data[i] = (data[i] / initial - 1) * 100
        plt.plot(company_data['c'], label=winner)
    plt.legend()
    plt.xlabel("Week of 2020")
    plt.ylabel("Percent Change in Price")
    plt.savefig('winners.png')

    losers = [e["company_name"] for e in differences[-1:-10:-1]]
    for loser in losers:
        company_data = read_company_data(loser)
        data = company_data['c']
        initial = data[0]
        for i in range(len(data)): data[i] = (data[i] / initial - 1) * 100
        plt.plot(company_data['c'], label=loser)
    plt.legend()
    plt.xlabel("Week of 2020")
    plt.ylabel("Percent Change in Price")
    plt.savefig('losers.png')

    dramatics = [(e["company_name"], e["year_volatility"]) for e in volatilities[:10]]
    for value in dramatics:
        dramatic, volatility = value
        company_data = read_company_data(dramatic)
        data = company_data['c']
        initial = data[0]
        for i in range(len(data)): data[i] = (data[i] / initial - 1) * 100
        plt.plot(company_data['c'], label=f"{dramatic} ({volatility} %)")
    plt.legend()
    plt.xlabel("Week of 2020")
    plt.ylabel("Percent Change in Price")
    plt.savefig('dramatics.png')
