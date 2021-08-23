from flask import Flask, render_template
from flask import *
from flask import request, abort, jsonify, url_for
from habidb import look_for_property_db

estados = ('pre_venta', 'en_venta', 'vendido')
app = Flask(__name__)


@app.route('/api/consulta')
def look_for_property():
    req = request.get_json()
    estado = ''
    res = {"OK": "Estado válido"}
    estado = req['state']
    building_date = req['building_date']
    city = req['city']
    if estado not in estados:
        return make_response({"Error": "Estado inválido"}, 400)
    res = look_for_property_db(estado, building_date, city)
    return make_response(jsonify(res), 200)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
