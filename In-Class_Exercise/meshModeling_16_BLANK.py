import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

## mesh data structure
vertices = [
    [-20.0, -10.0, 1.0],    #v0
    [-10.0, 10.0, 1.0],     #v1
    [0.0, -10.0, 1.0],      #v2
    [10.0, 10.0, 1.0],      #v3
    [20.0, -10.0, 1.0]      #v4
]

edges = [
    [0, 1],                 #v0, v1
    [1, 2],                 #v1, v2
    [2, 3],                 #v2, v3
    [3, 4],                 #v3, v4
    [0, 2],                 #v0, v2
    [2, 4],                 #v2, v4
    [1, 3]                  #v1, v3
]

triangles = [
    [0, 1, 2],              #v0-v1-v2
    [1, 2, 3],              #v1-v2-v3
    [2, 3, 4]               #v2-v3-v4
]

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

def draw_vertices():
    glColor3f(1.0, 1.0, 1.0)                                                # specify vertex color (r,g,b), white
    glPointSize(10.0)                                                       # specify point size
    glBegin(GL_POINTS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def draw_edges():
    glColor3f(1.0, 1.0, 1.0)
    glLineWidth(5.0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def draw_triangles():                                                       
    #glEnable(GL_CULL_FACE)                                                # enable front/back face culling
    #glCullFace(GL_BACK)                                                   # specify which face NOT drawing (culling)
    colors = ((1.0,0.0,0.0),(0.0,1.0,0.0),(0.0,0.0,1.0))                   # [red, green, blue]
    tri_idx = 0
    glBegin(GL_TRIANGLES)
    for triangle in triangles:
        glColor3fv(colors[tri_idx])                                        # draw each triangle with a diff color 
        for vertex in triangle:
            glVertex3fv(vertices[vertex])
        tri_idx += 1
    glEnd()

def draw_triangleStrips():
    glColor3f(0.0, 1.0, 0.0)
    triangle_strip = [] #TODO: Fill this up to draw triangle strips

    # create a list of colors for all the vertices in 'vertices'
    colors = ((1.0,0.0,0.0), # red
              (1.0,1.0,0.0), # yellow
              (0.0,1.0,0.0), # green
              (0.0,1.0,1.0), # turquoise
              (0.0,0.0,1.0)) # blue

    glBegin(GL_TRIANGLE_STRIP)
    for vertex in triangle_strip:
        glColor3fv(colors[vertex])                                         # assign a color to each vertex
        glVertex3fv(vertices[vertex])
    glEnd()

def draw_triangleFans():
    triangle_fan = [] #TODO: Fill this up to draw triangle fans

    # create a list of colors for all the vertices in 'vertices'
    colors = ((1.0,0.0,0.0), # red
              (1.0,1.0,0.0), # yellow
              (0.0,1.0,0.0), # green
              (0.0,1.0,1.0), # turquoise
              (0.0,0.0,1.0)) # blue

    glBegin(GL_TRIANGLE_FAN)
    for vertex in triangle_fan:
        glColor3fv(colors[vertex])                                         # assign a color to each vertex
        glVertex3fv(vertices[vertex])
    glEnd()

# In-Class Exercise 1: Please refer to Exercise 1 in Lecture 15
def exercise1_TriangleStrips():
    # TODO: create a vertex array (a list of lists)
    vertices_e1 = [

    ]

    # TODO: fill up the list triangle strip (a list)
    triangleStrip_e1 = []

    # TODO: draw triangle strips first using glBegin(GL_TRIANGLE_STRIP)-glEnd()
        # all triangle are in blue, first specify the triangle color as BLUE using glColor3f()



    # TODO: fill up the list for all the 9 edges (a list of lists)
    edges_e1 = [

    ]

    # TODO: draw triangle edges at last using glBegin(GL_LINES)-glEnd()
        # specify the edge color using glColor3f() with (1.0, 1.0. 1.0) indicating white color
        # specify the line width using glLineWidth() with 3.0 as length width


    return

# In-Class Exercise 2: Please refer to Exercise 2 in Lecture 15
def exercise2_TriangleFans():
    # TODO: create a vertex array (a list of lists)
    vertices_e2 = [

    ]

    # TODO: fill up the list for the triangle strip (a list)
    triangleFan_e2 = []

    # TODO: fill up the colors for vertices a, b, c, d: red, yellow, green, blue
        # a tuple of tuples: ((), (), ...)
    colors_e2 = (

    ) 


    # TODO: draw triangle fan first using glBegin(GL_TRIANGLE_FAN)-glEnd()
        # assign each vertex color in the for loop



    # TODO: fill up the list for all the 6 edges (a list of lists)
    edges_e2 = [
  
    ]

    # TODO: draw triangle edges at last using glBegin(GL_LINES)-glEnd()
        # specify the edge color using glColor3f() with (1.0, 1.0. 1.0) indicating white color
        # specify the line width using glLineWidth() with 3.0 as length width


    return



def draw():
    glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    
    #TODO: draw triangle fans
    #draw_triangleFans()

    #TODO: draw triangle strips
    #draw_triangleStrips()
    
    # draw triangles
    #draw_triangles()
    
    # draw edges (line-segments)
    #draw_edges()
    
    # draw vertices
    draw_vertices()

    # TODO: Exercise 1: Draw Triangle Strips
        # please commend out all the above functions first
    #exercise1_TriangleStrips()

    # TODO: Exercise 2: Draw Triangle Fans
        # please commend out all the above functions first
    #exercise2_TriangleFans()


def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - OpenGL Modeling')                # set title of the program window

    #glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100)                          # specify perspective-projection view volume

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