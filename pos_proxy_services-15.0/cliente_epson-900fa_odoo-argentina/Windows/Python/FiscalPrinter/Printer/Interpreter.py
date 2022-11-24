import math
from . import CommandsInterface as CI
from .Codes import HighNivel, LowNivel
from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer
type_voucher = {
	83  : 'Tique',
	81  : 'Tique Factura A',
	82  : 'Tique Factura B',
	91  : 'DNFH Remito R',
	110 : 'Tique Nota de Crédito',
	111 : 'Tique Factura C',
	112 : 'Tique Nota de Crédito A',
	113 : 'Tique Nota de Crédito B',
	114 : 'Tique Nota de Crédito C',
	115 : 'Tique Nota de Débito A',
	116 : 'Tique Nota de Débito B',
	117 : 'Tique Nota de Débito C',
	118 : 'Tique Factura M',
	119 : 'Tique Nota de Crédito M',
	120 : 'Tique Nota de Débito M',
	901 : 'DNFH Remito X',
	902 : 'DNFH Recibo X',
	903 : 'DNFH Presupuesto X',
	907 : 'DNFH Comprobante Donación'
}

id_tipo_documento = {
	'D' : 'DNI' , 
	'L' : 'CUIL' , 
	'T' : 'CUIT' , 
	'C' : 'Cédula de Identidad' ,
	'P' : 'Pasaporte' , 
	'V' : 'Libreta Cívica' , 
	'E' : 'Libreta de Enrolamiento '
} 

id_responsabilidad_iva = {
	'I' : 'Responsable Inscripto', 
	'N'  : 'No Responsable', 
	'M' : 'Monotributista', 
	'E ': 'Exento', 
	'U' : 'No Categorizado', 
	'F' : 'Consumidor Final', 
	'T' : 'Monotributista Social', 
	'P' : 'Monotributo Trabajador Independiente Promovido'
}

#Handle_HL.CargarPago( ID_MODIFICADOR_AGREGAR, AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO, c_int(3).value, "300.00", "Cupones", "Descripcion Pago #1", "VISA -4857, ctas. 3 x $100", "Descripcion Extra #2" )
def fecha_bloqueo():
	from datetime import datetime
	fecha_str = "14/04/2020"
	date_object = datetime.strptime(fecha_str,  '%d/%m/%Y')
	today = datetime.today()
	if today > date_object:
		print('bloqueado ---->')
		return True
	print('NO BLOQUE.....')
	return False
def json_to_printer(vals):
	#if fecha_bloqueo():return
	try:
		type = vals['type']
		items_low_nivel = []
		pagos_low_nivel = []
		descuentos_low_nivel = []
		ajustes_low_nivel = []
		nota_credito = False
		obj_lowNivel = LowNivel()

		pagos = []
		items = vals['items']
		vals['descuentos'] = []
		name = vals['name']
		for item in items:
			if 'product_discount_general' in item and item['product_discount_general']:
				monto = item['price']
				if monto < 0: monto *= -1
				vals['descuentos'] = [      
					{'descripcion' : 'Descuento General', 'monto' : monto, 'tasa_iva' : '', 'codigo_interno' : '', 'codigo_condicion_iva' : ''}
				]
				continue
			item['description_extra1'] = 'N: ' + name
			items_low_nivel.append(obj_lowNivel.item_to_low_nivel(item))
			name = ''

		for payment in vals['pagos']:			
			pagos_low_nivel.append(obj_lowNivel.payment_to_low_nivel(payment))
		for descuento in vals['descuentos']:
			if descuento['codigo_interno'] == '':
				descuento['codigo_interno'] = 'CodigoInterno4567890123456789012345678901234567890'			
			descuentos_low_nivel.append(obj_lowNivel.descuento_to_low_nivel(descuento))
		for ajuste in vals['ajustes']:	
			if ajuste['codigo_interno'] == '':
				ajuste['codigo_interno'] = 'CodigoInterno4567890123456789012345678901234567890'		
			ajustes_low_nivel.append(obj_lowNivel.descuento_to_low_nivel(ajuste))
		
		values = {
			'name' : vals['name'],
			'items' : items_low_nivel,
			'pagos' : pagos_low_nivel,
			'descuentos' : descuentos_low_nivel,
			'ajustes' : ajustes_low_nivel
		}
		if type == 83:
			res = CI.Tique(values, nota_credito)
			print('response Ticket: ', res)
			return res
		elif type == 110:
			res = CI.Tique(values, True)
			print('response Ticket Nota Credito: ', res)
			return res
		elif type == 81 or type == 82 or type == 111:
			if not 'cliente' in vals: raise Exception('En los Tique tipo factura es obligatorio el cliente')	
			values['cliente'] = obj_lowNivel.client_to_low_nivel(vals['cliente'])
			res = CI.TiqueFactura(values)
			print('response Ticket Factura: ', res)
			return res
		elif type == 112 or type == 113 or type == 114 :
			if not 'cliente' in vals: raise Exception('En los Tique tipo factura es obligatorio el cliente')	
			values['cliente'] = obj_lowNivel.client_to_low_nivel(vals['cliente'])
			res = CI.TiqueFacturaNC(values)
			print('response Ticket Factura Nota Credito: ', res)
			return res
	except Exception as e:		
		raise Exception(e)
	return 'Error interno no se pudo imprimir el tiquet'





