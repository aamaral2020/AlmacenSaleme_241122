from . import DriverFiscal as DF
from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer
from .Codes import HighNivel, LowNivel
from . import Codes
def Conectar():
  Handle = DF.get_driver()
  Handle.ConfigurarVelocidad( c_int(9600).value )
  Handle.ConfigurarPuerto( "0" )
 
  res = Handle.Conectar()
  ConsultarDescripcionDeError(res, 'Coneccion Existosa')
 
  return Handle


def Desconectar():
  Handle = DF.get_driver()
  res = Handle.Desconectar()
  ConsultarDescripcionDeError(res, 'Desconectada')
 

def Cancelar(Handle=None):
	if not Handle:
		Handle = Conectar()	
	res = Handle.Cancelar()	
	try:
		ConsultarDescripcionDeError(res, 'Documentos Cancelados')
	except Exception as e:
		pass
	
	
def ConsultarEstado(Handle, id_consulta):
	
	str_doc_response_max_len = 200
	str_doc_response = create_string_buffer( b'\000' * str_doc_response_max_len )		
	res = Handle.ConsultarEstado(id_consulta, str_doc_response)
	ConsultarDescripcionDeError(res, 'Consulta de Estado')
	return res

def ConsultarDescripcionDeError(response, msj):
	Handle = DF.get_driver()
	if response == 0:
		return True	
	else:
		str_doc_response_max_len = 200
		str_doc_response = create_string_buffer( b'\000' * str_doc_response_max_len )		
		Handle.ConsultarDescripcionDeError(response, str_doc_response, str_doc_response_max_len)
		value_decode = str_doc_response.value.decode('latin1')
		#print('ConsultarDescripcionDeError: ', value_decode)
		raise Exception(value_decode)

def AbrirComprobante(Handle, ID_TIPO_COMPROBANTE_TIQUET):	
	res = Handle.AbrirComprobante(ID_TIPO_COMPROBANTE_TIQUET)
	
	if res == 2050:
		ImprimirCierreZ(Handle)
		res = Handle.AbrirComprobante(ID_TIPO_COMPROBANTE_TIQUET)
		ConsultarDescripcionDeError(res, 'Comprobante Abierto')
	else:	
		ConsultarDescripcionDeError(res, 'Comprobante Abierto')
		
	
def ImprimirItem(Handle):
	return #Este metodo no funciona correctamente en Python
	
	res = Handle.ImprimirItem(HighNivel.ID_MODIFICADOR_AGREGAR, "Pizza", "10.000", "0.3000", 
		HighNivel.ID_TASA_IVA_21_00, HighNivel.ID_IMPUESTO_NINGUNO, "", HighNivel.ID_CODIGO_INTERNO, "1234567890", "",
		HighNivel.AFIP_CODIGO_UNIDAD_MEDIDA_UNIDAD)
	ConsultarDescripcionDeError(res, 'Item Impreso')


def CerrarComprobante(Handle):
	res = Handle.CerrarComprobante()
	ConsultarDescripcionDeError(res, 'Comprobante Cerrado')

def CargarTextoExtra(Handle, texto):
	res = Handle.CargarTextoExtra(texto)
	ConsultarDescripcionDeError(res, 'Texto Extra Impreso')
def EnviarComando(Handle, cmd):	
	n_cmd = cmd.encode('ASCII')
	res = Handle.EnviarComando(n_cmd)
	if res == 2050:
		ImprimirCierreZ(Handle)
		res = Handle.EnviarComando(n_cmd)
		ConsultarDescripcionDeError(res, 'Comando Exitoso')
	else:	
		ConsultarDescripcionDeError(res, 'Comando Exitoso')
	

def ImprimirCierreZ(Handle):
	#res = Handle.EnviarComando("0801|0C00")
	res = Handle.ImprimirCierreZ()
	ConsultarDescripcionDeError(res, 'Cierrre Z Impreso')
def ImprimirCierreX(Handle):
	#res = Handle.EnviarComando("0802|0C00")
	res =  Handle.ImprimirCierreX()
	print('ImprimirCierreX: ', res)
	#res = Handle.ImprimirCierreZ()
	ConsultarDescripcionDeError(res, 'Cierrre X Impreso')
