from flask import render_template, make_response, jsonify, send_file
from app import app
from io import BytesIO
from app import graphs
import plotly
import json


@app.errorhandler(400)
def custom400(error):
    return make_response(jsonify({"message": error.description}), 400)


@app.errorhandler(404)
def custom404(error):
    return make_response(jsonify({"message": "not found" + error.description}), 404)


@app.route('/')
@app.route('/index')
def index():
    ids = ["graph-0", "graph-1"]


    graphJSON = json.dumps([graphs.make_figure()], cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("index.html", title="colorado covid data", ids=ids, graphJSON=graphJSON)


@app.route('/colorado-log-graph')
def get_co_graph():
    fig = graphs.make_figure()
    img = BytesIO()
    fig.savefig(img, format="png")
    img.seek(0)

    return send_file(img, mimetype="image/png")
