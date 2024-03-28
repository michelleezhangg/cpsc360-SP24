import os
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

def drawAxes():                                                             # draw x-axis and y-axis
    glLineWidth(3.0)                                                        # specify line size (1.0 default)
    glBegin(GL_LINES)                                                       # replace GL_LINES with GL_LINE_STRIP or GL_LINE_LOOP
    glColor3f(1.0, 0.0, 0.0)                                                # x-axis: red
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(100.0, 0.0, 0.0)                                             # v1
    glColor3f(0.0, 1.0, 0.0)                                                # y-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 100.0, 0.0)                                             # v1
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: green
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

def draw_Scarecrow():                                                  # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode

    # configure quatratic drawing
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_FILL)  

    # Head (sphere: radius=2.5) 
    glPushMatrix()
    glTranslatef(0.0, 12.5, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    gluSphere(quadratic, 2.5, 32, 32)
    glPopMatrix()

    # Nose (cylinder: radius=0.2, length=2)
    glPushMatrix()
    glTranslatef(0.0, 12.5, 2.5)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 0.3, 0.0, 1.8, 32, 32)
    glPopMatrix()    

    # Torso (cylinder: radius=2.5, length=10)
    glPushMatrix()
    glRotatef(-90.0, 1, 0, 0)
    glColor3f(1.0, 1.0, 0.0)
    gluCylinder(quadratic, 2.5, 2.5, 10.0, 32, 32)
    glPopMatrix()

    # Left Leg (cylinders: radius=1.0, length=12)
    glPushMatrix()
    glTranslatef(-1.2, 0.0, 0.0)
    glRotatef(90.0, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Right Leg (cylinders: radius=1.0, length=12)
    glPushMatrix()
    glTranslatef(1.2, 0.0, 0.0)
    glRotatef(90.0, 1, 0, 0)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Left Arm (cylinders: radius=0.8, length=10)
    glPushMatrix()
    glTranslatef(-2.5, 9.0, 0.0)
    glRotatef(-90.0, 0, 1, 0)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # Right Arm (cylinders: radius=0.8, length=10)
    glPushMatrix()
    glTranslatef(2.5, 9.0, 0.0)
    glRotatef(90.0, 0, 1, 0)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

def main():
    pygame.init()                                                           # initialize a pygame program

    #os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 50)               # specify the position of the display window (default: screen center)

    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_window = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)    # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - View Transform')                 # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)                                         # the viewport can be identical or smaller than the display window
    #glViewport(0, 0, width//2, height//2)                                  # use integer division to set viweport size be half of the window 
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100.0)                        # specify perspective-projection view volume
    #glOrtho(-40, 40, -30, 30, 40, 60)                                      # specify an orthogonal-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)

    # Static view: set camera's eye, look-at, and view-up in the world
    #gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0) 
    #gluLookAt(50, 0, 0, 0, 0, 0, 0, 1, 0)                                   
    gluLookAt(0, 50, 0, 0, 0, 0, 0, 0, 1) 
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
    offset_z = 0
    while True:
        bResetModelMatrix = False

        # user interface event handling
        for event in pygame.event.get():

            # quit the window
            if event.type == pygame.QUIT:
                pygame.quit()

            # mouse event
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

            # keyboard event
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    bResetModelMatrix = True
                elif event.key == pygame.K_UP:
                    offset_z += 1
                elif event.key == pygame.K_DOWN:
                    offset_z -= 1

        draw_Scarecrow()                                                    # model creation and geom transforms

        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
            offset_z = 0
        
        glPushMatrix()
        glLoadMatrixf(initmodelMatrix)
        drawAxes()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

main()