"""
2. Secret Password
Problem Statement
Determine whether a password is Strong or Weak.
Input
Input: A string
Output
Output: Strong or Weak
Examples
Strong if length>=8, has one uppercase letter and one digit.
"""

class Solution:
    def secret_password(self, password: str) -> str:
        answer = 0
        if len(password)>=8: #First condition
            answer += 1
        for i in password: #Second condition
            if i.isupper():
                answer += 1
                break
        for i in password: #Third condition
            if i.isdigit():
                answer += 1
                break
        
        if answer < 3: #will only be strong if answer == 3 because to be a strong password it must satisfy all the 3 conditions
            return "Weak"
        else:
            return "Strong"


def main():
    password = input("Enter your password : ")
    solution = Solution()
    answer = solution.secret_password(password)
    print(answer)

if __name__ == "__main__":
    main()