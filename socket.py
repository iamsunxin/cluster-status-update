import sys, os, time, config, logging
import json
from socketIO_client import SocketIO, BaseNamespace
from functions_cc import make3dTileWithNewProject
from functions_api import update3DAPIStatus

# test 3dtile quality
project_folder = "D:/Projects/boonray_cloud/auto_script/data/3d/test/"
img_folder = "D:/Projects/boonray_cloud/auto_script/data/3d/test_imgs/"
make3dTileWithNewProject(project_folder, img_folder)


# test 3d status update
# update3DAPIStatus("121", "1", "finished", "https://boonraycloudtest.oss-cn-hangzhou.aliyuncs.com/138/998/resultCC/Production_1.json")


# test socket progress
# class ProcessNamespace(BaseNamespace):
#     def on_aaa_response(self, *args):
#         print('on_process_response', args)
#
# socketIO = SocketIO('test.boonray.com', 8080)
# process_socket = socketIO.define(ProcessNamespace, '/process')
# process_data = {
#     'topic':"test",
#     'process': 90,
#     'message':'update test'
# }
# process_socket.emit('update process', process_data)
# socketIO.wait(seconds=1)
