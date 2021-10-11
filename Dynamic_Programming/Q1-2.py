#https://algo-method.com/tasks/303
def main():
    N = int(input())
    A = list(map(int, input().split()))

    T = [0] * 110

    T[0] = 0
    T[1] = A[1]

    for i in range(2,N):
        T[i] = min(T[i-1] + A[i], T[i-2] + 2*A[i])
    
    print(T[N-1])

if __name__=="__main__":
    main()