import math


class Game:

    def __init__(self, board):
        self.board = board
        self.playable = True
        agents = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col][0] != 'n' and board[row][col][0].islower():
                    agents.append([row, col, True])
        self.agents = agents

    def display_board(self):
        print()
        for row in self.board:
            for cell in row:
                print(self.cell_mapper(self.cell_former(cell)), end="")
            print()
        print()

    @staticmethod
    def cell_former(cell):
        if cell[1] != 'n' and cell[0] == 'n':
            return cell[1]
        return cell[0]

    @staticmethod
    def cell_mapper(cell):
        color_map = {
            '#': '⬛',
            '$': '🔲',
            'n': '⬜',
            'b': '🟦',
            'r': '🟥',
            'p': '🟪',
            'y': '🟨',
            'g': '🟩',
            'o': '🟧',
            'B': '🔵',
            'R': '🔴',
            'P': '🟣',
            'Y': '🟡',
            'G': '🟢',
            'O': '🟠',
            'W': '⚪',
        }
        return color_map[cell]

    def deep_copy(self):
        board_copy = []
        for row in self.board:
            board_copy.append([[a, b] for [a, b] in row])
        return Game(board_copy)

    def __str__(self):
        res = ""
        for row in self.board:
            for cell in row:
                res += self.cell_mapper(self.cell_former(cell))
            res += "\n"
        return res

    def equals(self, game):
        for row in range(len(game.board)):
           for col in range(len(game.board[row])):
               if game.board[row][col][0] != self.board[row][col][0] or game.board[row][col][1] != self.board[row][col][1]:
                   return False
        return True

    def is_solved(self):
        if not self.agents:
            return True and self.playable
        return False

    def mark_unmovable_agents(self,direction):
        for agent in self.agents:
            if not self.movable(agent,direction):
                agent[2] = False

    def reset_unmovable_agents(self):
        for agent in self.agents:
                agent[2] = True

    def in_bounds(self,row,col):
        return 0 <= row < len(self.board) and 0 <= col < len(self.board[row])

    def movable(self , agent , direction):
        if direction == "right":
            if self.in_bounds(agent[0] , agent[1] + 1) and self.board[agent[0]][agent[1] + 1][0] == 'n':
                return True
        if direction == "left":
            if self.in_bounds(agent[0] , agent[1] - 1) and self.board[agent[0]][agent[1] - 1][0] == 'n':
                return True
        if direction == "up":
            if self.in_bounds(agent[0] - 1 , agent[1]) and self.board[agent[0] - 1][agent[1]][0] == 'n':
                return True
        if direction == "down":
            if self.in_bounds(agent[0] + 1 , agent[1]) and self.board[agent[0] + 1][agent[1]][0] == 'n':
                return True
        return False

    def move(self,direction):
        if self.playable:
            game_copy = self.deep_copy()
            game_copy.mark_unmovable_agents(direction)
            if direction == "right":
                r = 0
                for x in range(len(game_copy.agents) - 1 , -1 , -1):
                    x = x - r
                    if game_copy.agents[x][2]:
                        for col in range(game_copy.agents[x][1] + 1,len(game_copy.board[game_copy.agents[x][0]])):
                            if game_copy.board[game_copy.agents[x][0]][col][0] == '#' or (game_copy.board[game_copy.agents[x][0]][col][0] != 'n' and game_copy.board[game_copy.agents[x][0]][col][0].islower()):
                                break
                            if game_copy.board[game_copy.agents[x][0]][col][0] == '$':
                                game_copy.playable = False
                                game_copy.board[game_copy.agents[x][0]][col][0] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col][1] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col - 1][0] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
                            game_copy.board[game_copy.agents[x][0]][col][0] = game_copy.board[game_copy.agents[x][0]][col - 1][0]
                            game_copy.board[game_copy.agents[x][0]][col - 1][0] = game_copy.board[game_copy.agents[x][0]][col - 1][1]
                            game_copy.agents[x][1] += 1
                            if game_copy.board[game_copy.agents[x][0]][col][1] == 'W':
                                game_copy.board[game_copy.agents[x][0]][col][1] = game_copy.board[game_copy.agents[x][0]][col][0].upper()
                                break
                            if game_copy.board[game_copy.agents[x][0]][col][1] == game_copy.board[game_copy.agents[x][0]][col][0].upper():
                                game_copy.board[game_copy.agents[x][0]][col][0] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col][1] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
            elif direction == "left":
                r = 0
                for x in range(len(game_copy.agents)):
                    x = x - r
                    if game_copy.agents[x][2]:
                        for col in range(game_copy.agents[x][1] - 1 , -1 , -1):
                            if game_copy.board[game_copy.agents[x][0]][col][0] == '#' or (game_copy.board[game_copy.agents[x][0]][col][0] != 'n' and game_copy.board[game_copy.agents[x][0]][col][0].islower()):
                                break
                            if game_copy.board[game_copy.agents[x][0]][col][0] == '$':
                                game_copy.playable = False
                                game_copy.board[game_copy.agents[x][0]][col][0] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col][1] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col + 1][0] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
                            game_copy.board[game_copy.agents[x][0]][col][0] = game_copy.board[game_copy.agents[x][0]][col + 1][0]
                            game_copy.board[game_copy.agents[x][0]][col + 1][0] = game_copy.board[game_copy.agents[x][0]][col + 1][1]
                            game_copy.agents[x][1] -= 1
                            if game_copy.board[game_copy.agents[x][0]][col][1] == 'W':
                                game_copy.board[game_copy.agents[x][0]][col][1] = game_copy.board[game_copy.agents[x][0]][col][0].upper()
                                break
                            if game_copy.board[game_copy.agents[x][0]][col][1].lower() == game_copy.board[game_copy.agents[x][0]][col][0]:
                                game_copy.board[game_copy.agents[x][0]][col][0] = 'n'
                                game_copy.board[game_copy.agents[x][0]][col][1] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
            elif direction == "up":
                r = 0
                for x in range(len(game_copy.agents)):
                    x = x - r
                    if game_copy.agents[x][2]:
                        for row in range(game_copy.agents[x][0] - 1 , -1 , -1):
                            if game_copy.board[row][game_copy.agents[x][1]][0] == '#' or (game_copy.board[row][game_copy.agents[x][1]][0] != 'n' and game_copy.board[row][game_copy.agents[x][1]][0].islower()):
                                break
                            if game_copy.board[row][game_copy.agents[x][1]][0] == '$':
                                game_copy.playable = False
                                game_copy.board[row][game_copy.agents[x][1]][0] = 'n'
                                game_copy.board[row][game_copy.agents[x][1]][1] = 'n'
                                game_copy.board[row + 1][game_copy.agents[x][1]][0] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
                            game_copy.board[row][game_copy.agents[x][1]][0] = game_copy.board[row + 1][game_copy.agents[x][1]][0]
                            game_copy.board[row + 1][game_copy.agents[x][1]][0] = game_copy.board[row + 1][game_copy.agents[x][1]][1]
                            game_copy.agents[x][0] -= 1
                            if  game_copy.board[row][game_copy.agents[x][1]][1] == 'W':
                                game_copy.board[row][game_copy.agents[x][1]][1] = game_copy.board[row][game_copy.agents[x][1]][0].upper()
                                break
                            if game_copy.board[row][game_copy.agents[x][1]][1] == game_copy.board[row][game_copy.agents[x][1]][0].upper():
                                game_copy.board[row][game_copy.agents[x][1]][0] = 'n'
                                game_copy.board[row][game_copy.agents[x][1]][1] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
            elif direction == "down":
                r = 0
                for x in range(len(game_copy.agents) - 1 , -1 , -1):
                    x = x - r
                    if game_copy.agents[x][2]:
                        for row in range(game_copy.agents[x][0] + 1 , len(game_copy.board)):
                            if game_copy.board[row][game_copy.agents[x][1]][0] == '#' or (game_copy.board[row][game_copy.agents[x][1]][0] != 'n' and game_copy.board[row][game_copy.agents[x][1]][0].islower()):
                                break
                            if game_copy.board[row][game_copy.agents[x][1]][0] == '$':
                                game_copy.playable = False
                                game_copy.board[row][game_copy.agents[x][1]][0] = 'n'
                                game_copy.board[row][game_copy.agents[x][1]][1] = 'n'
                                game_copy.board[row - 1][game_copy.agents[x][1]][0] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
                            game_copy.board[row][game_copy.agents[x][1]][0] = game_copy.board[row - 1][game_copy.agents[x][1]][0]
                            game_copy.board[row - 1][game_copy.agents[x][1]][0] = game_copy.board[row - 1][game_copy.agents[x][1]][1] if game_copy.board[row - 1][game_copy.agents[x][1]][1].islower() else 'n'
                            game_copy.agents[x][0] += 1
                            if  game_copy.board[row][game_copy.agents[x][1]][1] == 'W':
                                game_copy.board[row][game_copy.agents[x][1]][1] = game_copy.board[row][game_copy.agents[x][1]][0].upper()
                                break
                            if game_copy.board[row][game_copy.agents[x][1]][1] == game_copy.board[row][game_copy.agents[x][1]][0].upper():
                                game_copy.board[row][game_copy.agents[x][1]][0] = 'n'
                                game_copy.board[row][game_copy.agents[x][1]][1] = 'n'
                                game_copy.agents.remove(game_copy.agents[x])
                                r += 1
                                break
            game_copy.reset_unmovable_agents()
            return game_copy
        else :
            return self

    def next_steps(self):
        steps = []
        directions = ['left','right','up','down']
        for x in range(4):
            if not self.equals(self.move(directions[x])):
                steps.append([directions[x],self.move(directions[x]),self.g_cost(directions[x])])
        return steps

    def g_cost(self , direction):
        c = 0
        game_copy = self.deep_copy()
        game_copy.mark_unmovable_agents(direction)
        for agent in game_copy.agents:
            if agent[2]:
                c += 1
        return c

    def h_cost(self , method = 'md'):
        def manhattan_distance():
            md  = 0
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j][1].isalpha() and self.board[i][j][1].isupper():
                        for agent in self.agents:
                            if self.board[i][j][1] == self.board[agent[0]][agent[1]][0].upper():
                                md += abs(i - agent[0]) + abs(j - agent[1])
                                break
            return md
        def euclidean_distance():
            ed  = 0
            for i in range(len(self.board)):
                for j in range(len(self.board[i])):
                    if self.board[i][j][1].isalpha() and self.board[i][j][1].isupper():
                        for agent in self.agents:
                            if self.board[i][j][1] == self.board[agent[0]][agent[1]][0].upper():
                                ed += math.sqrt(pow((i - agent[0]) , 2) + pow(abs(j - agent[1]),2))
                                break
            return ed
        fn = {'md':manhattan_distance ,'ed':euclidean_distance}
        return fn[method]()

