import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

########################################### DO NOT MODIFY CODE BELOW ####################################################

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
)

faces = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

def cube():
    glColor3f(0.2, 0.5, 0.4)
    glBegin(GL_QUADS)
    for face in faces:
        x = 0
        for vertex in face:
            x += 1
            vertexPos = vertices[vertex]
            vertexPos = tuple(5*v+7 for v in vertexPos)
            glVertex3fv(vertexPos)
    glEnd()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            vertexPos = vertices[vertex]
            vertexPos = tuple(5*v+7 for v in vertexPos)
            glVertex3fv(vertexPos)
    glEnd()

def draw():                                                                 # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    cube()

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
########################################### ASSIGNMENT CODE ####################################################
def drawRotationAxis():
    glLineWidth(5.0)
    glColor3f(1.0, 1.0, 0.0)
    glBegin(GL_LINES)
    glVertex3f(7.0, 20.0, 7.0)
    glVertex3f(7.0, 0.0, 7.0)
    glEnd()

# For Assignment 5: Complete the two functions below
# Q1:
def spinningTransform(theta):
    glTranslatef(7.0, 7.0, 7.0) # translate the cube back to its original position (7,7,7)
    glRotatef(theta, 0.0, 1.0, 0.0) # rotate the cube at the origin by parameter theta around the y-axis
    glTranslatef(-7.0, -7.0, -7.0) # translate the cube to the origin to prepare for rotation
    return

# Q2:
def scaleByHalf():
    glTranslatef(7.0, 7.0, 7.0) # translate the cube back to its original position (7,7,7)
    glScalef(0.5, 0.5, 0.5) # uniformly scaling the cube by half at the origin
    glTranslatef(-7.0, -7.0, -7.0) # translate the cube to the origin to prepare for scaling
    return

def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - Michelle Zhang')                      # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100.0)                        # specify perspective projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, -1, 0, 1, 0)
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)

    scaleByHalf() # calling scaleByHalf() (Q2)

    angle = 1.0 # able to initialize to any angle, must be positive to rotate counterclockwise

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        draw() # function to draw the object
        spinningTransform(angle) # calling spinningTransform() (Q1)

        # below are the code irrelevant to the assignment
        glPushMatrix()
        glLoadMatrixf(initmodelMatrix)
        drawAxes()
        drawRotationAxis()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

main()