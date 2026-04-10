class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sames_l = []
        sames_r = []
        same = ""
        iso = True
        for i in range(9):
            for j in range(9):
                same = board[i][j]
                other = board[j][i]
                if same != ".":
                    if same in sames_r:
                        iso = False
                    if same not in sames_r:
                        sames_r.append(same)
                if other != ".":
                    if other in sames_l:
                        iso = False
                    if other not in sames_l:
                        sames_l.append(other)
            sames_l.clear()
            sames_r.clear()
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                boxes = []
                for n in range(3):
                    for g in range(3):
                        if board[i + n][j+g] != ".":
                            if board[i + n][j+g] not in boxes:
                                boxes.append(board[i+n][j+g])
                            else:
                                iso = False
            
        return(iso)