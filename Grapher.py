# 3d grapher. 
import numpy as np
import sympy as sp

def dot(a,b):
	x = 0
	for i in range(0,len(a)):
		x = x + (a[i]*b[i])

	return x

def get2d(threeD,Aon):
	Ao = [(1/Aon[0]),Aon[1],Aon[2]]
	Xl = [Ao[0]*np.cos(Ao[1]),Ao[0]*-np.sin(Ao[1]),0]
	Yl = [Ao[0]*((np.sin(Ao[1]))*(np.sin(Ao[2]))),Ao[0]*((np.cos(Ao[1]))*(np.sin(Ao[2]))),Ao[0]*(np.cos(Ao[2]))]
	return [dot(threeD,Xl),dot(threeD,Yl)]

def organize2d(list):
	xs = list[0]
	ys = list[1]
	x = [0]
	for i in range(0,len(xs)):
		x = x + [[xs[i],ys[i]]]

	x.pop(0)
	return x

def cart(sph):
	x = sph[0]*np.cos(sph[1])*np.sin(sph[2])
	y = sph[0]*np.sin(sph[1])*np.sin(sph[2])
	z = sph[0]*np.cos(sph[2])
	return [x,y,z]

t = np.linspace(-1,1,1000)

axlen = 4

xax = [axlen*t,0,0]
yax = [0,axlen*t,0]
zax = [0,0,axlen*t]

eye = [1,(np.pi/4),(np.pi/4)]

def flistMe(flist3d,Aon):
	x = [0]
	for i in range(0,len(flist3d)):
		x = x + [get2d(flist3d[i],Aon)]

	y = x
	x.pop(0)
	return x

def subList(list,var,newVal):
		x = [0]
		for i in range(0,len(list)):
			x = x + [list[i].subs(var,newVal)]

		x.pop(0)
		return x

AxesList = flistMe([xax,yax,zax],eye)	

xarr1 = [axlen-((t+1)/8),((t+1)/8),0]

xarr2 = [axlen-((t+1)/8),-((t+1)/8),0]

xarr3 = [-(axlen-((t+1)/8)),-((t+1)/8),0]

xarr4 = [-(axlen-((t+1)/8)),((t+1)/8),0]

yarr1 = [0,((t+1)/8),axlen-((t+1)/8)]

yarr2 = [0,-((t+1)/8),axlen-((t+1)/8)]

yarr3 = [0,((t+1)/8),-(axlen-((t+1)/8))]

yarr4 = [0,-((t+1)/8),-(axlen-(t+1)/8)]

zarr1 = [((t+1)/8),axlen-((t+1)/8),0]

zarr2 = [-((t+1)/8),axlen-((t+1)/8),0]

zarr3 = [-((t+1)/8),-(axlen-((t+1)/8)),0]

zarr4 = [((t+1)/8),-(axlen-((t+1)/8)),0]

arrList = flistMe([xarr1,xarr2,xarr3,xarr4,yarr1,yarr2,yarr3,yarr4,zarr1,zarr2,zarr3,zarr4],eye)







