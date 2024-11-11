from boardloader import BoardLoader
from game import Game
file = open('Levels/level_26.txt', 'r')
board = BoardLoader.transform_board_from_file_to_2d_list(file)
game = Game(board)
game.display_board()
# print(game.equals(game.move("up")))
# game.move("up").display_board()
# game.move("up").move("left").display_board()
# game.move("up").move("left").display_board()
# game.move("up").move("left").move("up").display_board()
# game.move("up").move("left").move("up").move("right").display_board()
# game.move("up").move("left").move("up").move("right").move("down").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").move("up").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").move("up").move("down").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").move("up").move("down").move("left").display_board()
# game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").move("up").move("down").move("left").move("up").display_board()
# print(game.move("up").move("left").move("up").move("right").move("down").move("up").move("left").move("down").move("right").move("up").move("down").move("left").move("up").is_solved())
# print(game.agents)
while not game.is_solved():
    direction = input("direction : ")
    if direction not in ["left","right","up",'down']:
        break
    game = game.move(direction)
    if not game.playable:
        break
    game.display_board()
if game.playable:
    print("You Win Bro 🏆")
else: print("Game Over 💀")
# for direction , game_ in game.next_steps():
#     print(f"If We Moved {direction} , We Get This Board : ")
#     print(game_)



