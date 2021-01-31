import numpy as np
import sys
from clock import Clock
from HTML_writer import numpy2html, create_html_page
import os


# Global Variables
t = Clock.Stopwatch()
path = []
len_path = 0
temp = 0
comp = {}


# Functions
def shortest_path(matrix, row=0):
    """

    :param matrix: A converted matrix from space array. This matrix gives the possible moves
                    from a cell to other cells.
    :param row: This is the row in converted matrix which show the starting cell.
                By default the starting point is (0, 0)
    :return: Bool
    """
    global len_path, temp, comp, path

    if temp != 0:
        if len_path > temp:
            return False
    if row == ending:
        path.append(str(row))
        ky = "-".join(path)
        comp[str(ky)] = len_path
        temp = len_path - 1
        path.remove(str(row))
        print(f"Path length: {len_path + 1}")
        return False
    if sum(matrix[row, :]) == 0:
        return False

    n = 0
    for weigh in matrix[row, :]:
        if weigh == 1 and str(n) not in path:
            path.append(str(row))
            len_path += weigh
            if shortest_path(matrix, n):
                return True
            len_path -= weigh
            path.remove(str(row))

        n += 1
    return False


if __name__ == '__main__':
    sys.setrecursionlimit(999999999)  # Max recursion limit

    starting_row = input("Enter starting row (numbering starts from 0-8): ")
    starting_column = input("Enter starting column (numbering starts from 0-8): ")
    ending_row = input("Enter ending row (numbering starts from 0-8): ")
    ending_column = input("Enter ending column (numbering starts from 0-8): ")

    # 1 for blocks that are used to move and -1 for restricted blocks
    space = np.array([[1, 1, -1, 1, 1, 1, 1, 1, 1],
                      [1, 1, -1, 1, -1, 1, 1, -1, 1],
                      [1, -1, -1, 1, -1, 1, -1, -1, 1],
                      [1, 1, 1, 1, 1, -1, -1, 1, 1],
                      [1, 1, 1, 1, -1, -1, 1, 1, 1],
                      [1, 1, 1, -1, -1, 1, 1, 1, 1],
                      [1, 1, -1, 1, 1, 1, 1, 1, 1],
                      [1, -1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1]], dtype='int32')
    
    original_space = numpy2html(space)
    print("Finding the shortest path .........................")

    # Connection between cells
    rows = len(space[0, :])
    columns = len(space[:, 0])
    connections = {}
    for i in range(rows):
        for j in range(columns):
            if space[i, j] == -1:
                continue
            else:
                pos_path = []
                for k, o in [[x, y] for x in range(-1, 2) for y in range(-1, 2)]:
                    #if [k, o] == [0, 0]:  # move in 8-directions
                     #   continue
                    if abs(k) == abs(o):  # move in 4-directions
                        continue
                    if rows > i + k >= 0 and columns > j + o >= 0:
                        if space[i + k, j + o] == -1:
                            continue
                        else:
                            pos_path.append(f"{i + k}.{j + o}")
                connections[f"{i}.{j}"] = pos_path

    # creating connection matrix
    con_matrix = np.zeros((len(connections.keys()), len(connections.keys())))

    # Reference each cell to a row
    ref = {}
    for i, key in enumerate(connections.keys()):
        ref[key] = i

    # Showing relation between cells in connection matrix
    for key in connections.keys():
        for val in connections[key]:
            con_matrix[ref[key], ref[val]] = 1

    # Inputs
    starting = ref[f"{starting_row}.{starting_column}"]
    ending = ref[f"{ending_row}.{ending_column}"]

    # Restricting the return to starting point
    t.start()
    con_matrix[:, starting] = 0

    shortest_path(con_matrix, starting)

    # find the critical path
    critical = min(comp.values())
    html_table = []

    for k in comp.keys():
        if comp[k] == critical:
            k = k.split("-")
            result = []
            for value in k:
                for cat in ref.keys():
                    if ref[cat] == int(value):
                        result.append(cat)
            r = "-".join(result)
            p_space = space.copy()
            for p in result:
                p = p.split(".")
                p_space[int(p[0]), int(p[1])] = 0

            p_space[int(starting_row), int(starting_column)] = 3
            p_space[int(ending_row), int(ending_column)] = 3

            html_table.append(numpy2html(p_space))

    html_page_code = create_html_page(html_table,
                                      f"SHORTEST PATH from cell({starting_row},{starting_column}) to cell({ending_row}, {ending_column})",
                                      css_file_name="shortestpath.css")
    with open("shortestpath_visual.html", "w") as f:
        f.write(html_page_code)

    print(t.stop())
    os.startfile("shortestpath_visual.html")
