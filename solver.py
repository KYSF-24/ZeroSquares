class Solver:
    def __init__(self , s0):
        self.s0 = s0

    @staticmethod
    def is_visited(visited_states,state):
        for visited_state in visited_states:
            if visited_state.game.equals(state.game):
                return True
        return False

    def dfs(self):
        st = [self.s0]
        vis = list()
        path = list()
        while st:
            state = st.pop()
            if not Solver.is_visited(vis,state):
                vis.append(state)
            if state.game.is_solved():
                while state:
                    path.append(state)
                    state = state.parent
                path = path[::-1]
                return path , vis
            for next_state in state.next_states():
                if not Solver.is_visited(vis, next_state):
                    st.append(next_state)

    def bfs(self):
        q = [self.s0]
        vis = list()
        path = list()
        while q:
            state = q.pop(0)
            if not Solver.is_visited(vis,state):
                vis.append(state)
            if state.game.is_solved():
                while state:
                    path.append(state)
                    state = state.parent
                path = path[::-1]
                return path , vis
            for next_state in state.next_states():
                if not Solver.is_visited(vis,next_state):
                    q.append(next_state)

    def recursive_dfs(self, state, vis = None, path  = None):
        if vis is None:
            vis = []
        if path is None:
            path = []
        vis.append(state)
        path.append(state)
        if state.game.is_solved():
            return path , vis
        for next_state in state.next_states():
            if not Solver.is_visited(vis , next_state):
                l_path , l_vis = self.recursive_dfs(next_state , vis , path)
                if l_path:
                    return l_path , l_vis
        path.pop()
        return [] , vis

    def ucs(self):
        """
           Default Approach Where The Cost Of Any Action (Move From State To State)
           Is Equal To One(1) , In This Case The UCS <-> BFS Because The Weights
           Are All Equal Between All States , Which Is Equivalent To Not Having
           Weights At All (So BFS).
        """
        pq = [(self.s0 , 0)]
        vis = list()
        path = list()
        while pq:
            state , cost = pq.pop(0)
            if not Solver.is_visited(vis,state):
                vis.append(state)
                if state.game.is_solved():
                    while state:
                        path.append(state)
                        state = state.parent
                    path = path[::-1]
                    return path , vis , cost
                for next_state in state.next_states():
                    if not Solver.is_visited(vis , next_state):
                        pq.append((next_state,1 + cost))
                pq.sort(key=lambda t:t[1])

    def ucs_(self):
        """
              In This Approach We Assumed That The Weight Of Each Edge
              Determined Based On How Many Squares Moved When We Traverse
              From The Previous State To The Next State In Some Direction
              (Just An Example For The Sake Of The UCS Algorithm).
              So We Made Some Minor Changes In The Structure Of The State Object
              And The game Next Steps Function In Order For The Simulation
              Of The Algorithm , These Changes Does Not Affect Any Previous Algorithms
              So They Still Work Perfectly Fine , And These Changes Might Be Really
              Useful For Later Algorithms That Demands Different Weights Like A* For
              Example.
        """
        pq = [(self.s0 , self.s0.cost)]
        vis = list()
        path = list()
        while pq:
            state , cost = pq.pop(0)
            if not Solver.is_visited(vis, state):
                vis.append(state)
                if state.game.is_solved():
                    while state:
                        path.append(state)
                        state = state.parent
                    path = path[::-1]
                    return path , vis , cost
                for next_state in state.next_states():
                    if not Solver.is_visited(vis, next_state):
                        pq.append((next_state,cost + next_state.cost))
                pq.sort(key=lambda t: t[1])