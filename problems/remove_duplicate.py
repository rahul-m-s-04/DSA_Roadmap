"""
3. Remove Only the First Duplicate
Problem Statement
Remove only the first duplicate occurrence from a list.
Input
Input: List of integers
Output
Output: Modified list
Examples
Input: [1,2,3,2,4,2] Output: [1,2,3,4,2]
"""

class Solution:
    def remove_duplicate(self, arr: list[int]) -> list[int]:
        answer = []
        idx = 0 #this is to keep track of the first duplicate in the arr.
        for i in range(len(arr)): #this for loop is top find the first duplicate
            if arr[i] in answer:
                idx = i
                break
            answer.append(arr[i])
        for i in range(idx+1, len(arr)): #this for loop is add the remaining elements in the arr apart from the first dauplicate.
            answer.append(arr[i])
        return answer

def main():
    arr = list(map(int,input().split())) #its just a line to get list input from user
    solution = Solution()
    arr = solution.remove_duplicate(arr)
    print(arr)

if __name__ == "__main__":
    main()