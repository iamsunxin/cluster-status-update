
import sys, os, time, logging
import json
from socketio_client import SocketIO, BaseNamespace
def task_stat_updata():
    class ProcessNamespace(BaseNamespace):
        def on_aaa_response(self, *args):
            print('on_process_response', args)

    #topic = data.topic
    #process= data.process
    #message = data.message
    socketIO = SocketIO('test.boonray.com', 8080)
    process_socket = socketIO.define(ProcessNamespace, '/process')
    process_data = {
        'topic':"test",
        'process': 90,
        'message':'update test'
    }
    process_socket.emit('update process', process_data)
    socketIO.wait(seconds=1)
while(1):
    task_stat_updata()
    time.sleep(10)