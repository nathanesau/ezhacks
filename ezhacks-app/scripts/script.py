import requests
from datetime import datetime
import os
import json

from dataprep.eda import plot

DATA_FOLDER = "company_data"

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
    with open("companies_list.txt", "r") as f:
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

def get_year_difference(company_data):
    differenceYear = 0
    
    if company_data.get('h'):
        differenceYear = company_data['l'][-1] - company_data['h'][0]
    return float("{:.2f}".format(differenceYear))

def read_company_data(company):
    path = os.path.join(DATA_FOLDER, company)
    with open(path + ".csv", "r") as fp:
        return json.loads(fp.read().replace('\'','"'))

if __name__ == "__main__":
    #path = os.path.join(DATA_FOLDER, "MC")
    #saveToFile(path, get_company_data("MC"))
    #path = os.path.join(DATA_FOLDER, "BRK.A")
    #saveToFile(path, get_company_data("BRK.A"))
    #save_companies_data()

    differences = []

    for company in get_company_names():
        company_data = read_company_data(company)
        difference = get_year_difference(company_data)
        differences.append({"company_name":company,"year_difference":difference})
        print(f"reading company {company}")

    differences.sort(key=lambda el: el["year_difference"], reverse=True)

    print(f"Top Winners : {differences[:9]}")
    print(f"Top Losers : {differences[-1:-10:-1]}")
    
    #app.run(host='0.0.0.0', port=5000)
