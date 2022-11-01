import TreeNode
import heapq as min_heap_esque_queue
import time
# because it sort of acts like a min heap
# Below are some built-in puzzles to allow quick testing.
trivial = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 0]]
veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]
easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]
doable = [[0, 1, 2],
          [4, 5, 3],
          [7, 8, 6]]
oh_boy = [[8, 7, 1],
          [6, 0, 2],
          [5, 4, 3]]

def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, or '2' to create your own." + '\n')
    if puzzle_mode == "1":
        select_and_init_algorithm(init_default_puzzle_mode())
    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
        "Please only enter valid 8-puzzles. Enter the puzzle delimiting " +
        "the numbers with a space. RET only when finished." + '\n')
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")
        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()
        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])
        user_puzzle = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        select_and_init_algorithm(user_puzzle)
    return

def init_default_puzzle_mode():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 4." + '\n')
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return trivial
    if selected_difficulty == "1":
        print("Difficulty of 'Very Easy' selected.")
        return veryEasy
    if selected_difficulty == "2":
        print("Difficulty of 'Easy' selected.")
        return easy
    if selected_difficulty == "3":
        print("Difficulty of 'Doable' selected.")
        return doable
    if selected_difficulty == "4":
        print("Difficulty of 'Oh Boy' selected.")
        return oh_boy

def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        print(puzzle[i])
    print('\n')

def print_solution(node):
    depth = 0
    current_node = node
    while current_node.parent != None:
        print_puzzle(current_node.board)
        current_node = current_node.parent
        depth += 1
    print_puzzle(current_node.board)
    print(f"Depth: {depth}")

def select_and_init_algorithm(puzzle):
    algorithm=input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                    "or (3) the Manhattan Distance Heuristic." + '\n')
    if algorithm == "1":
        uniform_cost_search(puzzle, 0)
    if algorithm == "2":
        uniform_cost_search(puzzle, 1)
    if algorithm == "3":
        uniform_cost_search(puzzle, 2)

def uniform_cost_search(puzzle, heuristic):
    timestart = time.time()
    starting_node=TreeNode.TreeNode(None, puzzle, 0, 0)
    working_queue=[]
    repeated_states=set()
    min_heap_esque_queue.heappush(working_queue, starting_node)
    num_nodes_expanded=0
    max_queue_size=0
    repeated_states.add(starting_node.tostring())

    while len(working_queue) > 0:
        max_queue_size=max(len(working_queue), max_queue_size)
        # the node from the queue being considered/checked
        node_from_queue=min_heap_esque_queue.heappop(working_queue)
        repeated_states.add(node_from_queue.tostring())
        if node_from_queue.solved():  # check if the current state of the board is the solution
            print_solution(node_from_queue)
            print("Number of nodes expanded:", num_nodes_expanded)
            print("Max queue size:", max_queue_size)
            print("Time elapsed:", round((time.time() - timestart) * 1000, 3), "ms")
            return node_from_queue
        else:
            #Try swapping in 4 directions, making sure to avoid duplicate states.
            swapped_up = node_from_queue.swapUp()
            swapped_down = node_from_queue.swapDown()
            swapped_left = node_from_queue.swapLeft()
            swapped_right = node_from_queue.swapRight()

            if swapped_up != None:
                newState = TreeNode.TreeNode(node_from_queue, swapped_up, 0, node_from_queue.depth + 1)
                if heuristic == 1:
                    newState.heuristic += len(newState.misplacedTiles())
                elif heuristic == 2:
                    newState.heuristic += newState.manhattanDistance()
                if not newState.tostring() in repeated_states:
                    min_heap_esque_queue.heappush(working_queue, newState)
                    num_nodes_expanded += 1

            if swapped_down != None:
                newState = TreeNode.TreeNode(node_from_queue, swapped_down, 0, node_from_queue.depth + 1)
                if heuristic == 1:
                    newState.heuristic += len(newState.misplacedTiles())
                elif heuristic == 2:
                    newState.heuristic += newState.manhattanDistance()
                if not newState.tostring() in repeated_states:
                    min_heap_esque_queue.heappush(working_queue, newState)
                    num_nodes_expanded += 1

            if swapped_left != None:
                newState = TreeNode.TreeNode(node_from_queue, swapped_left, 0, node_from_queue.depth + 1)
                if heuristic == 1:
                    newState.heuristic += len(newState.misplacedTiles())
                elif heuristic == 2:
                    newState.heuristic += newState.manhattanDistance()
                if not newState.tostring() in repeated_states:
                    min_heap_esque_queue.heappush(working_queue, newState)
                    num_nodes_expanded += 1

            if swapped_right != None:
                newState = TreeNode.TreeNode(node_from_queue, swapped_right, 0, node_from_queue.depth + 1)
                if heuristic == 1:
                    newState.heuristic += len(newState.misplacedTiles())
                elif heuristic == 2:
                    newState.heuristic += newState.manhattanDistance()
                if not newState.tostring() in repeated_states:
                    min_heap_esque_queue.heappush(working_queue, newState)
                    num_nodes_expanded += 1              
        if len(working_queue) > 0: #Safeguard against out-of-bounds error if no solution exists.
            print(f"Next state: with depth {working_queue[0].depth} and heuristic {working_queue[0].heuristic}")
            print(f"Board: {working_queue[0].board}\n")

    print("Unable to solve the puzzle - all states have been exhausted.")

#Defining the actual main function
if __name__ == "__main__":
    main()