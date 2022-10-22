# Author: Raymond Zeng
# A simple tree-node implementation that should hold n children.

class TreeNode():
    # puzzle -> 2d square matrix
    # heuristic -> integer
    # depth -> integer 
    def __init__(self, puzzle, heuristic, depth):
        #Could implement a state here that defines more attributes of a state.
        self.puzzle = puzzle 
        self.children = []
        self.heuristic = heuristic
        self.depth = depth

    def getTotalDistance(self):
        return self.heuristic + self.depth