def ObtenerRespuestaExtendida(Handle, numero_campo):
	largo_buffer_salida  = 200
	buffer_salida = create_string_buffer( b'\000' * 100)
	largo_final_buffer_salida = c_int()  
	res = Handle.ObtenerRespuestaExtendida(numero_campo, buffer_salida, largo_buffer_salida, byref(largo_final_buffer_salida)) 
	ConsultarDescripcionDeError(res, 'ObtenerRespuestaExtendida Ok')
	val = buffer_salida.value
	n_val = val.decode('latin-1')
	print('ObtenerRespuestaExtendida: ', n_val)

def EstadoPapel():
	try:
		Desconectar()
		Handle =  Conectar()
		ObtenerRespuestaExtendida(Handle, 7001)
		Desconectar()	
	except Exception as e:
		if len(e.args) > 0:	
			return e.args[0].decode()
		else: return 'Error Inesperado'
def CargarDescuento(Handle, vals=None):
	res = Handle.CargarAjuste( HighNivel.ID_MODIFICADOR_DESCUENTO, "Descuento global", "10.00", c_int(0).value, "CodigoInterno4567890123456789012345678901234567890" )
	ConsultarDescripcionDeError(res, 'Descuento cargado')
def CargarAjuste(Handle, vals=None):
	res = Handle.CargarAjuste( HighNivel.ID_MODIFICADOR_AJUSTE, "Ajuste Global", "20.00", c_int(0).value, "CodigoInterno4567890123456789012345678901234567890" )
	ConsultarDescripcionDeError(res, 'ajuste cargado')
def CargarPago(Handle, id_modificador ,codigo_forma_pago , cantidad_cuotas ,monto , descripcion_cupones , descripcion , descripcion_extra1 , descripcion_extra2):
	res = Handle.CargarPago(id_modificador, codigo_forma_pago , cantidad_cuotas ,monto , descripcion_cupones , descripcion , descripcion_extra1 , descripcion_extra2)
	ConsultarDescripcionDeError(res, 'Pago Cargado')


def Tique(values, nota_credito=False):
	#print('Ticket: ', values)
	try:
		Desconectar()
		Handle =  Conectar()
		Cancelar(Handle)
		if not nota_credito:	
			AbrirComprobante(Handle, HighNivel.ID_TIPO_COMPROBANTE_TIQUET)
		else:
			AbrirComprobante(Handle, HighNivel.ID_TIPO_COMPROBANTE_TIQUE_NOTA_DE_CREDITO)
		#CargarTextoExtra(Handle, 'N°: ' + values['name'])
		EnviarComando(Handle, '0707|0000')
		EnviarComando(Handle, '0707|0001')

		#Handle.CargarComprobanteAsociado( "083-00001-00000027" )
		for item in values['items']:		
			cmd = LowNivel.TICKET_ITEM + item
			EnviarComando(Handle, cmd)
	
		for discount in values['descuentos']:						
			cmd = LowNivel.TICKET_DISCOUNT + discount
			EnviarComando(Handle, cmd)
	
		for ajuste in values['ajustes']:	
			cmd = LowNivel.TICKET_ADJUSTMENT + ajuste
			EnviarComando(Handle, cmd)
		
		for pay in values['pagos']:
			cmd = LowNivel.TICKET_PAYMENT + pay
			EnviarComando(Handle, cmd)

		CerrarComprobante(Handle)
		Desconectar()
		return True
	except  Exception  as  e:
		#print('Exception: ',str(e))	
		return str(e)
		'''if len(e.args) > 0:	
			return e.args[0]
		else: return 'Error Inesperado'''

