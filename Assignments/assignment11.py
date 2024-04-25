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

# TODO: Question 1
def draw_cube():
    # TODO: Construct the cube using an Indexed Triangles mesh representation
    # 8 vertices
    vertices = [ 

    ]

    # 12 triangles
    triangles = [

    ]
    
    # 12 edges
    edges = [

    ]
    
    # TODO: draw all the 12 triangles using GL_TRIANGLES
    # resotre the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [

    ]
 


    # TODO: draw all the 12 edges in white with a line width of 5 using GL_LINES




    return

# TODO: Question 2
def draw_pyramid():
    # TODO: Construct the pyramid using an Indexed Triangles mesh representation
    # 5 vertices
    vertices = [

    ]

    # 6 triangles
    triangles = [

    ]

    # 8 edges
    edges = [

    ]

    # TODO: draw all the 6 triangles using GL_TRIANGLES
    # resotre the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [

    ]



    # TODO: draw all the 8 edges in white with a line width of 5 using GL_LINES




    return

def draw():
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    glEnable(GL_CULL_FACE)                                                  # enable front/back face culling
    glCullFace(GL_BACK)                                                     # specify which face NOT drawing (culling)
    
    #TODO: write your code for Q1 inside draw_cube()
    draw_cube()

    #TODO: write your code for Q2 inside draw_pyramid()
    draw_pyramid()


def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - YOUR NAME')                      # set title of the program window

    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    glOrtho(-40, 40, -30, 30, 10, 80)                                       # specify an orthogonal-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)                                   # set camera's eye, look-at, and view-up in the world
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)
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

        # reset the current model-view back to the initial matrix
        if (bResetModelMatrix):
            glLoadMatrixf(initmodelMatrix)
        
        draw()
        drawAxes()

        pygame.display.flip()
        pygame.time.wait(10)

main()