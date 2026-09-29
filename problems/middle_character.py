"""
9. Replace the Middle Character
Problem Statement
Replace middle character(s) with * or **.
Input
Input:String
Output
Output:Modified String
Examples
hello->he*lo python->py**on
"""

class Solution:
    def middle_character(self, word: str) -> str:
        length = len(word)
        answer = ""
        if length%2==0:
            for i in range(len(word)):
                if i == len(word)//2 or i == len(word)//2 - 1:
                    answer += "*" # += is same as appending a character to a string
                else:
                    answer += word[i]
        else:
            for i in range(len(word)):
                if i == len(word)//2:
                    answer += "*"
                else:
                    answer += word[i]
        return answer

def main():
    word = input("Enter a word : ")
    solution = Solution()
    answer = solution.middle_character(word)
    print(answer)
    

if __name__ == "__main__":
    main()
