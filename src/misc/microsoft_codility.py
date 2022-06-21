'''
Writing Down My Thoughts:
This is an optimization problem. It looks like it's getting the max of the indices of 2 matching elements
in an Array A. If the indicies i, j both have the same element then it takes the max value of (i-j) or the previous
max of (i-j).

Time Complexity:
Original Code -> O(N^2) where it is comparing each element in the array A with each of the elements in A.

There probably is a solution that is more efficient when finding the maxiumum indicies of matching elements.

Possible Solutions:
1] The easier of the solution would be to find a way to convert the two nested for loops into a single iteration. Then
trying to find the maxiumum value that way.

2] Another solution is to use a hash map. With a lookup of O(1) It would be the most effiecnet way. That way with one
iteration the time complexity would be O(N)

I started with solution 2 because it's easier to implement then trying to figure out a faster way to iterate over every
element in an array. I am having a problem comparing the index I saved in the dict with the current iterating
index

'''


def solution(A):
    dict = {}
    result = 0
    N = len(A)
    for i in range(N):
        if(dict[str(i)] is None):
            dict[str(i)] = i
        else:
            result = max(result, abs(i,dict[str(i)]))
    return result

print(max(0,abs(4-4)))
print(solution([4,3,3,1,8,5]))