############################################################## 
# Licensed under the MIT License                             #
# Copyright (c) 2018 Stefan Hein Bengtson and Malte Pedersen #
# See the file LICENSE for more information                  #
##############################################################

import argparse
import os
import sys
from sklearn.externals import joblib

import sys
sys.path.append('D:\\bishe\\aauvap-3d-zef-7230261dcb99\\aauvap-3d-zef-7230261dcb99\\')
from modules.reconstruction.Camera import Camera

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--path", help="Path to folder")
ap.add_argument("-c", "--camId", help="Camera ID. top = 1 and front = 2")

args = vars(ap.parse_args())

path = args["path"]
camId = args["camId"]

intrinsicJson = os.path.join(path, "cam{}_intrinsic.json".format(camId))
extrinsicJson = os.path.join(path, "cam{}_references.json".format(camId))

cam = Camera(intrinsicJson, extrinsicJson)

outputName = os.path.join(path, 'cam{}.pkl'.format(camId))
print('Saving data to: ' + str(outputName))
joblib.dump(cam, outputName)
