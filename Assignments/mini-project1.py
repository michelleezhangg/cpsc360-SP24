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
    glColor3f(0.0, 0.0, 1.0)                                                # z-axis: blue
    glVertex3f(0.0, 0.0, 0.0)                                               # v0
    glVertex3f(0.0, 0.0, 100.0)                                             # v1
    glEnd()

# For Mini-project 1:
# TODO: 1) Create a scarecrow as instructed and 2) Constantly rotate head and nose ONLY
def draw_Scarecrow():                                                  # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode

    # configure quatratic drawing
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_FILL)  

    # TODO: Head (sphere: radius=2.5) 
    glColor3f(0.0, 1.0, 0.0)
    gluSphere(quadratic, 2.5, 32, 32)

    # TODO: Nose (cylinder: base-radius=0.3, top-radius=0, length=2)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 0.3, 0.0, 1.8, 32, 32)  

    # TODO: Torso (cylinder: radius=2.5, length=10)
    glColor3f(1.0, 1.0, 0.0)
    gluCylinder(quadratic, 2.5, 2.5, 10.0, 32, 32)

    # TODO: Left Leg (cylinders: radius=1.0, length=12)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)

    # TODO: Right Leg (cylinders: radius=1.0, length=12)
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)

    # TODO: Left Arm (cylinders: radius=1.0, length=10)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)

    # TODO: Right Arm (cylinders: radius=1.0, length=10)
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)

def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - YOUR NAME')                      # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100.0)                        # specify perspective projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, -1, 0, 1, 0)
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)

    while True:
        bResetModelMatrix = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:
                    glRotatef(event.rel[1], 1, 0, 0)
                    glRotatef(event.rel[0], 0, 1, 0)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    bResetModelMatrix = True
        
        # ONLY write your code inside the function below 
        #   You don't need to modify any other code in this file.
        draw_Scarecrow()

        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)

        # draw x, y, z axes without involving any transformations
        glPushMatrix()
        glLoadMatrixf(initmodelMatrix)
        drawAxes()
        glPopMatrix()
        pygame.display.flip()
        pygame.time.wait(10)

main()