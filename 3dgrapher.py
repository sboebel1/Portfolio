import pygame as pygame
import Grapher as gp
import numpy as np
import fracs as fr
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
szeX = 800
szeY = 600
print("Window Size (dflt = 800x600)")
strMe = input()
if (type(str) == tuple):
	szeX, szeY = strMe
 
dis = pygame.display.set_mode((szeX, szeY))
pygame.display.set_caption('3d grapher')
 
game_over = False
 
a = szeX/2
b = szeY/2
ranges = 1
x1 = 0
y1 = 0
z1 = 0
pi = np.pi
tpi = np.pi*2
fname = "kshlipp$"

axlen = 4
 
a1_change = 0       
b1_change = 0
r1_change = 0
x1_change = 0
y1_change = 0
z1_change = 0
inputStr = ""

eyeVector = [1,0,((5/4)*np.pi)]

clock = pygame.time.Clock()

tParam = np.linspace(-1,1,100)

# Graphing functions

def xax(t):
	return [axlen*t,0,0]
def yax(t):
	return [0,axlen*t,0]
def zax(t):
	return [0,0,axlen*t]

def plane(s,t):
	return [axlen*0.5*s,axlen*0.5*t,0]

def sphere(t,s):
	theta = ((t+1)/2)*2*(np.pi)
	phi = ((s+1)/2)*(np.pi)
	return [np.cos(theta)*np.sin(phi),np.sin(theta)*np.sin(phi),np.cos(phi)]
	


# Helper functions 

def posChng(eyeVector,newR,newA,newB):
	origCartesianVector = gp.cart(eyeVector)
	newCartesianVector = gp.cart([(eyeVector[0]+newR),(eyeVector[1]+newA),(eyeVector[2]+newB)])	
	return fr.addbynum(origCartesianVector,fr.xsl(-1,newCartesianVector))

def drawPt(a,color):
	it = gp.get2d(a,[ranges,anew,bnew])
	pygame.draw.circle(dis,color,((50*it[0]+szeX/2),(50*it[1]+szeY/2)),3)

def drawVector(a,color):
	def vf(t):
		return [a[0]*(t+1)/2,a[1]*(t+1)/2,a[2]*(t+1)/2]

	drawIt(vf,color)
	drawPt(a,color)

def drawIt(vectorFunction,color):
	def newVectorFunction(t):
		return [(vectorFunction(t)[0]+x1),(vectorFunction(t)[1]+y1),(vectorFunction(t)[2]+z1)]

	it = gp.get2d(newVectorFunction(tParam),[ranges,anew,bnew])
	pygame.draw.lines(dis, color, False, gp.organize2d([(50*it[0]+(szeX/2)),(50*it[1]+(szeY/2))]))

def write2d(textIt,pt,sze,color):
	font = pygame.font.SysFont(None, sze)
	img = font.render(textIt, True, color)
	dis.blit(img, pt)

def write3d(textIt,pt3d,sze,color):
	pt3dNew = [(pt3d[0]+x1),(pt3d[1]+y1),(pt3d[2]+z1)]
	pt2d = gp.get2d(pt3dNew,[ranges,anew,bnew])
	xs = 50*pt2d[0]+(szeX/2)
	ys = 50*pt2d[1]+(szeY/2)
	write2d(textIt,[xs,ys],sze,color)


def drawItALot(vectorWithTandS,quality,color):
	sParam2 = np.linspace(-1,1,quality).tolist()
	for i in range(0,len(sParam2)):
		def newVectorX(t):
			return vectorWithTandS(t,sParam2[i]) 
		def newVectorY(t):
			return vectorWithTandS(sParam2[i],t)
		
		drawIt(newVectorY,color)
		drawIt(newVectorX,color)

def sysInput():
	loop_over = False
	print("inputting--")
	varName = ""
	keyIt = ""
	while (not loop_over):
		for event2 in pygame.event.get():
			if ((event2.type == pygame.KEYDOWN) and (event2.key == pygame.K_RETURN)):
				loop_over = True
			if (event2.type == pygame.QUIT):
				game_over = True
				print("Closed window. Thaks for playing.")
			if (event2.type == pygame.KEYDOWN):
				keyIt = event2.unicode
				varName = varName + keyIt
				print(keyIt)
			if ((event2.type == pygame.KEYDOWN) and (event2.key == pygame.K_DOWN)):
				varName = varName + "\n"

	return varName

