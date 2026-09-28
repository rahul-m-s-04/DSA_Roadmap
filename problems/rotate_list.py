"""
6. Rotate the List Once
Problem Statement
Move the last element to the beginning.
Input
Input: List
Output
Output: Rotated List
Examples
Input:[1,2,3,4] Output:[4,1,2,3]
"""


class Solution:
    def rotate_list(self, arr: list[int]) -> list[int]:
        answer = []

        answer.append(arr[len(arr)-1]) #First im adding the last element to the final answer

        for i in range(len(arr)-1): #im using len(arr)-1 becuase i have already taken the last element
            answer.append(arr[i])

        return answer

        

def main():
    arr = list(map(int,input().split())) #its just a line to get list input from user
    solution = Solution()
    answer = solution.rotate_list(arr)
    print(answer)

if __name__ == "__main__":
    main()