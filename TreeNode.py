# Author: Raymond Zeng
# A simple tree-node implementation that represents a state in a decision tree.
import copy

goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

goal_map = {}

for row in range(len(goal_state)):
    for col in range(len(goal_state[row])):
        goal_map[goal_state[row][col]] = (row, col)

class TreeNode():
    # board -> 2d square matrix
    # heuristic -> integer
    # depth -> integer 
    def __init__(self, parent, board, heuristic, depth):
        #Could implement a state here that defines more attributes of a state.
        self.parent = parent
        self.board = board
        self.heuristic = heuristic
        self.depth = depth

    def getTotalDistance(self):
        return self.heuristic + self.depth

    def solved(self):
        return self.board == goal_state

    def tostring(self):
        hashString = ""
        for row in self.board:
            hashString = hashString.join(str(row))
        return hashString

    #Helper functions to help comparison in the pq
    def __lt__(self, other):
        if self.getTotalDistance() < other.getTotalDistance():
            return True
        elif self.getTotalDistance() == other.getTotalDistance():
            return self.depth < other.depth
        return False

    def findZero(self): #Returns the row, col tuple of where the 0 is.
        currRow = 0
        currCol = 0
        for row in self.board:
            for value in row:
                if value == 0:
                    return (currRow, currCol)
                currCol += 1
            currRow += 1
            currCol = 0

    def swapUp(self):
        row, col = self.findZero()
        if row > 0:
            board_copy = copy.deepcopy(self.board)
            board_copy[row - 1][col], board_copy[row][col] = board_copy[row][col], board_copy[row - 1][col] #Swap in-place with the number above
            return board_copy

    def swapDown(self):
        row, col = self.findZero()
        if row < len(self.board) - 1:
            board_copy = copy.deepcopy(self.board)
            board_copy[row + 1][col], board_copy[row][col] = board_copy[row][col], board_copy[row + 1][col] #Swap in-place with the number below
            return board_copy
    
    def swapLeft(self):
        row, col = self.findZero()
        if col > 0:
            board_copy = copy.deepcopy(self.board)
            board_copy[row][col - 1], board_copy[row][col] = board_copy[row][col], board_copy[row][col - 1] #Swap in-place with the number to the left
            return board_copy
    
    def swapRight(self):
        row, col = self.findZero()
        if col < len(self.board[0]) - 1:
            board_copy = copy.deepcopy(self.board)
            board_copy[row][col + 1], board_copy[row][col] = board_copy[row][col], board_copy[row][col + 1] #Swap in-place with the number to the right
            return board_copy

    def findTile(self, target, source): #Finds a tile within the 2d matrix, and returns a tuple coordinate if it is found.
        if source == goal_state: #Return the goal state cached coordinate
            return goal_map[target]
        for row in range(len(source)):
            for col in range(len(source[0])):
                if source[row][col] == target:
                   return (row, col) 
    
    def misplacedTiles(self): #Returns a list of misplaced tiles based off of the goal state in the form of a tuple of tuples.
        misplaced = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                if self.board[row][col] != goal_state[row][col] and goal_state[row][col] != 0:
                    misplacedPair = (row, col)
                    misplaced.append(misplacedPair)
        return misplaced

    def manhattanDistance(self): #Calculates the total manhattan distance of a board based off of its place in the goal state.
        misplacedList = self.misplacedTiles()
        dX_total = 0
        dY_total = 0
        for pair in misplacedList:
            goal_coord = self.findTile(self.board[pair[0]][pair[1]], goal_state)
            dX_total += abs(goal_coord[0] - pair[0])
            dY_total += abs(goal_coord[1] - pair[1])
        return dX_total + dY_total