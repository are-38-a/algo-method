# https://algo-method.com/tasks/329

def main():
    N = int(input())

    #盤面を用意
    A = [[0]*N for _ in range(N)]

    #初期値
    A[0][0] = 1
    
    for i in range(N):
        for j in range(N):
            #上からくる
            if 0 < i:
                A[i][j] += A[i-1][j]
            #左からくる
            if 0 < j:
                A[i][j] += A[i][j-1]
    
    print(A[N-1][N-1])

if __name__=="__main__":
    main()