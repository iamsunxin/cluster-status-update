import socket
import logging
import time
from socketio_client.manager import Manager
import schedule
import time
import socketio
import socket
f = open('./statuslog.txt')
logging.basicConfig(filename='../LOG/'+__name__+'.log',
                    format ='[%(asctime)s-%(filename)s-%(levelname)s:%(message)s]',
                    level = logging.DEBUG,
                    filemode='a',
                    datefmt='%Y-%m-%d%I:%M:%S %p')

io1 = Manager(scheme='http',hostname='test.boonray.com', port=8080)
s = io1.connect()
logging.info('prepared to connect sock_serv')

def on_message(*args):
    # print "recv:", args
    # print "geted:", type(args[0])
    print('on_msg')
'''
data = {
    "sn": 0,
    "ver": 2}
# send data to message
s.emit('message', data, on_message)
s.sendf(data, on_message)  # default send data to message
# send data to login
s.emit('login', data, on_message)
s.wait_for_callbacks(seconds=1)
'''

def status_update():
    try:
        data = 'test for 2d,3d model'
        io1.emit ('update process',{
            'topic':'taskid499',
            'percent':49,
            'message':data
        })
        logging.info('datasend succ')
        io1.handle_close()
    except Exception:
        print('remote offline')
        io1.handle_close()

schedule.every(5).seconds.do(status_update)
while True:
    schedule.run_pending()
    time.sleep(1)
