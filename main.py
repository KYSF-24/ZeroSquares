from boardloader import BoardLoader
from game import Game
from solver import Solver
from state import State
file = open('Levels/level_21.txt')
board = BoardLoader.transform_board_from_file_to_2d_list(file)
game = Game(board)
s0 = State(game)
solver = Solver(s0)
print("UCS : ")
for state in solver.ucs()[0]:
    print(state.game)
print("UCS Visited List : ")
for state in solver.ucs()[1]:
    print(state.game)
print("UCS Cost : " , solver.ucs()[2])
# print("Recursive DFS : ")
# for state in solver.recursive_dfs(s0)[0]:
#     print(state.game)
# print("Visited List : ")
# for state in solver.recursive_dfs(s0)[1]:
#     print(state.game)
# print("Solving Using DFS")
# for state in solver.dfs()[0]:
#     print(state.game)
# print(len(solver.dfs()[1]))
# print("Visited Path")
# for state in solver.dfs()[1]:
#     print(state.game)
# print("\n\n\n")
# print("Solving Using BFS")
# for state in solver.bfs()[0]:
#     print(state.game)
# print("Visited Path")
# for state in solver.bfs()[1]:
#     print(state.game)
# print(len(solver.bfs()[1]))
