from boardloader import BoardLoader
from game import Game
from solver import Solver
from state import State
file = open('Levels/level_9.txt')
board = BoardLoader.transform_board_from_file_to_2d_list(file)
game = Game(board)
s0 = State(game)
solver = Solver(s0)

print("A* Path : ")
for state in solver.astar()[0]:
    print(state.game)

print("A* Path Cost : " , solver.astar()[2])
print("A* Vis Len : " , solver.astar()[1])

# print("UCS Path : ")
# for state in solver.ucs()[0]:
#     print(state.game)
# print("UCS Visited List : ",solver.ucs()[1])
#
# print("UCS Cost : " , solver.ucs()[2])

# print("\n\n\n")
#
# print("Recursive DFS Path : ")
# for state in solver.recursive_dfs(s0)[0]:
#     print(state.game)
# print("Recursive DFS Visited List : ")
# for state in solver.recursive_dfs(s0)[1]:
#     print(state.game)
#
# print("\n\n\n")

# print("Iterative DFS Path :")
# for state in solver.dfs()[0]:
#     print(state.game)
# print(len(solver.dfs()[1]))
# print("Iterative DFS Visited List :")
# for state in solver.dfs()[1]:
#     print(state.game)

# print("\n\n\n")


# print("Iterative BFS Path : ")
# for state in solver.bfs()[0]:
#     print(state.game)
# print("Iterative BFS Visited Path")
# for state in solver.bfs()[1]:
#     print(state.game)
# print(len(solver.bfs()[1]))


# Keyboard Playing :
# playable = True
# s0.game.display_board()
# while not s0.game.is_solved():
#     direction = input("Enter A Direction [Left , Right , Down , Up] : ")
#     s0.game = s0.game.move(direction)
#     if not s0.game.playable:
#         print("You Have Lost 💀")
#         playable = False
#         break
#     s0.game.display_board()
# if playable:
#     print("Congrats 🎉 , You Have Won 🏆")
