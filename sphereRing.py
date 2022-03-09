from maya import cmds
import math

def reRange(oldValue):
	oldMax = 1
	oldMin = -1
	newMax = 1
	newMin = 0
	oldRange = oldMax - oldMin
	newRange = newMax - newMin
	newValue = (((oldValue-oldMin)*newRange)/oldRange)+newMin
	return newValue

for i in range(1,73):
	cmds.polySphere()
	cmds.move(0,0,-10, relative = True)
	cmds.move(0,0,10,('pSphere' + str(i) + '.scalePivot'), ('pSphere' + str(i) + '.rotatePivot'), relative=True)
	cmds.rotate(0,5*i,0, r=True, os=True)
	
	yTranslate = math.sin(math.radians(5*i))
	
	cmds.move(0,yTranslate,0, relative = True)
	cmds.expression(string = f"pSphere{i}.translateY = sin(time + {i})", object = f'pSphere{i}', ae=True, uc='all')
	
	redVal = math.sin(math.radians(i * 5))
	redVal = reRange(redVal)
	# we are shifting the sin wave 120 degrees
	greenVal = math.sin(math.radians(i * 5 + 120))
	greenVal = reRange(greenVal)
	blueVal = math.sin(math.radians(i * 5 + 240))
	blueVal = reRange(blueVal)
	
	# requires to be operated on polygon meshs not nurbs
	cmds.polyColorPerVertex( rgb=(redVal, greenVal, blueVal), cdo=True )
