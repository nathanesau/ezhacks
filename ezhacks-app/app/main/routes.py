from flask import render_template, request
from app.main import bp
from app.models import MarketData
from flask_paginate import Pagination, get_page_parameter
from sqlalchemy import func, or_
import requests
import json

# utils
def get_page_items(items, page, page_size):
    return items[(page-1)*page_size: (page)*page_size]


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/explore')
def explore():
    """
    view data as a table
    """
    page = request.args.get(get_page_parameter(), type=int, default=1)
    search_value = request.args.get('search_value')
    companies = MarketData.query.all() if not search_value else \
        MarketData.query.filter(func.lower(MarketData.description).contains(
            func.lower(search_value))).all()
    items = get_page_items(companies, page, page_size=25)
    pagination = Pagination(page=page, total=len(companies), search=False,
                            record_name='companies', css_framework='bootstrap4', per_page=25)
    return render_template('main/explore.html', items=items, pagination=pagination)


@bp.route('/about')
def about():
    return render_template('main/about.html')


@bp.route('/company')
def company():
    page = request.args.get(get_page_parameter(), type=int, default=1)
    id = request.args.get('id')
    company = MarketData.query.get(id)
    try:
        data = requests.get(company.url)
        jvalues = json.loads(data.text.replace("'", "\""))
        closing_price = jvalues['c']
        volume = jvalues['v']
        values = []
        for i in range(len(closing_price)):
            values.append({"week": i+1, "closing_price": closing_price[i], "volume": volume[i]})
        items = get_page_items(values, page, page_size=25)
        pagination = Pagination(page=page, total=len(values), search=False,
                                record_name='weeks', css_framework='bootstrap4', per_page=25)
    except:
        items = None
        pagination = None
    return render_template('main/company.html', company=company, items=items, pagination=pagination)
