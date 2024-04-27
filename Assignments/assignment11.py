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
        [-10, -10, -10],    # v0
        [-10, -10, 10],     # v1
        [10, -10, 10],      # v2
        [10, -10, -10],     # v3
        [-10, 10, -10],     # v4
        [-10, 10, 10],      # v5
        [10, 10, 10],       # v6
        [10, 10, -10]       # v7
    ]

    # 12 triangles
    triangles = [
        # top face
        [4, 5, 6],          # v4-v5-v6
        [4, 6, 7],          # v4-v6-v7

        # front face
        [5, 1, 6],          # v5-v1-v6
        [2, 6, 1],          # v2-v6-v1

        # right face
        [6, 2, 7],          # v6-v2-v7
        [3, 7, 2],          # v3-v7-v2

        # back face
        [7, 3, 4],          # v7-v3-v4
        [0, 4, 3],          # v0-v4-v3

        # left face
        [4, 0, 5],          # v4-v0-v5
        [1, 5, 0],          # v1-v5-v0

        # bottom face
        [1, 0, 2],          # v1-v0-v2
        [3, 2, 0]           # v3-v2-v0
    ]
    
    # 12 edges
    edges = [
        [0, 1],             # v0-v1
        [0, 3],             # v0-v3
        [2, 3],             # v2-v3
        [1, 2],             # v1-v2
        [4, 5],             # v4-v5
        [4, 7],             # v4-v7
        [5, 6],             # v5-v6
        [6, 7],             # v6-v7
        [0, 4],             # v0-v4
        [1, 5],             # v1-v5
        [2, 6],             # v2-v6
        [3, 7]              # v3-v7
    ]
    
    # TODO: draw all the 12 triangles using GL_TRIANGLES
    # restore the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [
        # top face - green
        (0.0, 1.0, 0.0),
        (0.0, 1.0, 0.0),

        # front face - blue
        (0.0, 0.0, 1.0),
        (0.0, 0.0, 1.0),
    
        # right face - red
        (1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),

        # back face - blue
        (0.0, 0.0, 1.0),
        (0.0, 0.0, 1.0),

        # left face - red
        (1.0, 0.0, 0.0),
        (1.0, 0.0, 0.0),

        # bottom face - green
        (0.0, 1.0, 0.0),
        (0.0, 1.0, 0.0)
    ]

    tri_idx = 0
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3fv(colors[tri_idx]) 
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
        tri_idx += 1
    glEnd()

    # TODO: draw all the 12 edges in white with a line width of 5 using GL_LINES
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

    return

# TODO: Question 2
def draw_pyramid():
    # TODO: Construct the pyramid using an Indexed Triangles mesh representation
    # 5 vertices
    vertices = [
        [-10, 0, -10],      # v0
        [-10, 0, 10],       # v1
        [10, 0, 10],        # v2
        [10, 0, -10],       # v3
        [0, 20, 0]          # v4
    ]

    # 6 triangles
    triangles = [
        # left face
        [4, 0, 1],          # v4-v0-v1

        # front face
        [4, 1, 2],          # v4-v1-v2

        # right face
        [4, 2, 3],          # v4-v2-v3

        # back face
        [4, 3, 0],          # v4-v3-v0

        # bottom face
        [1, 0, 2],          # v1-v0-v2
        [3, 2, 0]           # v3-v2-v0
    ]

    # 8 edges
    edges = [
        [0, 1],             # v0-v1
        [1, 2],             # v1-v2
        [2, 3],             # v2-v3
        [3, 0],             # v3-v0
        [0, 4],             # v0-v4
        [1, 4],             # v1-v4
        [2, 4],             # v2-v4
        [3, 4]              # v3-v4
    ]

    # TODO: draw all the 6 triangles using GL_TRIANGLES
    # resotre the colors for all the faces in a list of tuples: [(r, g, b), (), ...]
    colors = [
        # left face - red
        (1.0, 0.0, 0.0),

        # front face - yellow
        (1.0, 1.0, 0.0),

        # right face - green
        (0.0, 1.0, 0.0),

        # back face - turquoise
        (0.0, 1.0, 1.0),

        # bottom face - blue
        (0.0, 0.0, 1.0),
        (0.0, 0.0, 1.0)
    ]

    tri_idx = 0
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3fv(colors[tri_idx])
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
        tri_idx += 1
    glEnd()

    # TODO: draw all the 8 edges in white with a line width of 5 using GL_LINES
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

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
    pygame.display.set_caption('CPSC 360 - Michelle Zhang')                      # set title of the program window

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