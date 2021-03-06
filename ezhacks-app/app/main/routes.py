from flask import render_template
from app.main import bp
from app.models import MarketData


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/explore')
def explore():
    """
    view data as a table
    """
    items = MarketData.query.all()
    return render_template('main/explore.html', items=items)


@bp.route('/about')
def index():
    return render_template('main/about.html')
