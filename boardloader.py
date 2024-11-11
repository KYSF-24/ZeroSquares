class BoardLoader:
    @staticmethod
    def transform_board_from_file_to_2d_list(file):
        board = []
        for l in file:
            row = []
            if l.endswith("\n"):
                l = l[:-1:]
            for c in l.split(" "):
                    row.append([c[0],c[1]])
            board.append(row)
        return  board