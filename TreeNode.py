# Author: Raymond Zeng
# A simple tree-node implementation that represents a state in a decision tree.
import copy

goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

class TreeNode():
    # puzzle -> 2d square matrix
    # heuristic -> integer
    # depth -> integer 
    def __init__(self, puzzle, heuristic, depth):
        #Could implement a state here that defines more attributes of a state.
        self.board = puzzle 
        self.heuristic = heuristic
        self.depth = depth

    def getTotalDistance(self):
        return self.heuristic + self.depth

    def solved(self):
        return self.board == goal_state

    def __hash__(self) -> int:
        hash_clone = copy.deepcopy(self.board)
        for rowIndex in range(len(hash_clone)):
            hash_clone[rowIndex] = tuple(hash_clone[rowIndex])
        return hash(tuple(hash_clone))

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
    