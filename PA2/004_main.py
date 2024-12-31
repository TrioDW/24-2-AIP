def print_snail_matrix(N):
    # N x N 크기의 빈 행렬 생성
    matrix = [[0] * N for _ in range(N)] 

    # [[1, 2, 3], 
    # [8, 9, 4], 
    # [7, 6, 5]]
    
    # 방향을 나타내는 변수들: 오른쪽, 아래, 왼쪽, 위쪽 순서
    dx = [0, 1, 0, -1] # 위에서 아래
    dy = [1, 0, -1, 0] # 왼쪽에서 오른쪽
    
    # 현재 위치 및 초기 방향 설정
    x, y, direction = 0, 0, 0
    current_num = 1
    
    # 행렬을 채우기 위한 반복문
    while current_num <= N * N:
        # 현재 위치에 숫자 삽입
        matrix[x][y] = current_num
        current_num += 1
        
        # 다음 위치 계산
        nx, ny = x + dx[direction], y + dy[direction]
        
        # 다음 위치가 범위를 벗어나거나 이미 값이 채워져 있으면 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny] != 0:
            direction = (direction + 1) % 4
            nx, ny = x + dx[direction], y + dy[direction]
        
        # 위치 업데이트
        x, y = nx, ny
    
    # 행렬 출력
    for row in matrix:
        print(" ".join(map(str, row)))

# 사용자로부터 입력받기
size = int(input())
print_snail_matrix(size)