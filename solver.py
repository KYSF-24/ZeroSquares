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
        path = []
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
        path = []
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
            if not Solver.is_visited(vis,next_state):
                l_path , l_vis = self.recursive_dfs(next_state , vis , path)
                if l_path:
                    return l_path , l_vis
        path.pop()
        return [] , vis



