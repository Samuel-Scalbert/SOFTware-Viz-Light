from flask import Flask, render_template
from pyArango.connection import Connection
from Utils.db import insert_json_db
from Utils.home import home_data
from Utils.desambiguacao import desambiguacao
app = Flask(__name__,template_folder='templates',static_folder='static')

#app.config['ARANGO_HOST'] = 'arangodb'
app.config['ARANGO_HOST'] = 'localhost'
app.config['ARANGO_PORT'] = 8529
app.config['ARANGO_DB'] = 'SOF-viz-light'
app.config['ARANGO_USERNAME'] = 'root'
app.config['ARANGO_PASSWORD'] = 'root'

def init_db():
    global db
    db = Connection(
        arangoURL='http://{host}:{port}'.format(
            host=app.config['ARANGO_HOST'],
            port=app.config['ARANGO_PORT']
        ),
        username=app.config['ARANGO_USERNAME'],
        password=app.config['ARANGO_PASSWORD']
    )
    if not db.hasDatabase('SOF-viz-light'):
        db.createDatabase('SOF-viz-light')
    db = Connection(
        arangoURL='http://{host}:{port}'.format(
            host=app.config['ARANGO_HOST'],
            port=app.config['ARANGO_PORT']
        ),
        username=app.config['ARANGO_USERNAME'],
        password=app.config['ARANGO_PASSWORD']
    )[app.config['ARANGO_DB']]

init_db()  # Call the init_db function to initialize the db variable

insert_json_db('./app/static/data/json_files','./app/static/data/xml_files', db)
structure = None
global data_dashboard
data_dashboard = None
#data_dashboard = dashboard(db, structure)

from app.routes import doc_route, dashboard_route,reset_db, software_route, api_route, disambiguate_route, author_route

@app.route('/')
def home():
    # Read the text file
    try:
        with open('app/static/Corpus/corpus.txt', 'r', encoding='utf-8') as f:
            corpus_txt = f.read()
    except FileNotFoundError:
        corpus_txt = "File not found. Please check the file path."
    print(corpus_txt)
    data = home_data(db)
    return render_template('pages/home.html', data=data[0], corpus=corpus_txt)

