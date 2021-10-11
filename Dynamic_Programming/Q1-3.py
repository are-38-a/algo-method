#https://algo-method.com/tasks/304
def main():
    N = int(input())
    C = [0] * 50

    C[0] = 1
    C[1] = 1

    for i in range(2,N+1):
        C[i] = C[i-1] + C[i-2] #1段前から来る場合/2段前から来る場合

    print(C[N])

if __name__=="__main__":
    main()