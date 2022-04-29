
# 
# For this assignment you will need to use a popular and powerful library known as [OpenCV](https://opencv.org/). To do this on hub, you will need to open a terminal (File->New Launcher->Terminal) and enter `pip install opencv-python`. If you are trying to run the notebook somewhere else and can't figure out how to install the library, ask on piazza and provide details.

from matplotlib import pyplot as plt
import cv2
import numpy as np 
import heapdict

def fixPixelValues(px):
    # convert the RGB values into floating point to avoid an overflow that will give me wrong answers
    return [ float(px[0]), float(px[1]), float(px[2]) ]

## Given (x,y) coordinates of two neighboring pixels, calculate the edge weight.
# We take the squared euclidean distance between the pixel values and add 0.1
def getEdgeWeight(img, u, v):
    # get edge weight for edge between u, v
    # First make sure that the edge is legit
    i0,j0 = u.x, u.y
    i1,j1 = v.x, v.y
    height, width, _ = img.shape
    assert i0 >= 0 and j0 >= 0 and i0 < width and j0 < height # pixel position valid?
    assert i1 >= 0 and j1 >= 0 and i1 < width and j1 < height # pixel position valid?
    assert -1 <= i0 - i1 <= 1 # edge between node and neighbor?
    assert -1 <= j0 - j1 <= 1
    px1 = fixPixelValues(img[j0,i0])
    px2 = fixPixelValues(img[j1,i1])
    return 0.1 + (px1[0] - px2[0])**2 + (px1[1] - px2[1])**2 + (px1[2]- px2[2])**2
    
# This is a useful function that given a list of (x,y) values, 
# draw a series of red lines between each coordinate and next to 
# show the path in the image
def drawPath(img, path, pThick=2):
    v = path[0]
    x0, y0 = v[0], v[1]
    for v in path:
        x, y = v[0], v[1]
        cv2.line(img,(x,y), (x0,y0), (255,0,0),pThick)
        x0, y0 = x,y
        

#img = cv2.imread('maze.png') # read an image from a file using opencv (cv2) library
#drawPath(img, [ (15, 15), (150, 15), (150, 85), (75, 85), (75, 195)])
#plt.imshow(img) # show the image on the screen 
#plt.title('Illustration of drawPath')
#plt.show()

# ## Step 1: Compute Single Source Shortest Path For an Image
# 
# Given an image, compute the  shortest path between source and destination pixels by modifying Dijkstra's algorithm. __Your challenge  is to implement it without needing to create the entire the adjacency list for the graph
# in the first place. However, for simplicity you can try a first cut implementation of a generic Dijkstra algorithm over
# graphs represented as adjacency matrix or list.__ 


class Vertex: # This is the outline for a vertex data structure
    def __init__ (self,  i, j):
        self.x = i # The x coordinate
        self.y = j  # The y coordinate
        self.d = float('inf') # the shortest path estimate
        self.visited = False # Has this vertex's final shortest path distance been computed
        self.idx_in_priority_queue = -1 # The index of this vertex in the queue
        self.pi = None # the parent vertex.
    
        

# However, if you want Dijkstra efficiently, 
# you may want to implement a priority queue.
# We provide you the signature for a priority queue.
# Feel free to implement extra functions if you wish


class PriorityQ:
    # Constructor: 
    def __init__(self):
        self.pq = heapdict.heapdict()
    
    def insert(self, v):
        v_coordinates = "(" + str(v.x) + ", " + str(v.y) + ")"
        self.pq[v_coordinates] = v.d
    
    def get_and_delete_min(self, vertices_table):
        min_coordinates = self.pq.get()
        min_x = int(min_coordinates[1])
        min_y = int(min_coordinates[4])

        return vertices_table[min_y, min_x]

    def is_empty(self):
        try: 
            self.pq.peekitem()
            return True
        except:
            return False
        
    def update_vertex_weight(self, v):
        self.insert(v)
        

def createVertices(img) :
    # get image width and height
    shape  = img.shape
    height = shape[0] # y - rows
    width = shape[1] # x - columns
    vertex_table = np.empty((height, width), dtype=Vertex)

    for j in range(height) :
        for i in range(width) :
            vertex_table[j, i] = Vertex(i, j)

    return vertex_table
            

def relax(img, u, v) :
    w = getEdgeWeight(img, u, v)

    # if the current distance estimate is bigger
    # than the distance to u, then we update it
    # with the new smaller distance through node u
    if v.d > u.d + w :
        v.d = u.d + w
        v.pi = u
        return True # relax successful
    else :
        return False # we weren't able to relax


def makeVertexPQ(vertex_table):
    q = PriorityQ()
    
    for j in range(vertex_table.shape[0]) : # y - rows
        for i in range(vertex_table.shape[1]) : # x - columns
            q.insert(vertex_table[j, i]) # goes in [y, x]

    assert(len(q.pq) == np.size(vertex_table))

    return q


def getPath(vertex_table, source, dest) :
    assert(vertex_table[dest[1], dest[0]].visited == True) # make sure destination has been fully processed 
    curr_pos = dest
    path = []
    count = 0

    # go backwards starting at the destination and find the path following parent nodes
    while curr_pos != source and count < vertex_table.shape[0]*vertex_table.shape[1]:
        path.append(curr_pos)
        parent = vertex_table[curr_pos[1], curr_pos[0]].pi  # goes in [y, x]
        assert(parent is not None)
        curr_pos = (parent.x, parent.y)
        count += 1

    path.append(source)
    print(path)

    return path


def computeShortestPath(img, source, dest): 
    # make table of vertices aka pixels
    vertex_table = createVertices(img)
    vertex_table[source[1], source[0]].d = 0

    q = makeVertexPQ(vertex_table)


    while q.is_empty() != True :
        u = q.get_and_delete_min()

        #for nodes adjacent to u :
        for i in range(u.x-1, u.x+2) :
            for j in range(u.y-1, u.y+2) :
                if i >= 0 and j >= 0 and i < img.shape[1] and j < img.shape[0] :
                    v = vertex_table[j, i]

                    if v.visited == False :
                        relax_success = relax(img, u, v)
                        if relax_success :
                            q.update_vertex_weight(v)

        u.visited = True

        if u.x == dest[0] and u.y == dest[1] : # we've found the shortest path to the destination
            break
        

    path = getPath(vertex_table, source, dest)

    return path



