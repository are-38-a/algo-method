# https://algo-method.com/tasks/323

def main():
    N, M = map(int, input().split())
    list_D = list(map(int, input().split()))

    dp = [False] * (N+1)

    dp[0] = True

    for i in range(1, N+1):
        for j in range(M):
            if 0 <= i - list_D[j] and dp[i-list_D[j]]:
                dp[i] = True

    if dp[N]:
        print("Yes")
    else:
        print("No")

if __name__=="__main__":
    main()
