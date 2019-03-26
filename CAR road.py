from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import*


def myinit():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, 1, .1, 30)
    gluLookAt(8, 9, 10,
              0, 0, 0,
              0, 1, 0)
    glClearColor(0, .7, 0, 1)
    glClear(GL_COLOR_BUFFER_BIT)


angle = 0
x = 0
forward = True


def draw():
    global angle
    global x
    global forward
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glBegin(GL_POLYGON)
    glColor3f(.1, .3, 0)
    glVertex3d(8, 4, 1)
    glVertex3d(-22, 4, 1)
    glVertex3d(-20, -4, 2)
    glVertex3d(11, -4, 2)
    glEnd()
    glLoadIdentity()

    glBegin(GL_POLYGON)
    glColor3f(.5, .3, .1)
    glVertex2d(5, 4)
    glVertex2d(4, 4)
    glVertex2d(4, 6.5)
    glVertex2d(5, 6.5)
    glEnd()
    glLoadIdentity()
    drawbolyCircle(1, 4.5, 7, .3, .9, 0)

    #car tires
    glColor3f(0, 0, 1)
    glTranslate(2+x, -2.5 * .4, 1 * .6)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glTranslate(-1.5+x, -2.5 * .4, 2 * .6)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glTranslate(2+x, -2.5 * .5, -2.5 * .6)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
    glTranslate(-2+x, -2.5 * .5, -2.5 * .6)
    glRotate(angle, 0, 0, 1)
    glutSolidTorus(.25, .5, 12, 9)
    glLoadIdentity()
#car

    glColor3f(1, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, .25, .5)
    glutSolidCube(5)
    glLoadIdentity()
    glTranslate(x, 5*.25, 0)
    glScale(.5, .25, .5)
    glutSolidCube(4)
    glLoadIdentity()

#sphere
    glColor3f(.9, 1, 0)
    glTranslate(2.5+x, 0, 1)
    glutSolidSphere(.4, 10, 10)
    glLoadIdentity()
    glTranslate(2.5+x, 0, -1)
    glutSolidSphere(.4, 10, 10)






    if forward:
        angle -= .1
        x += .005
        if x > 6:
            forward = False
    else:
        x -= .005
        angle += .1

        if x < -11:
            forward = True




    glutSwapBuffers()


def drawbolyCircle(r=.01, xc=0, yc=0, a=0, b=0, c=0):
    glColor3f(a, b, c)
    glBegin(GL_POLYGON)
    for theta in np.arange(0, 2 * pi, .1):
        x = r*cos(theta)
        y = r*sin(theta)
        glVertex(x+xc, y+yc)

    glEnd()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(600, 600)
glutCreateWindow(b"car_road")
glutDisplayFunc(draw)
glutIdleFunc(draw)   #rotaion
myinit()
glutMainLoop()
