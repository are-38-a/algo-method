# https://algo-method.com/tasks/324

def main():
    A = [list(map(int, input().split()))]
    for _ in range(3):
        A.append([0,0,0,0])

    for i in range(1,4):
        for j in range(4):
            
            #左上がある
            if 0 < j:
                A[i][j] += A[i-1][j-1]
            
            #真上
            A[i][j] += A[i-1][j]

            #右上がある
            if j < 3:
                A[i][j] += A[i-1][j+1]

    print(A[3][3])



if __name__=="__main__":
    main()