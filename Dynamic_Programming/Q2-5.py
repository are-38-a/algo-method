# https://algo-method.com/tasks/333

def main():
    N = int(input())
    list_map = []
    for _ in range(N):
        list_map.append(list(input()))

    #配列を用意
    dp = [[0]*N for _ in range(N)]
    
    #初期値
    dp[0][0] = 1
    
    for i in range(N):
        for j in range(N):

            #上から来る
            if 0 < i:
                if list_map[i-1][j] == ".":
                    dp[i][j] += dp[i-1][j]
            #左からくる
            if 0 < j:
                if list_map[i][j-1] == ".":
                    dp[i][j] += dp[i][j-1]
    
    print(dp[N-1][N-1])


if __name__ == "__main__":
    main()