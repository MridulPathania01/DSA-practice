"""
Array Reduction algorithm
n = size of array
arr = array of size n

1. initialzie an empty array result
2. Select an integer such that 1<=k<=n
3. append the MEX(minimum Excludant) of the fist k elements of array to result
4. remove the first k elements from the array
determine the lexicographically largest array result that can be obtained using the algorithm
"""
from typing import List
def arrRed(n: int, arr: List[int]) -> List[int]:
    result=[]
    while arr:
        k = min(n, len(arr))
        mex = 0
        seen = set(arr[:k])
        while mex in seen:
            mex+=1
        result.append(mex)
        arr = arr[k:]
    return result

if __name__ == "__main__":
    n = int(input())
    arr=[]*n
    for i in range(n):
        arr.append(int(input()))
    result = arrRed(n, arr)
    print(" ".join(map(str, result)))