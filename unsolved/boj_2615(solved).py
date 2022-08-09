def check():
    board = []
    for _ in range(19):
        board.append(input().split())

    for i in range(19):
        for j in range(19):           
            if board[i][j] == '1' or board[i][j] == '2':
                val = '1' if board[i][j] == '1' else '2'

                for k in range(3):
                    coordi = []
                    for l in range(1, 6):
                        if not k and -1 < j + l < 19:                          
                            if board[i][j + l] == val:
                                coordi.append((i, j + l))
                            else:
                                break
                        elif k == 1 and -1 < i + l < 19:
                            if board[i + l][j] == val:
                                print(val, i + l, j)
                                coordi.append((i + l, j))
                            else:
                                break
                        elif k == 2 and -1 < j + l < 19:
                            if board[i + l][j + l] == val:
                                coordi.append((i + l, j + l))
                            else:
                                break
                        else:
                            break

                    coordi = [(i, j)] + coordi
                    
                    if len(coordi) == 5:
                        return val, coordi
    
    return 0, ()

val, coordi = check()
print(int(val))
if val:
    print(coordi[0][0] + 1, coordi[0][1] + 1)
