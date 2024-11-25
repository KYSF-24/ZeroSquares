# This Is A Wrapper Class For The Game Class For Higher Abstraction And More Understanding
class State:
    def __init__(self , game , parent = None , cost = 0):
        self.game = game
        self.parent = parent
        self.cost = cost

    def next_states(self):
        next_states = []
        for game in self.game.next_steps():
            next_states.append(State(game[1] , self , game[2]))
        return next_states