def constructFun(fname,freturn):
	prog = "def " + fname.strip("\r") + "(t):\n		return " + freturn.strip("\r")
	exec(prog)
	exec("f=" + fname.strip("\r"))
	return f
	

# Window instance
 
while (not game_over):
	for event in pygame.event.get():
		if (event.type == pygame.QUIT):
			game_over = True
			print("Closed window. Thanks for playing.")

		if ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_i)):
			inStr = sysInput()

		if (event.type == pygame.KEYDOWN):
			
			if event.key == pygame.K_a:
                		a1_change = -5
                		b1_change = 0
			elif event.key == pygame.K_d:
                		a1_change = 5
               			b1_change = 0
			elif event.key == pygame.K_w:
                		a1_change = 0
                		b1_change = 5
			elif event.key == pygame.K_s:
                		a1_change = 0
                		b1_change = -5
			elif event.key == pygame.K_c:
				a1_change = 0
				b1_change = 0
				r1_change = 0
			elif event.key == pygame.K_RSHIFT:
				x1_change = 0
				y1_change = 0
				z1_change = 0


			elif event.key == pygame.K_q:
				r1_change = -0.1*axlen
			elif event.key == pygame.K_x:
				r1_change = 0.1*axlen
			elif event.key == pygame.K_RIGHT:
				x1_change = -(1/8)*axlen
			elif event.key == pygame.K_LEFT:
				x1_change = (1/8)*axlen
			elif event.key == pygame.K_UP:
				y1_change = (1/8)*axlen
			elif event.key == pygame.K_DOWN:
				y1_change = -(1/8)*axlen
			elif event.key == pygame.K_SPACE:
				z1_change = -(1/8)*axlen
			elif event.key == pygame.K_LSHIFT:
				z1_change = (1/8)*axlen	


			
						
					
					
					
			
	a += a1_change
	b += b1_change
	ranges += r1_change
	x1 += x1_change
	y1 += y1_change
	z1 += z1_change
	x1_change = 0
	y1_change = 0
	z1_change = 0
	r1_change = 0
	dis.fill(white)
	anew = ((a/800)-(1/2))*2*np.pi
	bnew = (((b/800)-(1/2))*2*np.pi)-np.pi
	eyeVector = [ranges,anew,bnew]
	eyeCart = gp.cart(eyeVector)
	pygame.draw.circle(dis, black, (szeX/2, szeY/2), 3) 


	drawIt(xax,(0,0,0))
	drawIt(yax,(0,0,0))
	drawIt(zax,(0,0,0))
	drawItALot(plane,5,(0,0,0))
	drawItALot(sphere,10,(0,0,0))
	
	write3d('+x',[axlen,0,0],20,black)
	write3d('-x',[-axlen,0,0],20,black)
	write3d('+y',[0,axlen,0],20,black)
	write3d('-y',[0,-axlen,0],20,black)
	write3d('+z',[0,0,axlen],20,black)
	write3d('-z',[0,0,-axlen],20,black)
	write3d(str(axlen/2),[axlen/2,0,0],20,black)
	write3d(str(-axlen/2),[-axlen/2,0,0],20,black)
	write3d(str(axlen/2),[0,axlen/2,0],20,black)
	write3d(str(-axlen/2),[0,-axlen/2,0],20,black)
	write3d(str(axlen/2),[0,0,axlen/2],20,black)
	write3d(str(-axlen/2),[0,0,-axlen/2],20,black)
	write2d(('Pt Location: x: ' + str(x1) + ' y: ' + str(y1) + ' z: ' + str(z1) + ' '),[20,20],20,black)
	write2d(inputStr,[20,40],20,black)
	pygame.display.update()
	clock.tick(30)
 
pygame.quit()
quit()