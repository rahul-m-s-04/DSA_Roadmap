"""
5. Hidden Word
Problem Statement
Print every second character without using loops.
Input
Input: String
Output
Output: String
Examples
Input: Programming Output: Pormig
"""

class Solution:
    def hidden_word(self, word: str) -> str:

        """
        Alternate appraoch:
        for i in range(0,len(word),2):
            print(word[i])

        """


        answer = word[0:len(word):2] # 0-start index, len(word) - end index, 2 - step value

        return answer

def main():
    word = input("Enter a word : ")
    solution = Solution()
    answer = solution.hidden_word(word)
    print(answer)
    

if __name__ == "__main__":
    main()
