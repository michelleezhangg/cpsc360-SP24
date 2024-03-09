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
angle = 0 # global variable for the angle of rotation

def draw_Scarecrow():                                                  # This is the drawing function drawing all graphics (defined by you)
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode

    # configure quatratic drawing
    quadratic = gluNewQuadric()
    gluQuadricDrawStyle(quadratic, GLU_FILL)  

    # head
    glPushMatrix()
    glTranslatef(0.0, 12.5, 0.0) # translated sphere up 12.5 units +y-axis
    glColor3f(0.0, 1.0, 0.0)
    gluSphere(quadratic, 2.5, 32, 32)
    glPopMatrix()

    # nose
    glPushMatrix()
    glTranslatef(0.0, 12.5, 2.5) # translated the nose up 12.5 units +y-axis and out 2.5 units +z-axis
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 0.3, 0.0, 1.8, 32, 32)
    glPopMatrix()

    # torso
    glPushMatrix()
    glRotatef(-90.0, 1.0, 0.0, 0.0) # rotated the torso around the x-axis by 90 degrees clockwise
    glColor3f(1.0, 1.0, 0.0)
    gluCylinder(quadratic, 2.5, 2.5, 10.0, 32, 32)
    glPopMatrix()

    # left leg
    glPushMatrix()
    glTranslatef(-1.2, 0.0, 0.0) # then translated the leg to the left (-x-axis) by 1.2 units
    glRotatef(90.0, 1.0, 0.0, 0.0) # first rotated the leg 90 degrees counterclockwise around the x-axis
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # right leg
    glPushMatrix()
    glTranslatef(1.2, 0.0, 0.0) # then translated the leg to the right (+x-axis) by 1.2 units
    glRotatef(90.0, 1.0, 0.0, 0.0) # first rotated the leg 90 degrees counterclockwise around the x-axis
    glColor3f(1.0, 0.0, 0.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # left arm
    glPushMatrix()
    glTranslatef(2.4, 9.0, 0.0) # then translated the arm to the right (+x-axis) 2.4 units and up 9.0 units (+y-axis)
    glRotatef(90.0, 0.0, 1.0, 0.0) # first rotated the arm 90 degrees counterclockwise around the y-axis
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

    # right arm
    glPushMatrix()
    glTranslatef(-2.4, 9.0, 0.0) # then translated the arm to the left (-x-axis) 2.4 units and up 9.0 units (+y-axis)
    glRotatef(-90.0, 0.0, 1.0, 0.0) # first rotated the arm 90 degrees clockwise around the y-axis
    glColor3f(0.0, 0.0, 1.0)
    gluCylinder(quadratic, 1.0, 1.0, 12.0, 32, 32)
    glPopMatrix()

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