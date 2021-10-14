# https://algo-method.com/tasks/306
def main():
	INF = 1000000

	N, M = map(int, input().split())
	A = list(map(int,input().split()))

	T = [INF] * N
	
	T[0] = 0

	for i in range(1,N):
		for j in range(1,M+1):
			if i-j >= 0:
				T[i] = min(T[i], T[i-j] + A[i] * j)
	
	print(T[N-1])

if __name__=="__main__":
	main()