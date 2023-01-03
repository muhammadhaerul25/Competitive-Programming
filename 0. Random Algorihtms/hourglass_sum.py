def hourglass_sum(arr):
    #let arr is 6 x 6 2D arrays
    
    max_sum = -63
    #why? -9 x 7 = -63

    for i in range(4):
        for j in range(4):
            sum = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            max_sum = max(max_sum, sum)
    return max_sum

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglass_sum(arr)
    print(result)