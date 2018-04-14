from phBot import *

import QtBind
import binascii

gui = QtBind.init(__name__, 'PacketLogger')

padding_left = 260
padding_top = 125

QtBind.createLabel(gui, 'client to server', padding_left + 11, padding_top + 10)
QtBind.createButton(gui, 'log_client_start', 'start', padding_left + 10, padding_top + 30)
QtBind.createButton(gui, 'log_client_stop', 'stop', padding_left + 10, padding_top + 60)

QtBind.createLabel(gui, 'server to client', padding_left + 111, padding_top + 10)
QtBind.createButton(gui, 'log_server_start', 'start', padding_left + 110, padding_top + 30)
QtBind.createButton(gui, 'log_server_stop', 'stop', padding_left + 110, padding_top + 60)

log_client = False
log_server = False


def handle_silkroad(opcode, data):
    if log_client:
        log('[%s]: packet from client to server' % (__name__))
        log('[%s]: \topcode: 0x%02X' % (__name__, opcode))
        if data is not None:
            log('[%s]: \tdata: %s' % (__name__, binascii.hexlify(data)))
    return True


def handle_joymax(opcode, data):
    if log_server:
        if opcode == 0x2002:
            return True  # we don't want to log pings
        log('[%s]: packet from server to client' % (__name__))
        log('[%s]: \topcode: 0x%02X' % (__name__, opcode))
        if data is not None:
            log('[%s]: \tdata: %s' % (__name__, binascii.hexlify(data)))
    return True


def log_client_start():
    global log_client
    log('[%s]: log client started' % (__name__))
    log_client = True


def log_client_stop():
    global log_client
    log('[%s]: log client stopped' % (__name__))
    log_client = False


def log_server_start():
    global log_server
    log('[%s]: log server started' % (__name__))
    log_server = True


def log_server_stop():
    global log_server
    log('[%s]: log server stopped' % (__name__))
    log_server = False


log('[%s] loaded' % (__name__))
