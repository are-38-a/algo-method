# https://algo-method.com/tasks/325

def main():

    #入力
    N = int(input())
    A = [[0] * N for _ in range(N)]
    A[0] = list(map(int, input().split()))

    #順に求めていく
    for i in range(1,N):
        for j in range(N):

            #左上がある
            if 0 < j:
                A[i][j] += A[i-1][j-1]
                A[i][j] %= 100

            #真上
            A[i][j] += A[i-1][j]
            A[i][j] %= 100

            #右上がある
            if j < N-1:
                A[i][j] += A[i-1][j+1]
                A[i][j] %= 100

    print(A[N-1][N-1])



if __name__=="__main__":
    main()