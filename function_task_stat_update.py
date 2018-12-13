import sys, os, time, logging
import json
from socketIO_client import SocketIO, BaseNamespace

def task_stat_updata(data):
    class ProcessNamespace(BaseNamespace):
        def on_aaa_response(self, *args):
            print('on_process_response', args)

        def on_update_process(self, *args):
            print('on_aaa_response', args)
    topic = data.topic
    process= data.percent
    message = data.message
    socketIO = SocketIO('test.boonray.com', 8080)
    process_socket = socketIO.define(ProcessNamespace, '/process')
    process_data = {
        'topic':topic,
        'percent':process,
        'message':message
    }
    def on_update_process(*args):
        messages = list(args)
        print('on_aaa_response', messages.get)

    process_socket.emit('update process', process_data)
    #process_socket.on('process_1288',on_update_process)
    print('msg send')
    socketIO.wait(3)
while(1):
    task_stat_updata()
    print('server')
    time.sleep(3)