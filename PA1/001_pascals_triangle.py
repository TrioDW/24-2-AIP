def generate_pascals_triangle(n):
    triangle = [] # [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]

    for i in range(n):
        row = [1] * (i + 1) # 모든 값을 1로 초기화
        for idx in range(1, i): #[1,2,1]
            row[idx] = triangle[i-1][idx-1] + triangle[i-1][idx]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    max_len = len(triangle[-1]) * 2 - 1  # 마지막 행 길이

    for row in triangle:
        row_str = " ".join(map(str, row)) #["1","2","1"] => "1 2 1"
        print(row_str.center(max_len))


if __name__ == "__main__":
    n = int(input())
    
    pascal_triangle = generate_pascals_triangle(n)
    print_pascals_triangle(pascal_triangle)