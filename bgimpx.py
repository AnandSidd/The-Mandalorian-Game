from PIL import Image
from sys import argv
import numpy as np
class Pxl:
	def __init__(self,path):
		self._path=path
		self._pixel_values=[]
		self._width=238
		self._height=50
	def getpx(self):	
		image=Image.open(self._path, 'r')
		image=image.resize((self._width,self._height ), Image.ANTIALIAS)
		image=image.convert('RGB')
		self._pixel_values = list(image.getdata())
		self._pixel_values = np.array(self._pixel_values).reshape((self._height,self._width, 3))
		return self._pixel_values
# obj=Pxl("dawn.jpg")
# pixel_values=obj.getpx()
# for x in range(50):
# # 	for y in range(width1-1,0,-1):
# # 		p0=int((255-pixel_values[x][y][0]))
# # 		p1=int((255-pixel_values[x][y][1]))
# # 		p2=int((255-pixel_values[x][y][2]))
# # 	# 	# "+str(pixel_values[x][y][0])+"
# # 	# 	# stdout.write("\x1b[38;2;"+str(pixel_values[x][y][0])+";"+str(pixel_values[x][y][1])+";"+str(pixel_values[x][y][2])+"m\u2588\x1b[0m")
# # 		# f.write("\x1b[38;2;"+str(p0)+";"+str(p1)+";"+str(p2)+"m\u2588\x1b[0m")
# # 		print("\x1b[38;2;"+str(p0)+";"+str(p1)+";"+str(p2)+"m\u2588\x1b[0m",end="")
# 	for y in range(238):
# 		p0=int(pixel_values[x][y][0])
# 		p1=int(pixel_values[x][y][1])
# 		p2=int(pixel_values[x][y][2])
# 	# 	# "+str(pixel_values[x][y][0])+"
# 	# 	# stdout.write("\x1b[38;2;"+str(pixel_values[x][y][0])+";"+str(pixel_values[x][y][1])+";"+str(pixel_values[x][y][2])+"m\u2588\x1b[0m")
# 		# f.write("\x1b[38;2;"+str(p0)+";"+str(p1)+";"+str(p2)+"m\u2588\x1b[0m")
# 		print("\x1b[38;2;"+str(p0)+";"+str(p1)+";"+str(p2)+"m\u2588\x1b[0m",end="")
# 		# stdout.write("\x1b[38;2;"+str(pixel_values[x][y][0])+";"+str(pixel_values[x][y][1])+";"+str(pixel_values[x][y][2])+"m\u2588\x1b[0m")
# 		# print("\x1b[38;2;"+str(pixel_values[x][y][0])+";"+str(pixel_values[x][y][1])+";"+str(pixel_values[x][y][2])+"m\u2588\x1b[0m",end="")
# 		# print("\x1b[38;2;"+str(pixel_values[x][y][0])+";"+str(pixel_values[x][y][1])+";"+str(pixel_values[x][y][2])+"m#\x1b[0m",end="")
# 		# print("x=",x,"y=",y)
# 	print("")















