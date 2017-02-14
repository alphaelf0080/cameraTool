import maya.cmds as cmds
import math
import numpy

filmWidth =36.0
filmHight =24.0
focalLength = 50.0
filmBack = math.sqrt(math.pow(filmWidth,2)+math.pow(filmHight,2))

cameraAngleD = 2 * math.atan((filmBack/2)/focalLength)/(math.pi)*180 # angle diagonal
cameraAngleH = 2 * math.atan((filmWidth/2)/focalLength)/(math.pi)*180 # angle horizontal
cameraAngleV = 2 * math.atan((filmHight/2)/focalLength)/(math.pi)*180 # angle vertical
print cameraAngleD," ",cameraAngleH," ",cameraAngleV

a =(filmBack/2)/focalLength

math.atanh(0.4326661530)

math.sin(math.degrees((math.pi)/2))

math.radians(180)

18.0/50.0