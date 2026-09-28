"""
7. Character Frequency Without Dictionary
Problem Statement
Print frequency of every unique character without using dictionaries.
Input -> it is always lowercase
Input:String
Output
Output:Character frequencies
Examples
Input: banana Output: b->1 a->3 n->2
"""

class Solution:
    def character_frequency(self, word: str) -> None:
        hashing = []
        for i in range(26):
            hashing.append(0)
        for i in word:
            hashing[ord(i)-97] += 1
        for i in range(26):
            if hashing[i]: #Im checking whether hashing[i] is either a zero or not.
                print(chr(i+97),"->",hashing[i])
def main():
    word = input("Enter a word : ")
    solution = Solution()
    solution.character_frequency(word)


if __name__ == "__main__":
    main()