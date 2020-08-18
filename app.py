from flask import Flask, render_template, request
import sqlite3
import init_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resultat', methods=['POST'])
def resultat():
    result = request.form
    prenom = result['prenom']
    age = result['age']
    gender = result['gender']
    with_child = result['with_child']
    place_of_residence = result['place_of_residence']
    budget = result['budget']
    default_budget = 15000

    if budget:
        where_query = ' Where price_eur < ' + budget
    else:
        where_query = ' Where price_eur < ' + budget

    if with_child == "oui":
        where_query += ' And body_type = \'van\''
    else:
        where_query += ' And body_type = \'compact\''

    sql_query = 'SELECT * FROM Cars ' + where_query + ' Limit 10'

    conn = get_db_connection()
    posts = conn.execute(sql_query).fetchall()
    conn.close()

    return render_template("resultat.html", posts=posts, prenom=prenom)


@app.route('/init')
def init():
    return init_db.load_data()


def get_db_connection():
    conn = sqlite3.connect('CarStore3000.db')
    conn.row_factory = sqlite3.Row
    return conn