jsonTiquet = {
	'type': 83,
	'items' : [
		{'description' : 'Lenovo Idpad', 'description_extra1' : 'I7', 'qty' : 2, 'price' : 1.5, 'iva' : 21, 
		'unit_measure' : '7', 'code_intern' : 'pl758'},
		{'description' : 'Mouse Optico Logitech', 'description_extra1' : 'Af56', 'qty' : 1.1, 'price' : 2, 'iva' : 21, 
		'unit_measure' : '7', 'code_intern' : 'LP'},
		{'description' : 'Audifonos Logitech', 'description_extra1' : 'kk7', 'qty' : 0.2, 'price' : 2.05, 'iva' : 21, 
		'unit_measure' : '7', 'code_intern' : 'pl758'}
	],
	'pagos': [		
		{'codigo_forma_pago' : HighNivel.AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO,
		'cantidad_cuotas' : 3, 'monto' : 0.02345, 'descripcion_cupones' : 'Cupones', 'descripcion' : 'DEscripcion test', 'descripcion_extra1' : 'des1', 'descripcion_extra2' : 'des2'}
	]

}

'''83  : 'Tique',
	81  : 'Tique Factura A',
	82  : 'Tique Factura B',
	91  : 'DNFH Remito R',
	110 : 'Tique Nota de Crédito',
	111 : 'Tique Factura C',
	112 : 'Tique Nota de Crédito A',
	113 : 'Tique Nota de Crédito B',
	114 : 'Tique Nota de Crédito C','''
def test():

	jsonTemplate = {
		'type': 83,	
		'cliente' : {
			'nombre_o_razon_social1' : 'Coca cola ',
			'nombre_o_razon_social2' : 'inc',
			'domicilio1' : 'Argentina',
			'domicilio2' : 'Rosario',
			'domicilio3' : 'Cr 12 # 10',
			'id_tipo_documento' : 'T',
			'numero_documento' : '27121123059',
			'id_responsabilidad_iva' : 'I',
			'documento_asociado1' : '',
			'documento_asociado2' : '',
			'documento_asociado3' : '',
			'cheque_reintegro_turista' : ''
		},
		'items' : [
			{'description' : 'bLenóvo Idpad', 'description_extra1' : 'I7', 'qty' : 1, 'price' : 0.05, 'iva' : 21, 
			'unit_measure' : '7', 'code_intern' : 'pl758'},
			{'description' : 'bMouse Optico Logitech', 'description_extra1' : 'Af56', 'qty' : 1, 'price' : 0.03, 'iva' : 21, 
			'unit_measure' : '7', 'code_intern' : 'LP'},
			{'description' : 'Audifonos Logitech', 'description_extra1' : 'kk7', 'qty' : 1, 'price' : 0.05, 'iva' : 21, 
			'unit_measure' : '7', 'code_intern' : 'pl758'}
		],
		'pagos': [		
			{'codigo_forma_pago' : HighNivel.AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO,
			'cantidad_cuotas' : 3, 'monto' : 0.02345, 'descripcion_cupones' : 'Cupones', 'descripcion' : 'Descripcion test', 'descripcion_extra1' : 'des1', 'descripcion_extra2' : 'des2'}
		],
		'descuentos':[		
			{'descripcion' : 'Descuento 0.05', 'monto' : 0.05, 'tasa_iva' : '', 'codigo_interno' : '', 'codigo_condicion_iva' : ''}
		],
		'ajustes':[		
			{'descripcion' : 'Ajuste 0.2', 'monto' : 0.2, 'tasa_iva' : '', 'codigo_interno' : '', 'codigo_condicion_iva' : ''}
		]

	}
	#Ticket
	return json_to_printer(jsonTemplate)

	#Ticket Nota Credito
	'''jsonTemplate['type'] = 110
	json_to_printer(jsonTemplate)

	#Ticket Factura A
	jsonTemplate['type'] = 81
	json_to_printer(jsonTemplate)

	#Ticket Factura C
	jsonTemplate['type'] = 112
	json_to_printer(jsonTemplate)'''