


from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer


def string_to_ascci(val): 
	
	a,b = 'áéíóúüñÁÉÍÓÚÜÑ','aeiouunAEIOUUN'
	trans = str.maketrans(a,b)
	val = val.translate(trans)
	return val



class HighNivel:
	#EpsonLibInterface = cdll.LoadLibrary() # Linux Caraga de libreria

	# -----------------------------------------------------------------------------
	# GLOBAL DEFINES AREA
	# -----------------------------------------------------------------------------
	ID_TIPO_COMPROBANTE_TIQUET                = c_int( 1 ).value  # "83"  Tique
	ID_TIPO_COMPROBANTE_TIQUE_FACTURA         = c_int( 2 ).value  # "81"  Tique Factura A, "82" Tique Factura B, "111" Tique Factura C, "118" Tique Factura M
	ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO = c_int( 3 ).value  # "110" Tique Nota de Credito, "112" Tique Nota de Credito A, "113" Tique Nota de Credito B, "114" Tique Nota de Credito C, "119" Tique Nota de Credito M
	ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_DEBITO  = c_int( 4 ).value  # "115" Tique Nota de Debito A, "116" Tique Nota de Debito B, "117" Tique Nota de Debito C, "120" Tique Nota de Debito M

	ID_TIPO_DOCUMENTO_NINGUNO           = c_int( 0 ).value
	ID_TIPO_DOCUMENTO_DNI               = c_int( 1 ).value
	ID_TIPO_DOCUMENTO_CUIL              = c_int( 2 ).value
	ID_TIPO_DOCUMENTO_CUIT              = c_int( 3 ).value
	ID_TIPO_DOCUMENTO_CEDULA_IDENTIDAD  = c_int( 4 ).value
	ID_TIPO_DOCUMENTO_PASAPORTE         = c_int( 5 ).value
	ID_TIPO_DOCUMENTO_LIB_CIVICA        = c_int( 6 ).value
	ID_TIPO_DOCUMENTO_LIB_ENROLAMIENTO  = c_int( 7 ).value

	ID_RESPONSABILIDAD_IVA_NINGUNO                              = c_int(  0 ).value
	ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO                = c_int(  1 ).value
	ID_RESPONSABILIDAD_IVA_NO_RESPONSABLE                       = c_int(  3 ).value
	ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA                       = c_int(  4 ).value
	ID_RESPONSABILIDAD_IVA_CONSUMIDOR_FINAL                     = c_int(  5 ).value
	ID_RESPONSABILIDAD_IVA_EXENTO                               = c_int(  6 ).value
	ID_RESPONSABILIDAD_IVA_NO_CATEGORIZADO                      = c_int(  7 ).value
	ID_RESPONSABILIDAD_IVA_MONOTRIBUTISTA_SOCIAL                = c_int(  8 ).value
	ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL               = c_int(  9 ).value
	ID_RESPONSABILIDAD_IVA_CONTRIBUYENTE_EVENTUAL_SOCIAL        = c_int( 10 ).value
	ID_RESPONSABILIDAD_IVA_MONOTRIBUTO_INDEPENDIENTE_PROMOVIDO  = c_int( 11 ).value

	ID_MODIFICADOR_AGREGAR_ITEM                     = c_int( 200 ).value
	ID_MODIFICADOR_ANULAR_ITEM                      = c_int( 201 ).value
	ID_MODIFICADOR_AGREGAR_ITEM_RETORNO_ENVASES     = c_int( 202 ).value
	ID_MODIFICADOR_ANULAR_ITEM_RETORNO_ENVASES      = c_int( 203 ).value
	ID_MODIFICADOR_AGREGAR_ITEM_BONIFICACION        = c_int( 204 ).value
	ID_MODIFICADOR_ANULAR_ITEM_BONIFICACION         = c_int( 205 ).value
	ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO           = c_int( 206 ).value
	ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO            = c_int( 207 ).value
	ID_MODIFICADOR_AGREGAR_ITEM_ANTICIPO            = c_int( 208 ).value
	ID_MODIFICADOR_ANULAR_ITEM_ANTICIPO             = c_int( 209 ).value
	ID_MODIFICADOR_AGREGAR_ITEM_DESCUENTO_ANTICIPO  = c_int( 210 ).value
	ID_MODIFICADOR_ANULAR_ITEM_DESCUENTO_ANTICIPO   = c_int( 211 ).value
	ID_MODIFICADOR_DESCUENTO                        = c_int( 400 ).value
	ID_MODIFICADOR_AJUSTE                           = c_int( 401 ).value
	ID_MODIFICADOR_AJUSTE_NEGATIVO                  = c_int( 402 ).value
	ID_MODIFICADOR_AUDITORIA_DETALLADA              = c_int( 500 ).value
	ID_MODIFICADOR_AUDITORIA_RESUMIDA               = c_int( 501 ).value

	ID_MODIFICADOR_AGREGAR                          = ID_MODIFICADOR_AGREGAR_ITEM
	ID_MODIFICADOR_ANULAR                           = ID_MODIFICADOR_ANULAR_ITEM

	ID_TASA_IVA_NINGUNO = c_int( 0 ).value
	ID_TASA_IVA_EXENTO  = c_int( 1 ).value
	ID_TASA_IVA_10_50   = c_int( 4 ).value
	ID_TASA_IVA_21_00   = c_int( 5 ).value
	ID_TASA_IVA_27_00   = c_int( 6 ).value

	ID_IMPUESTO_NINGUNO            = c_int( 0 ).value
	ID_IMPUESTO_INTERNO_FIJO       = c_int( 1 ).value
	ID_IMPUESTO_INTERNO_PORCENTUAL = c_int( 2 ).value

	ID_CODIGO_INTERNO = c_int( 1 ).value
	ID_CODIGO_MATRIX  = c_int( 2 ).value

	AFIP_CODIGO_UNIDAD_MEDIDA_SIN_DESCRIPCION            = c_int(  0 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO                  = c_int(  1 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_METROS                     = c_int(  2 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUADRADO             = c_int(  3 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_METRO_CUBICO               = c_int(  4 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_LITROS                     = c_int(  5 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD                     = c_int(  7 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_PAR                        = c_int(  8 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_DOCENA                     = c_int(  9 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_QUILATE                    = c_int( 10 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILLAR                     = c_int( 11 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_ANTIB     = c_int( 12 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD_INT_ACT_INMUNG      = c_int( 13 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO                      = c_int( 14 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO                  = c_int( 15 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILIMETRO_CUBICO           = c_int( 16 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO                  = c_int( 17 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_HECTOLITRO                 = c_int( 18 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_UNIDAD_INT_ACT_INMUNG = c_int( 19 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO                 = c_int( 20 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_ACTIVO           = c_int( 21 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_ACTIVO               = c_int( 22 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_GRAMO_BASE                 = c_int( 23 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_UIACTHOR                   = c_int( 24 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_JGO_PQT_MAZO_NAIPES        = c_int( 25 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTHOR                  = c_int( 26 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_CENTIMETRO_CUBICO          = c_int( 27 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_UIACTANT                   = c_int( 28 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_TONELADA                   = c_int( 29 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_DECAMETRO_CUBICO           = c_int( 30 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_HECTOMETRO_CUBICO          = c_int( 31 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOMETRO_CUBICO           = c_int( 32 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MICROGRAMO                 = c_int( 33 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_NANOGRAMO                  = c_int( 34 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_PICOGRAMO                  = c_int( 35 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTANT                  = c_int( 36 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_UIACTIG                    = c_int( 37 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILIGRAMO                  = c_int( 41 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILILITRO                  = c_int( 47 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_CURIE                      = c_int( 48 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MILICURIE                  = c_int( 49 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MICROCURIE                 = c_int( 50 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_U_INTER_ACT_HORMONAL       = c_int( 51 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MEGA_U_INTER_ACT_HORMONAL  = c_int( 52 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BASE             = c_int( 53 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_GRUESA                     = c_int( 54 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_MUIACTIG                   = c_int( 55 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_KILOGRAMO_BRUTO            = c_int( 61 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_PACK                       = c_int( 62 ).value
	AFIP_CODIGO_UNIDAD_MEDIDA_HORMA                      = c_int( 63 ).value

	AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_NACIONALES                 = c_int(  1 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTOS_PROVINCIAL                 = c_int(  2 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_MUNICIPAL                   = c_int(  3 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_IMPUESTO_INTERNOS                    = c_int(  4 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_INGRESOS_BRUTOS                      = c_int(  5 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_IVA                    = c_int(  6 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_DE_INGRESOS_BRUTOS        = c_int(  7 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_PERCEPCION_POR_IMPUESTOS_MUNICIPALES = c_int(  8 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_OTRAS_PERCEPCIONES                   = c_int(  9 ).value
	AFIP_CODIGO_OTROS_TRIBUTOS_OTROS                                = c_int( 99 ).value

	#Formas de pago
	AFIP_CODIGO_FORMA_DE_PAGO_CARTA_DE_CREDITO_DOCUMENTARIO       = c_int(  1 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_CARTAS_DE_CREDITO_SIMPLE            = c_int(  2 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_CHEQUE                              = c_int(  3 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_CHEQUES_CANCELATORIOS               = c_int(  4 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_CREDITO_DOCUMENTARIO                = c_int(  5 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_CUENTA_CORRIENTE                    = c_int(  6 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_DEPOSITO                            = c_int(  7 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_EFECTIVO                            = c_int(  8 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_ENDOSO_DE_CHEQUE                    = c_int(  9 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_FACTURA_DE_CREDITO                  = c_int( 10 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_GARANTIAS_BANCARIAS                 = c_int( 11 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_GIROS                               = c_int( 12 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_LETRAS_DE_CAMBIO                    = c_int( 13 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_MEDIOS_DE_PAGO_DE_COMERCIO_EXTERIOR = c_int( 14 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_DOCUMENTARIA          = c_int( 15 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_ORDEN_DE_PAGO_SIMPLE                = c_int( 16 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_PAGO_CONTRA_REEMBOLSO               = c_int( 17 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_REMESA_DOCUMENTARIA                 = c_int( 18 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_REMESA_SIMPLE                       = c_int( 19 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_CREDITO                  = c_int( 20 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_TARJETA_DE_DEBITO                   = c_int( 21 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_TICKET                              = c_int( 22 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_BANCARIA              = c_int( 23 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_TRANSFERENCIA_NO_BANCARIA           = c_int( 24 ).value
	AFIP_CODIGO_FORMA_DE_PAGO_OTROS_MEDIOS_DE_PAGO                = c_int( 99 ).value


class LowNivel:
	
	GET_FIRMWARE_VERSION    = "020A|0000"    
	NUM_CAMPO_VERSION       = 1
	NUM_CAMPO_VERSION_MAYOR = 3
	NUM_CAMPO_VERSION_MENOR = 4

	X_REPORT                = "0802|0C01"
	Z_REPORT                = "0801|0000"

	TICKET_OPEN             = "0A01|0080"
	TICKET_ITEM             = "0A02|0000"
	TICKET_DISCOUNT    		= '0A04|0000'
	TICKET_ADJUSTMENT  		= '0A04|0001'
	TICKET_PAYMENT          = "0A05|0000"
	TICKET_CLOSE            = "0A06|0013"

	TICKET_OPEN_FACTURA		= "0B01|0000" 
	TICKET_ITEM_FACTURA 	= '0B02|0000'
	TICKET_PAYMENT_FACTURA 	= '0B05|0000'
	TICKET_DISCOUNT_FACTURA	= '0B04|0000'
	TICKET_ADJUSTMENT_FACTURA = '0B04|0001'

	TICKET_NC_OPEN_FACTURA  = "0D01|0000"
	TICKET_NC_ITEM_FACTURA 	= '0D02|0000'
	TICKET_NC_PAYMENT_FACTURA 	= '0D05|0000'
	TICKET_NC_DISCOUNT_FACTURA	= '0D04|0000'
	TICKET_NC_ADJUSTMENT_FACTURA = '0D04|0001'


	TICKET_NC_OPEN          = "0A01|4000"
	TICKET_NC_ITEM          = "0A02|0000"
	TICKET_NC_PAYMENT       = "0A05|0000"
	TICKET_NC_CLOSE         = "0A06|0013"

	DNF_OPEN                = "0E01|0000"
	DNF_ITEM                = "0E02|0000"
	DNF_CLOSE               = "0E06|0001"

	# Datos variables de los campos suministrados por el software POS (fijos en este ejemplo solo para efectos demostrativos)
	TICKET_ITEM_FIELDS      = "|Linea 1 de descripcion |Linea 2 de descripcion |Linea 3 de descripcion |Linea 4 de descripcion |Descripcion ITEM|10000|20000|2100|||||1234567890|1|7"
	TICKET_PAYMENT_FIELDS   = "|Pago extra #1|Pago extra #2|10|Otra forma de pago|Detalle de cupones|06|1000"
	TICKET_CLOSE_FIELDS     = "|||||||"  # 7 campos

	TICKET_NC_OPEN_FIELDS     = ""
	TICKET_NC_ITEM_FIELDS     = "|Linea 1 de descripcion |Linea 2 de descripcion |Linea 3 de descripcion |Linea 4 de descripcion |Descripcion ITEM|10000|120000|2100|||||1234567890|1|7"
	TICKET_NC_PAYMENT_FIELDS  = "|Pago extra #1|Pago extra #2|10|Otra forma de pago|Detalle de cupones|06|1000"
	TICKET_NC_CLOSE_FIELDS    = "|||||||"  # 7 campos

	DNF_ITEM_FIELDS         = "|Texto a imprimir"
	DNF_CLOSE_FIELDS        = "||||||"    # 6 campos


	def descuento_to_low_nivel(self, descuento):

		descripcion = '|' + descuento['descripcion']
		monto = '|' +self. monto_descuento_format(descuento['monto'])
		tasa_iva = '|' + str(descuento['tasa_iva'])
		codigo_interno = '|' + descuento['codigo_interno']
		codigo_condicion_iva = '|' + str(descuento['codigo_condicion_iva'])

		values = descripcion + monto + tasa_iva + codigo_interno + codigo_condicion_iva
		values = string_to_ascci(values)
		return values

	def client_to_low_nivel(self, cliente):
		TICKET_FACTURA = "0B01|0000"
		TICKET_NC_OPEN_FIELDS = "|Nombre Comprador '1|Nombre Comprador '2|Domicilio Comprador '1|||T|30614104712|I||||"
		
		nombre_o_razon_social1 = '|' + cliente['nombre_o_razon_social1']
		nombre_o_razon_social2 = '|' + cliente['nombre_o_razon_social2']
		domicilio1 = '|' + cliente['domicilio1']
		domicilio2 = '|' + cliente['domicilio2']
		domicilio3 = '|' + cliente['domicilio3']
		id_tipo_documento = '|' + cliente['id_tipo_documento']
		numero_documento = '|' + cliente['numero_documento']
		id_responsabilidad_iva = '|' + cliente['id_responsabilidad_iva']
		documento_asociado1 = '|' + cliente['documento_asociado1']
		documento_asociado2 = '|' + cliente['documento_asociado2']
		documento_asociado3 = '|' + cliente['documento_asociado3']
		cheque_reintegro_turista = '|' + cliente['cheque_reintegro_turista']


		values = nombre_o_razon_social1 + nombre_o_razon_social2 + domicilio1 + domicilio2 + domicilio3 + id_tipo_documento + numero_documento + id_responsabilidad_iva + documento_asociado1 + documento_asociado2 + documento_asociado3 + cheque_reintegro_turista
		values = string_to_ascci(values)
		
		return values
	def payment_to_low_nivel(self, payment):
		#TICKET_PAYMENT_FIELDS   = "|Pago extra #1|Pago extra #2|10|Otra forma de pago|Detalle de cupones|06|1000"
		try:
			
			payment['monto'] = str(self.monto_format(payment['monto']))			
			payment['cantidad_cuotas'] = str(payment['cantidad_cuotas'])

			descripcion_extra1 = '|' + payment['descripcion_extra1']
			descripcion_extra2 = '|' + payment['descripcion_extra2']
			cantidad_cuotas = '|' + payment['cantidad_cuotas']
			descripcion = '|' + payment['descripcion']
			descripcion_cupones = '|' + payment['descripcion_cupones']
			codigo_forma_pago = '|' + str(payment['codigo_forma_pago'])
			monto = '|' + payment['monto']

			values = descripcion_extra1 + descripcion_extra2 + cantidad_cuotas + descripcion + descripcion_cupones + codigo_forma_pago + monto
			#print('values payment= ', values)
			values = string_to_ascci(values)
			return values


			
		except Exception as e:
			raise Exception(e)
	def item_to_low_nivel(self, item):
		try:
			description = '|' + item['description']
			description_extra1 = description_extra2 = description_extra3 = description_extra4 = ''
			if 'description_extra1' in item:
				description_extra1 = item['description_extra1']
			if 'description_extra2' in item:
				description_extra2 = item['description_extra2']
			if 'description_extra3' in item:
				description_extra3 = item['description_extra3']
			if 'description_extra4' in item:
				description_extra4 = item['description_extra4']
			price = '|' + self.price_format(item['price'])
			
			qty = '|' + self.qty_format(item['qty'])
			iva = '|' + self.iva_format(item['iva'])

			code_intern = ''
			if 'code_intern' in item: code_intern = item['code_intern']
			code_intern = '|' + code_intern
			unit_measure = '7'
			if 'unit_measure' in item: unit_measure = item['unit_measure']
			unit_measure = '|' + unit_measure
			description_extra1 = '|' + description_extra1
			description_extra2 = '|' + description_extra2
			description_extra3 = '|' + description_extra3
			description_extra4 = '|' + description_extra4

			other_fields = '||||'
			values = description_extra1 + description_extra2 + description_extra3 + description_extra4 + description + qty + price + iva + other_fields + code_intern + unit_measure + '|'
			values = string_to_ascci(values)
			print('values: ', values)
			return values

		except Exception as e:
			raise Exception(e)

	def monto_descuento_format(self, monto):
		str_monto = str(monto)
		str_integer = ''
		str_decimal = ''
		index_point = str_monto.find('.')
		if index_point > -1:
			str_decimal = str_monto[index_point + 1:len(str_monto)]
			str_integer = str_monto[0:index_point]
			
		else:
			str_integer = str_monto

		if len(str_integer) > 10:
			raise Exception('Valor entero del monto del pago no debe ser mayor de 10')
		if len(str_decimal) > 2:
			str_decimal = str_decimal[0:2]
		elif len(str_decimal) == 0: str_decimal = '00'
		elif len(str_decimal) < 2:
			while len(str_decimal) < 2:
				str_decimal += '0'
		#print('entero: ', str_integer, '- str_decimal: ', str_decimal)
		return str_integer + str_decimal
		


	def monto_format(self, monto):
		str_monto = str(monto)
		str_integer = ''
		str_decimal = ''
		index_point = str_monto.find('.')
		if index_point > -1:
			str_decimal = str_monto[index_point + 1:len(str_monto)]
			str_integer = str_monto[0:index_point]
			
		else:
			str_integer = str_monto

		if len(str_integer) > 9:
			raise Exception('Valor entero del monto del pago no debe ser mayor de 9')
		if len(str_decimal) > 2:
			str_decimal = str_decimal[0:2]
		elif len(str_decimal) == 0: str_decimal = '00'
		elif len(str_decimal) < 2:
			while len(str_decimal) < 2:
				str_decimal += '0'
		#print('entero: ', str_integer, '- str_decimal: ', str_decimal)
		return str_integer + str_decimal
	def qty_format(self, qty):
		str_qty = str(qty)
		str_integer = ''
		str_decimal = ''
		index_point = str_qty.find('.')
		if index_point > -1:
			str_decimal = str_qty[index_point + 1:len(str_qty)]
			str_integer = str_qty[0:index_point]
			
		else:
			str_integer = str_qty

		if len(str_integer) > 5:
			raise Exception('Valor entero de la cantidad no debe ser mayor de 5')
		if len(str_decimal) > 4:
			str_decimal = str_decimal[0:4]
		elif len(str_decimal) == 0: str_decimal = '0000'
		elif len(str_decimal) < 4:
			while len(str_decimal) < 4:
				str_decimal += '0'
		#print('entero: ', str_integer, '- str_decimal: ', str_decimal)
		return str_integer + str_decimal
	def price_format(self, price):
		str_price = str(price)
		str_integer = ''
		str_decimal = ''
		index_point = str_price.find('.')
		if index_point > -1:
			str_decimal = str_price[index_point + 1:len(str_price)]
			str_integer = str_price[0:index_point]
			
		else:
			str_integer = str_price

		if len(str_integer) > 7:
			raise Exception('Valor entero del precio no debe ser mayor de 7')
		if len(str_decimal) > 4:
			str_decimal = str_decimal[0:4]
		elif len(str_decimal) == 0: str_decimal = '0000'
		elif len(str_decimal) < 4:
			while len(str_decimal) < 4:
				str_decimal += '0'
		#print('entero: ', str_integer, '- str_decimal: ', str_decimal)
		return str_integer + str_decimal

	def iva_format(self, iva):
		str_iva = str(iva)
		str_integer = ''
		str_decimal = ''
		index_point = str_iva.find('.')
		if index_point > -1:
			str_decimal = str_iva[index_point + 1:len(str_iva)]
			str_integer = str_iva[0:index_point]
			
		else:
			str_integer = str_iva

		if len(str_integer) > 2:
			raise Exception('Valor entero del iva no debe ser mayor de 2')
		if len(str_decimal) > 2:
			str_decimal = str_decimal[0:2]
		elif len(str_decimal) == 0: str_decimal = '00'
		elif len(str_decimal) < 2:
			while len(str_decimal) < 2:
				str_decimal += '0'
		#print('entero: ', str_integer, '- str_decimal: ', str_decimal)
		return str_integer + str_decimal
