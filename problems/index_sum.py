"""
4. Odd Index Sum vs Even Index Sum
Problem Statement
Compare the sums at even and odd indices.
Input
Input: List
Output
Output: Even Index Sum is Greater / Odd Index Sum is Greater / Equal
Examples
Example: [10,20,30,40,50] -> Even Index Sum is Greater
"""

class Solution:
    def index_sum(self, arr: list[int]) -> None:
        odd_sum = 0
        even_sum = 0
        for i in range(len(arr)):
            if i%2==0:
                even_sum += arr[i]
            else:
                odd_sum += arr[i]

        if odd_sum > even_sum:
            print("Odd Sum is greater")
        elif odd_sum < even_sum:
            print("Even Sum is greater")
        else:
            print("Equal")

def main():
    arr = list(map(int,input().split()))
    solution = Solution()
    solution.index_sum(arr)
    

if __name__ == "__main__":
    main()