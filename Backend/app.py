import json
from Generator.Generator import Generator
from flask import Flask, jsonify, request
from flask.json import tag
from flask_cors import CORS
from Entorno.Entorno import Environment
from __parser__ import parser

import sys
sys.setrecursionlimit(10000)
app = Flask(__name__)
CORS(app)

@app.route('/code', methods=["POST"])
def analizarCode():
    #tablaSimbolos.clear()
    global inp
    code = request.json["codigo"]
    inp  = code
    copilado = parser.parse(code)
    
    #tree = arbol.parse(code)
    generator: Generator = Generator()
    globalEntorno = Environment(None,"global")
    for ins in copilado:
        ins.generator = generator
        ins.compile(globalEntorno)

    
    #codigoInterpretado.clear()
    f = open("./salida.txt", "w")   
    
    return jsonify({"codigo": generator.getCode(),"tree":"","tablaSimbolos":"","errores":""})

@app.route('/tSimbolos')
def returnTablaSimbolos():
    return jsonify({})

@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"
if __name__ == '__main__':
    app.run(debug=True, port=4000)
