from phBot import *

import QtBind
import binascii

gui = QtBind.init(__name__, 'PacketLogger')

paddingLeft = 260
paddingTop  = 125

QtBind.createLabel(gui, 'client to server', paddingLeft+11, paddingTop+10)
QtBind.createButton(gui, 'log_client_start', 'start', paddingLeft+10, paddingTop+30)
QtBind.createButton(gui, 'log_client_stop', 'stop', paddingLeft+10, paddingTop+60)

QtBind.createLabel(gui, 'server to client', paddingLeft+111, paddingTop+10)
QtBind.createButton(gui, 'log_server_start', 'start', paddingLeft+110, paddingTop+30)
QtBind.createButton(gui, 'log_server_stop', 'stop', paddingLeft+110, paddingTop+60)

logClient = False
logServer = False

def handle_silkroad(opcode, data):
	if logClient == True:
		log('[%s]: packet from client to server' %(__name__))
		log('[%s]: \topcode: 0x%02X' %(__name__, opcode))
		if data is not None:
			log('[%s]: \tdata: %s' %(__name__, binascii.hexlify(data)))
	return True

def handle_joymax(opcode, data):
	if logServer == True:
		if opcode == 0x2002:
			return True # we don't want to log pings
		log('[%s]: packet from server to client' %(__name__))
		log('[%s]: \topcode: 0x%02X' %(__name__, opcode))
		if data is not None:
			log('[%s]: \tdata: %s' %(__name__, binascii.hexlify(data)))
	return True

def log_client_start():
	log('[%s]: log client started' %(__name__))
	global logClient
	logClient = True

def log_client_stop():
	log('[%s]: log client stopped' %(__name__))
	global logClient
	logClient = False

def log_server_start():
	log('[%s]: log server started' %(__name__))
	global logServer
	logServer = True

def log_server_stop():
	log('[%s]: log server stopped' %(__name__))
	global logServer
	logServer = False

log('[%s] loaded' %(__name__))