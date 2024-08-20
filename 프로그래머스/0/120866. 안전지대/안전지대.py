def solution(board):
    answer = 0
    land_arr = []
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                land_arr.append([i,j])
                
    direction = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    
    for l in land_arr:
        for x, y in direction:
            if 0 <= (l[0] + x) < len(board) and 0 <= (l[1] + y) < len(board):
                board[l[0] + x][l[1] + y] = 1
    
    for b in board:
        answer += b.count(0)   
    
    return answer