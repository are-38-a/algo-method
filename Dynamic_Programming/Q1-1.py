#https://algo-method.com/tasks/302

def main():
    N, X, Y = map(int, input().split())

    A = [0 for _ in range(110)]
    A[0] = X
    A[1] = Y
    for i in range(2,N):
	    A[i] = (A[i-2]+A[i-1])%100

    print(A[N-1])

if __name__=="__main__":
    main()