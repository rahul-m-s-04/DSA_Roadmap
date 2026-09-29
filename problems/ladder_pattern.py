"""
8. Number Ladder
Problem Statement
Print numbers from 1 to N in ladder format.
Input
Input: Integer N
Output
Output: Pattern
Examples
Input:5 Output: 1 / 12 / 123 / 1234 /12345
"""

class Solution:
    def ladder_pattern(self, n: int) -> None:
        for i in range(1,n+1):
            for j in range(1,n+1):
                if j<=i:
                    print(j,end = " ")
                else:
                    break
            print()

def main():
    n = int(input("Enter an integer : "))
    solution = Solution()
    solution.ladder_pattern(n)

if __name__ == "__main__":
    main()