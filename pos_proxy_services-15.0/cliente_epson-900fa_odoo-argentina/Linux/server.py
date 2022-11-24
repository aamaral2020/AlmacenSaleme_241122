#!/usr/bin/python3
from flask import Flask, request

import json
from flask_cors import CORS, cross_origin
from flask_jsonpify import jsonify
app = Flask(__name__)
CORS(app)



	#print(message.sid)
def response_cors(res):
	res = {'response' : res}
	response = jsonify(res)
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response	


@app.route("/print_pos_ticket", methods=['GET','OPTIONS'])
def print_pos_ticket():
	from Printer import Interpreter

	if not 'vals' in request.args:
		return response_cors('Debe enviar los valores del tiquet')
	vals = request.args['vals']
	if isinstance(vals, dict):
		json_vals = vals
	elif isinstance(vals, str):
		try:		
			json_vals = json.loads(vals)			
		except Exception as e:
			return str(e)
	else:
		return 'Formato de los valores incorrecto'
	
	response_printer = Interpreter.json_to_printer(json_vals)	
	print('print_pos_ticket response_printer: ', response_printer)
	return response_cors(response_printer)
	
@app.route("/print_pos_fiscal_close", methods=['GET','OPTIONS'])
def print_pos_fiscal_close():
	print('print_pos_fiscal_close: ', request.args)
	if not 'type' in request.args:
		return response_cors('Debe enviar el tipo de cierre fiscal')
	type = request.args['type']
	from Printer import CommandsInterface
	response_printer = CommandsInterface.ImprimirCierre(type)
	print('print_pos_fiscal_close response_printer: ', response_printer)
	return response_cors(response_printer)

@app.route("/state_printer", methods=['GET','OPTIONS'])
def state_printer():	
	from Printer import CommandsInterface
	response_state = CommandsInterface.EstadoEstacionRecibos()	
	return response_cors(response_state)

	
#from Printer import InterpreterO
#InterpreterO.test()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5005)

