class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # dicts = []
        # for i in range(27):
        #     dicts.append({})
        # square = 0
        # for i in range(9):
        #     for j in range(9):
        #         element = board[i][j]
        #         #check cols
        #         dicts[i][element] = 1 + dicts[i].get(element, 0)
        #         if dicts[i].get(element, 1)>1 and element != ".":
        #             print(i,j,'1')
        #             return False
        #         #check col
        #         dicts[j+9][element] = 1 + dicts[j+9].get(element, 0)
        #         if dicts[j+9].get(element, 1)> 1 and element != ".":
        #             print(i,j,'2')
        #             return False

        #         if i%3==0 and j%3==0:
        #             for k in range(3):
        #                 for l in range(3):
        #                     element = board[i+k][j+l]
        #                     dicts[18+square][element] = 1 + dicts[18+square].get(element, 0)
        #                     if dicts[18+square].get(element, 0)>1 and element != ".":
        #                         print(i,j,'3',dicts, element)
        #                         return False
        #             square += 1
        # return True



        for i in range(9):
            d = {}
            for j in range(9):
                if not board[i][j] == ".":
                    d[board[i][j]] = 1+ d.get(board[i][j],0)
                    if d[board[i][j]]>1:
                        return False
            d = {}
            for j in range(9):
                if not board[j][i] == ".":
                    d[board[j][i]] = 1+ d.get(board[j][i],0)
                    if d[board[j][i]]>1:
                        return False

        squers = [[0,0], [0,3], [0,6], [3,0], [3,3], [3,6], [6,0], [6,3], [6,6]]
        counter = 0
        for i , j in squers:
            
            d = {}
            for m in range(3):
                for n in range(3):       
                    if not board[i+m][j+n] == ".":
                        d[board[i+m][j+n]] = 1+ d.get(board[i+m][j+n],0)
                        if d[board[i+m][j+n]]>1:
                            return False

        return True




