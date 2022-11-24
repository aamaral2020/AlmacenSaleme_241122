
from ctypes import byref, c_int, c_char, c_long, c_short, create_string_buffer, cdll
import binascii
import sys



import platform
import os
EpsonLibInterface = False
def get_driver():
	try:
		
	
		name_os = platform.system()
		path  = os.path.dirname(os.path.realpath(__file__))
		#print ('path library: '), path
		archbits = platform.architecture()[0]
		if name_os == 'Linux':
			
			
			
			if archbits[0:2] == "64":
				fullpath = path + '/Library/Linux/64/libEpsonFiscalInterface.so'
			else:
				fullpath = path + '/Library/Linux/32/libEpsonFiscalInterface.so'

			#print('fullpath: ' , fullpath)
		
			import ctypes
			EpsonLibInterface = ctypes.cdll.LoadLibrary(fullpath)
		
		else:
			from ctypes import windll
			#Ojo: Siempre se va a leer la dll de 32 bits, porque se esta utilizando el python de 32 bits
			'''if archbits[0:2] == "64":
				fullpath =  path + "\\Library\\Windows\\64\\EpsonFiscalInterface.dll"
			else:'''
			print('fullpath: ')
			fullpath =  path + "\\Library\\Windows\\32\\EpsonFiscalInterface.dll"
			print('fullpath: ' , fullpath)
			
			EpsonLibInterface = windll.LoadLibrary(fullpath)
	except Exception as e:	
		raise Exception(e)

	return EpsonLibInterface

