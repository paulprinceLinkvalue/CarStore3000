from flask import Flask, render_template, request
import init_db

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Bienvenue'


@app.route('/whoareyou')
def index():
    # return "<p>Tout fonctionne parfaitement</p>"

    return render_template('index.html')

@app.route('/resultat',methods = ['POST'])
def resultat():
  result = request.form
  n = result['nom']
  p = result['prenom']
  return render_template("resultat.html", nom=n, prenom=p)

@app.route('/init')
def init():
    return init_db.load_data()