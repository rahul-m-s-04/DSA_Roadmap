"""
1. Mirror Number
Problem Statement
Given an integer n, if n is even print its digits from left to right. Otherwise print its digits from right to
left.
Input
Input: Integer n
Output
Output: Space-separated digits
Examples
Example 1: Input: 1234 Output: 1 2 3 4
Example 2: Input: 1235 Output: 5 3 2 1
Constraints
Constraints: 1 <= n <= 10^9
"""

class Solution:
    def mirror_number(self, n: int) -> None:
        l = [] #im storing the digits here one by one
        temp = n #Im taking this temp variable becausew i dont want to amnupilate the oringial value of n
        while(temp!=0):
           l.append(temp%10)
           temp = temp//10
        if n%2==0: #even condition
            for i in range(len(l)-1,-1,-1): #Im reversing the even list because the answer that i got from the while loop is already reversed.
                print(l[i],end=" ")
        if n%2==1: #odd condition
            for i in l:
                print(i,end=" ")
    

def main():
    n = int(input("Enter an integer : ")) #user input
    solution = Solution() #Object to invoke the method
    solution.mirror_number(n)

if __name__ == "__main__":
    main()