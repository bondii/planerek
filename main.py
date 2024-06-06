from scripts.calculate_route import calculate_route
from scripts.shortest_way import ShortestPathAnd2ndShortestDijkstras
from tests.validate_nodes_and_routes import validate_nodes_and_maps


def main():
    # calculate_route("EC_1", "AB_3", "CC_4")
    adjacencyMatrix = [
        [0, 10, 0, 0, 3],
        [10, 0, 5, 0, 1],
        [0, 5, 0, 7, 8],
        [0, 0, 7, 0, 2],
        [3, 1, 8, 2, 0],
    ]
    src = 2
    dest = 0
    myobj = ShortestPathAnd2ndShortestDijkstras()
    myobj.shortestPath(adjacencyMatrix, src, dest, 3)
    test = 3


if __name__ == "__main__":
    main()
