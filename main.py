
import pymongo
import certifi

from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

from Controladores.PartidoControlador import PartidoControlador



app = Flask(__name__)
cors = CORS(app)





########################
###CARGAR EL ARCHIVO DE CONFIGURACION
########################
def loadConfigFile():
    with open('config.json') as file:
        data = json.load(file)
    return data



###############
#   VARIABLES GLOBALES
###############
miControladorPartido = PartidoControlador()






######################
# probar el servicio
#############################

@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Server running..."
    return jsonify(json)


##################
##   ENDPOINT PARTIDO
##################

@app.route("/partidos", methods=["GET"])
def getPartidos():
    json = miControladorPartido.index()
    return jsonify(json)


@app.route("/partidos", methods=["POST"])
def crearPartido():
    data = request.get_json()
    json = miControladorPartido.create(data)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=["GET"])
def getPartido(id):
    json = miControladorPartido.show(id)
    return jsonify(json)


@app.route("/partidos/<string:id>", methods=["PUT"])
def modificarPartido(id):
    data = request.get_json()
    json = miControladorPartido.update(id, data)
    return jsonify(json)


@app.route("/partidos/<string:id", methods=["DELETE"])
def deletePartido(id):
    json = miControladorPartido.delete(id)
    return jsonify(json)


if __name__ == "__main__":
    app.run(debug=False, port=9999)




def dbConnection():
    configData = loadConfigFile()
    try:
        client = pymongo.MongoClient(
            "mongodb+srv://user-back-votaciones:123@cluster0.eth6r2c.mongodb.net/?retryWrites=true&w=majority",
            tlsCAFile=ca)
        db = client["db-registro-votaciones"]

    except:
        print("Error de conexion en DB")
    return db


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    configData = loadConfigFile()
    print('Servidor ejecutandose .... en http://' + configData["url-backend"] + ":" + str(configData['port']))
    serve(app, host=configData["url-backend"], port=configData["port"])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
