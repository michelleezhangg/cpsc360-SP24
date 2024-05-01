import os
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 800, 600                                                    # width and height of the screen created

# cross product
def cross(a, b):
    c = (a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0])

    return c

# Function to load the mesh from an OBJ file
def loadOBJ(filename):
    vertices = []
    normals = []
    faces = []
    with open(filename, "r") as file:
        for line in file:
            if line.startswith('v '):
                _, x, y, z = line.split()
                vertices.append((float(x), float(y), float(z)))
            elif line.startswith('vn '):
                _, nx, ny, nz = line.split()
                normals.append((float(nx), float(ny), float(nz)))
            elif line.startswith('f '):
                face = line.split()[1:]
                faces.append((int(face[0].split('//')[0]) - 1,
                              int(face[1].split('//')[0]) - 1,
                              int(face[2].split('//')[0]) - 1))
    return vertices, normals, faces

def drawAxes(bEnableLighting = False):                                      # draw x-axis and y-axis
    # Disable lighting for the axes so that their colors are vivid
    glDisable(GL_LIGHTING)
   
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

    # Re-enable lighting if it was enabled before
    if bEnableLighting == True:
        glEnable(GL_LIGHTING)    

# Function to draw the loaded mesh
def drawMesh(vertices, normals, faces, shading = 'Flat'):
    glPushMatrix()
    glScalef(100.0, 100.0, 100.0)
 
    if shading == 'Gouraud':
        glShadeModel(GL_SMOOTH)
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glNormal3fv(normals[vertex])
                glVertex3fv(vertices[vertex])
        glEnd()
    elif shading == 'Flat':
        glShadeModel(GL_FLAT)
        glBegin(GL_TRIANGLES)
        for face in faces:
            # calculate normal vector of the current triangle (face)
                # based on 3 vertices of the triangle
            v0 = vertices[face[0]]
            v1 = vertices[face[1]]
            v2 = vertices[face[2]]
            edge01 = (v1[0] - v0[0], v1[1] - v0[1], v1[2] - v0[2])
            edge02 = (v2[0] - v0[0], v2[1] - v0[1], v2[2] - v0[2]) 
            normal_face = cross(edge01, edge02)
            glNormal3fv(normal_face)
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()
    elif shading == 'None':
        glColor3f(1.0, 1.0, 0.0) # yellow
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertices[vertex])
        glEnd()

    glPopMatrix()

def setupLighting():
    glEnable(GL_NORMALIZE)
    glEnable(GL_DEPTH_TEST)  # Enable depth testing for proper occlusion

    lightPosition = (20, 20, 20, 1)    # point light (1) / direction light (0), position(20, 20, 20)
    lightDiffuse = (1, 1, 1, 1)        # diffuse color: white
    lightSpecular = (1, 1, 1, 1)       # specular color: white
    lightAmbient = (0.1, 0.1, 0.1, 1)  # Ambient light set to a low grey to simulate global illumination

    glLightfv(GL_LIGHT0, GL_POSITION, lightPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightDiffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular)
    glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbient)
    glEnable(GL_LIGHT0)

    # Set material properties to render the mesh in yellow with some specular highlights
    ambient = (0.3, 0.3, 0.3, 1.0)  # low ambinet reflection
    diffuse = (1.0, 1.0, 0.0, 1.0)  # RGBA for yellow
    specular = (0.9, 0.9, 0.9, 1.0)  # high specular reflection
    shininess = 128.0  # High shininess for a shiny surface

    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, ambient)
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, diffuse)
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specular)
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, shininess)  # Specular highlight (shininess)



def main():
    pygame.init()                                                           # initialize a pygame program
    glutInit()                                                              # initialize glut library 

    screen = (width, height)                                                # specify the screen size of the new program window
    display_surface = pygame.display.set_mode(screen, DOUBLEBUF | OPENGL)   # create a display of size 'screen', use double-buffers and OpenGL
    pygame.display.set_caption('CPSC 360 - Lighting')      # set title of the program window

    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)                                             # set mode to projection transformation
    glLoadIdentity()                                                        # reset transf matrix to an identity
    gluPerspective(45, (width / height), 0.1, 100)                          # specify perspective-projection view volume

    glMatrixMode(GL_MODELVIEW)                                              # set mode to modelview (geometric + view transf)
    gluLookAt(0, 0, 50, 0, 0, 0, 0, 1, 0)                                   # set camera's eye, look-at, and view-up in the world
    initmodelMatrix = glGetFloat(GL_MODELVIEW_MATRIX)

    # Enable lighting for surface rendering
    bEnableLighting = True
    if bEnableLighting == True:
        glEnable(GL_LIGHTING)
        setupLighting()
    
    # load the mesh
    model_name = 'bunny_n.obj'
    dir_path = os.path.dirname(os.path.realpath(__file__))
    model_path = dir_path + '/' + model_name 
    print(model_path)
    # NOTE: only enable the line below when you've downloaded 'bunny_n.obj'
        # into the same folder of this Python file
    #vertices, normals, faces = loadOBJ(model_path)

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
        
        glClearColor(0, 0, 0, 1)                                                # set background RGBA color 
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)                        # clear the buffers initialized in the display mode
    
        if bEnableLighting == True:
            shading = 'Flat' # set it as 'Gouraud' (GL_SMOOTH) or 'Flat' (GL_FLAT)
        else:
            shading = 'None'

        # render imported mesh
        # NOTE: only enable the line below when you've downloaded 'bunny_n.obj'
            # into the same folder of this Python file
        #drawMesh(vertices=vertices, normals= normals, faces=faces, shading=shading)

        # render a sphere
        if shading == 'Flat':
            glShadeModel(GL_FLAT)
        elif shading == 'Gouraud':
            glShadeModel(GL_SMOOTH)
        elif shading == 'None':
            glColor3f(1.0, 1.0, 0.0)
        quad = gluNewQuadric()
        gluSphere(quad,5,20,20)

        # draw x, y, z axes
        drawAxes(bEnableLighting=bEnableLighting)

        pygame.display.flip()
        pygame.time.wait(10)

main()