#vals = "|||||Antibacterial|20000|25000|2100|||||1234567890|1|7"
def CargarDatosCliente(Handle, vals):
	print('CargarDatosCliente: ', vals)
	nombre_o_razon_social1 = vals['nombre_o_razon_social1']
	nombre_o_razon_social2 = vals['nombre_o_razon_social2']
	domicilio1 = vals['domicilio1']
	domicilio2 = vals['domicilio2']
	domicilio3 = vals['domicilio3']
	id_tipo_documento = vals['id_tipo_documento']
	numero_documento = vals['numero_documento']
	id_responsabilidad_iva = vals['id_responsabilidad_iva']

	print('numero_documento: ', numero_documento)
	res = Handle.CargarDatosCliente(nombre_o_razon_social1, nombre_o_razon_social2, domicilio1, domicilio2, domicilio3, id_tipo_documento, numero_documento, id_responsabilidad_iva)
	#res = Handle.CargarDatosCliente( "Nombre Comprador #1", "Nombre Comprador #2", "Domicilio Comprador #1", "Domicilio Comprador #2", "Domicilio Comprador #3",HighNivel.ID_TIPO_DOCUMENTO_CUIT, "24272242549", HighNivel.ID_RESPONSABILIDAD_IVA_RESPONSABLE_INSCRIPTO )
	print('CargarDatosCliente: ', res)
	ConsultarDescripcionDeError(res, 'Cliente Cargado')
def CargarComprobanteAsociado(Handle, comprobante):
	print('CargarComprobanteAsociado: ', comprobante)
	res  = Handle.CargarComprobanteAsociado(comprobante)
	ConsultarDescripcionDeError(res, 'Comprobante Cargado')

def TiqueFactura(values):
	print('TiqueFactura values: ', values)
	try:
		Desconectar()
		Handle =  Conectar()
		Cancelar(Handle)
		OPEN_FACTURA = LowNivel.TICKET_OPEN_FACTURA		
		cmd = OPEN_FACTURA + values['cliente'] 
		EnviarComando(Handle, cmd)
		EnviarComando(Handle, '0707|0000')
		EnviarComando(Handle, '0707|0001')
		
		
		#print('---- cliente')
		for item in values['items']:		
			cmd = LowNivel.TICKET_ITEM_FACTURA + item
			EnviarComando(Handle, cmd)
		for discount in values['descuentos']:					
			cmd = LowNivel.TICKET_DISCOUNT_FACTURA + discount
			EnviarComando(Handle, cmd)
		for ajuste in values['ajustes']:		
			cmd = LowNivel.TICKET_ADJUSTMENT_FACTURA + ajuste
			EnviarComando(Handle, cmd)
		
		for pay in values['pagos']:
			cmd = LowNivel.TICKET_PAYMENT_FACTURA + pay
			EnviarComando(Handle, cmd)

		CerrarComprobante(Handle)
		Desconectar()
		return True
	except Exception as e:
		return str(e)

def TiqueFacturaNC(values):
	#print('TiqueFactura nota_credito: ')
	try:
		Desconectar()
		Handle =  Conectar()
		Cancelar(Handle)
		OPEN_FACTURA = LowNivel.TICKET_NC_OPEN_FACTURA		
		cmd = OPEN_FACTURA + values['cliente'] 
		EnviarComando(Handle, cmd)	

		for item in values['items']:		
			cmd = LowNivel.TICKET_NC_ITEM_FACTURA + item
			EnviarComando(Handle, cmd)
		for discount in values['descuentos']:					
			cmd = LowNivel.TICKET_NC_DISCOUNT_FACTURA + discount
			EnviarComando(Handle, cmd)
		for ajuste in values['ajustes']:		
			cmd = LowNivel.TICKET_NC_ADJUSTMENT_FACTURA + ajuste
			EnviarComando(Handle, cmd)
		
		for pay in values['pagos']:
			cmd = LowNivel.TICKET_NC_PAYMENT_FACTURA + pay
			EnviarComando(Handle, cmd)


		CerrarComprobante(Handle)
		Desconectar()
		return True
	except Exception as e:
		return str(e)

def ImprimirCierre(type):
	#print('TiqueFactura nota_credito: ')
	try:
		Desconectar()
		Handle =  Conectar()
		Cancelar(Handle)
		if type == 'x':
			ImprimirCierreX(Handle)
		elif type == 'z':
			ImprimirCierreZ(Handle)
		Desconectar()
		return True
	except Exception as e:
		return str(e)


def EstadoEstacionRecibos():

	try:
		Desconectar()
		Handle =  Conectar()
		res = ConsultarEstado(Handle, 7001)
		Desconectar()

		if res == 0:
			return True
		elif res == 1:
			return "Poco Papel Disponible"
		elif res == 2:
			return "Papel no Disponible"
	except Exception as e:
		return str(e)
		
		