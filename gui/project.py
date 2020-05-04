from tkinter import *
from tkinter.messagebox import *
from heapq import *

class Project(object):
 
    def __init__(self):
        #   param   #
        self.row, self.column = 15, 15
        self.mesh = 25
        self.ratio = 0.9
        self.step = self.mesh / 2
        self.vertex_r = self.step * self.ratio
        self.board_color = "#ffffff"
        self.header_bg = "#ffffff" 
        self.matrix = [[0 for y in range(self.column)] for x in range(self.row)]
        self.alphaCur = 0
        self.edgeCur = 0
        self.clickState = True
        self.verDict = {0:[0,0]}#coor X & coor Y
        self.start = False
        self.testCase = 1
        #    GUI     #
        self.root = Tk()
        self.root.title("Project")
        self.root.resizable(width=False, height=False)
        print("Discrbition: ")
        print("Computer project of Discreate Math II in 2020 Spring: ")
        print("PROJECT 5: create algorithm to determine the shortest ")
        print("path between two vertices in a weighted grapgh ")
        print("By Zhan Zeqiye, Zhusubaliev Amangeldi, Imanalieva Kanykei")
        # Create header zone
        self.f_headerFir = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.f_headerFir.pack(fill=BOTH, ipadx=10)
        self.f_headerSec = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.f_headerSec.pack(fill=BOTH, ipadx=10)
        self.f_headerThi = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.f_headerThi.pack(fill=BOTH, ipadx=10)
        self.f_headerFou = Frame(self.root, highlightthickness=0, bg=self.header_bg)
        self.f_headerFou.pack(fill=BOTH, ipadx=10)
        # First header
        self.l_state = Label(self.f_headerFir,width = 50,text = 'Please enter the number of vertices(Maximum 26)',bg = 'white')
        self.l_state.pack()
        # Second header
        self.l_vertices = Label(self.f_headerSec,width = 20,text = 'Number of vertices: ',bg = 'white')
        self.e_numVertices = Entry(self.f_headerSec,width = 5)
        self.b_confirmVertices = Button(self.f_headerSec, text="Confirm",command = self.getNumVertices)
        self.l_vertices.pack(side=LEFT)
        self.e_numVertices.pack(side=LEFT, padx=1)
        self.b_confirmVertices.pack(side=LEFT, padx=10)
        
        self.l_edges = Label(self.f_headerSec,width = 20,text = 'Number of Edges: ',bg = 'white')
        self.e_numEdges = Entry(self.f_headerSec,width = 5)
        self.b_confirmEdges = Button(self.f_headerSec, text="Confirm",command = self.getNumEdges, state=DISABLED)
        self.l_edges.pack(side=LEFT)
        self.e_numEdges.pack(side=LEFT, padx=1)
        self.b_confirmEdges.pack(side=LEFT, padx=10)
        # Third header
        self.l_vertexA = Label(self.f_headerThi,width = 10, text="First vertex:", bg = 'white')
        self.l_vertexB = Label(self.f_headerThi,width = 15, text="Second vertex:", bg = 'white')
        self.l_weightVertices = Label(self.f_headerThi,width = 20, text="Weight of edge(1-999):", bg = 'white')
        self.e_vertexAEnter = Entry(self.f_headerThi,width = 5)
        self.e_vertexBEnter = Entry(self.f_headerThi,width = 5)
        self.e_weightEnter = Entry(self.f_headerThi,width = 5)
        self.l_vertexA.pack(side=LEFT)
        self.e_vertexAEnter.pack(side=LEFT, padx=10)
        self.l_vertexB.pack(side=LEFT, padx=0)
        self.e_vertexBEnter.pack(side=LEFT,padx=0)
        self.l_weightVertices.pack(side=LEFT, padx=0)
        self.e_weightEnter.pack(side=LEFT,padx=0)
        # Fourth header
        self.b_create = Button(self.f_headerFou, text="Create edge between two vertices", command = self.draw_edge, state=DISABLED)
        self.b_find = Button(self.f_headerFou, text="Find the shortest path between them", command = self.find_path, state=DISABLED)
        self.b_create.pack(side=LEFT, padx=20)
        self.b_find.pack(side=RIGHT)
        # Draw board and vertex
        self.c_vertex = Canvas(self.root, bg=self.board_color, width=(self.column + 1) * self.mesh,
                              height=(self.row + 1) * self.mesh, highlightthickness=0)
        self.draw_board()
        self.c_vertex.bind("<Button-1>", self.cf_board)
        self.c_vertex.pack()
 
        self.root.mainloop()
    # Algorithm about shortest path
    def dijkstra(self,src,dest,path):
        d = [-1] * int(self.e_numVertices.get())
        p = [None] * int(self.e_numVertices.get())
        d[src] = 0
        p[src] = [src,0]
        q = [(0, src)]
        while (q):
            v = heappop(q)[1]
            for i in self.store[v]:
                u = i[0]
                w = i[1]
                if d[u] == -1 or d[u] > d[v] + w:
                    d[u] = d[v] + w
                    p[u] = [v,w]
                    heappush(q, (d[u], u))
            
        dist = d[dest]
        if dist != -1:
            v = dest
            while v != src:
                path.append([[p[v][0],v], p[v][1]])
                v = p[v][0]
            path.reverse()
        return dist

    def getNumVertices(self):
        if self.e_numVertices.get() == '':
            return
        listLengh = 0
        if self.e_numVertices.get() != '':
            listLengh = int(self.e_numVertices.get())
        if listLengh > 26:
            listLengh = 26
        self.alphaList = [i for i in range(1, listLengh + 1)]
        self.l_state.config(text = ('Please click the coordinate of vertex ',self.alphaList[self.alphaCur]))
        # Change the state of buttons
        self.b_confirmVertices.config(state=DISABLED)
        # Make the click function NORMAL
        self.start = True
        # Algorithm param
        self.store = [[] for _ in range (0, int(self.e_numVertices.get()))]

    def getNumEdges(self):
        if self.e_numEdges.get() == '':
            return
        self.b_confirmEdges.config(state=DISABLED)
        self.b_create.config(state=NORMAL)
        self.l_state.config(text = 'Please enter the target vertices and create edge')
        

    # Function of click
    def cf_board(self, e):
        if self.clickState == False or self.e_numVertices.get() == '' or not self.start:
            return
        x, y = int((e.y - self.step) / self.mesh), int((e.x - self.step) / self.mesh)
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        distance = ((center_x - e.y) ** 2 + (center_y - e.x) ** 2) ** 0.5
        #If the distance is not within the specified circle, exit // If there is already a piece at this position, exit
        if distance > self.step * 0.95 or self.matrix[x][y] != 0:
            return
        # change the tag of matrix from 0 to 1
        tag = 1;
        self.draw_vertex(x, y)
        self.matrix[x][y] = tag
        if self.clickState == True:
            self.l_state.config(text = ('Please click the coordinate of vertex ', self.alphaList[self.alphaCur]))

    # Draw the vertex and alphabet
    def draw_vertex(self, x, y):
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        self.c_vertex.create_oval(center_y - self.vertex_r, center_x - self.vertex_r,
                                 center_y + self.vertex_r, center_x + self.vertex_r,
                                 fill="white")
        alphaX, alphaY=center_y + 68,center_x+95
        # add the coordinate of vertext to dict in order to get coordinate of create_line
        self.verDict[self.alphaList[self.alphaCur]] = [center_y,center_x]
        self.l_alphabet = Label(width = 1, text=self.alphaList[self.alphaCur], bg = 'white').place(x=alphaX,y=alphaY)
        self.alphaCur += 1
        # check
        if self.e_numVertices.get() != '':
            if self.alphaCur == int(self.e_numVertices.get()):
                self.clickState = False
                self.alphaCur -= 1
                self.l_state.config(text = 'Please enter the number of edges')
                self.b_confirmEdges.config(state=NORMAL)

    def draw_edge(self):
        if self.edgeCur >= int(self.e_numEdges.get()):
            return
        a = self.e_vertexAEnter.get()
        b = self.e_vertexBEnter.get()
        w = self.e_weightEnter.get()
        # check a,b,w are legal
        if a=='' or b=='' or not self.checkVertexInDict(int(a)) or not self.checkVertexInDict(int(b)) or int(a) <= 0 or int(b) <= 0 or w == '' or not w.isdigit() or int(w)>=1000 or int(w) <=0:
            self.l_state.config(text = 'Please enter the legal value')
            return
        # get coordinate of line from dict
        alist = self.verDict[int(a)]
        blist = self.verDict[int(b)]
        self.c_vertex.create_line(alist[0],alist[1],blist[0],blist[1])
        # store vertex and weight into store of algo
        self.edgeCur += 1
        x = int(a) - 1
        y = int(b) - 1
        self.store[x].append([y,int(w)])
        self.store[y].append([x,int(w)])

        if self.edgeCur >= int(self.e_numEdges.get()):
            self.l_state.config(text = 'Now you can choose two vertices and find the shortest path')
            self.b_create.config(state=DISABLED)
            self.b_find.config(state=NORMAL)

    def checkVertexInDict(self,num):
        for key in self.verDict:
            if num == key:
                return True
        return False

    def find_path(self):
        src = int(self.e_vertexAEnter.get()) - 1
        dest = int(self.e_vertexBEnter.get()) - 1
        path = []
        dist = self.dijkstra(src,dest,path)
        print('Test case: ',self.testCase)
        self.testCase += 1
        if dist == -1:
            print('There is no any path from vertex %d to vertex %d' %(src + 1, dest + 1))
        else:
            print('Shortest path from %d to %d has a total weights %d and consists of %d edges:' %(src + 1, dest + 1, dist, len(path)) )
            for i in path :
                print('vertex %d to vertex %d, weight: %d'%(i[0][0] + 1, i[0][1] + 1, i[1]))

 
    def draw_board(self):
        [self.draw_mesh(x, y) for y in range(self.column) for x in range(self.row)] 

    def draw_mesh(self, x, y):
        ratio = (1 - self.ratio) * 0.99 + 1
        center_x, center_y = self.mesh * (x + 1), self.mesh * (y + 1)
        self.c_vertex.create_rectangle(center_y - self.step, center_x - self.step,
                                      center_y + self.step, center_x + self.step,
                                      fill=self.board_color, outline=self.board_color)
        a, b = [0, ratio] if y == 0 else [-ratio, 0] if y == self.row - 1 else [-ratio, ratio]
        c, d = [0, ratio] if x == 0 else [-ratio, 0] if x == self.column - 1 else [-ratio, ratio]
        self.c_vertex.create_line(center_y + a * self.step, center_x, center_y + b * self.step, center_x)
        self.c_vertex.create_line(center_y, center_x + c * self.step, center_y, center_x + d * self.step)
 
if __name__ == '__main__':
    Project()