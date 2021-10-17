# https://algo-method.com/tasks/41

def main():

    #入力
    N = int(input())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))

    #配列を用意
    dp = [[0]*3 for _ in range(N)]

    #1日目
    for j in range(3):
        dp[0][j] = A[0][j]

    #i日目の報酬を求める
    for i in range(1,N):
        dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i][0]
        dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + A[i][1]
        dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + A[i][2]

    #N-1日目の報酬を表示
    print(max(dp[N-1][0], dp[N-1][1], dp[N-1][2])) 