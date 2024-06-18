import sys


class ShortestPathAnd2ndShortestDijkstras:
    # Stolen from thw world wide webb
    def __init__(self):
        self.NO_PARENT = -1
        self.path = []  # nodes in the shortest path
        self.allDists = []  # list of shortest distance, keep insertion order

    # use Dijkstra’s Shortest Path Algorithm, Time O(n^2)  n is number of nodes
    # auxillary Space O(n)
    def shortestPath(self, adjacencyMatrix, src, dest):
        n = len(adjacencyMatrix[0])
        shortest = {}  # Dict med kortaste avstånd till respektive nod
        visited = {}  # Dict med True/False om noden är "visited"
        parents = {}
        for v in range(0, n, 1):
            shortest[v] = sys.maxsize
            visited[v] = False
        shortest[src] = 0
        parents[src] = self.NO_PARENT
        # Loopar över längden på matrisen, dvs alla noder
        for i in range(1, n, 1):
            pre = -1
            # Initialvärde
            min = sys.maxsize
            # Vikt för nod
            for v in range(0, n, 1):
                if not visited[v] and shortest[v] < min:
                    # Vi kollar efter nod som ej är behandlad med som det är kortast avstånd till
                    # Den noden blir "pre" och "min" är avståndet dit
                    pre = v
                    min = shortest[v]
            if pre == -1:
                return
            visited[pre] = True  # Sätt noden som "besökt"

            for v in range(
                0, n, 1
            ):  # Gå igenom noder och kolla avståndet till närliggande noder, 0 betyder "ingen connection"
                dist = adjacencyMatrix[pre][v]
                if dist != 0 and (
                    (min + dist) < shortest[v]
                ):  # Om avståndet är större än 0 och vi hittat en kortare väg till aktuell nod: sätt denna som föregående nod
                    parents[v] = pre
                    shortest[v] = min + dist
        self.allDists.append(shortest[dest])
        self.addPath(dest, parents)

    # utility func to add nodes in the path recursively
    # Time O(n), Space O(n)
    def addPath(self, i, parents):
        if i == self.NO_PARENT:
            return
        self.addPath(parents[i], parents)
        self.path.append(i)

    # get 2nd shortest by removing each edge in shortest and compare
    # Time O(n^3), Space O(n)
    def find2ndShortest(self, adjacencyMatrix, src, dest):
        # store previous vertex's data
        preV = -1
        preS = -1
        preD = -1
        mylist = list(self.path)
        for i in range(0, len(mylist) - 1, 1):
            # get source and destination for each path in shortest path
            s = mylist[i]
            d = mylist[i + 1]
            # resume the previous path
            if preV != -1:
                adjacencyMatrix[preS][preD] = preV
                adjacencyMatrix[preD][preS] = preV
            # record the previous data for recovery
            preV = adjacencyMatrix[s][d]
            preS = s
            preD = d
            # remove this path
            adjacencyMatrix[s][d] = 0
            adjacencyMatrix[d][s] = 0
            # re-calculate
            self.shortestPath(adjacencyMatrix, src, dest)


#
#      0
#   10/ \3
#    /   \
#   1--1--4
#  5|  8/ |2
#   | /   |
#   2--7--3
#
"""adjacencyMatrix = [
            [ 0,10, 0, 0, 3 ],
            [ 10, 0, 5, 0, 1 ],
            [ 0, 5, 0, 7, 8 ],
            [ 0, 0, 7, 0, 2 ],
            [ 3, 1, 8, 2, 0 ]
]
src = 2
dest = 4
myobj = ShortestPathAnd2ndShortestDijkstras()
myobj.shortestPath(adjacencyMatrix, src, dest);
myobj.find2ndShortest(adjacencyMatrix, src, dest);
print("Shortest distance: " + str(myobj.allDists[0]))
print("2nd shortest distance: " + str(myobj.allDists[1]))"""
