#-*-coding: GB2312 -*-
import sys, os, time, logging
import json
from socketio_client import SocketIO, BaseNamespace
class ProcessNamespace(BaseNamespace):
    def on_connect(self):
        print('[Connected]')
socketIO = SocketIO('test.boonray.com',8080)
process_socket = socketIO.define(ProcessNamespace, '/process')
def get_data(da):
    print(da)
process_socket.on('process_12_88', get_data)