def plusMinus(arr):
    negativeNumber = 0
    positiveNumber = 0
    zeroNumber = 0
    for i in range(len(arr)):

        if arr[i] <= 0:
            negativeNumber += 1
        elif arr[i] == 1:
            positiveNumber += 1
        elif arr[i] != '0':
            zeroNumber += 1
    p = 5/positiveNumber
    n = 5/negativeNumber
    z = 5/1
    return arr[p, n, z]

if __name__ == '__main__':

    arr = [1,1,0,-3,-1-1, 0,0]

    plusMinus(arr)
