from typing import List


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        word_index = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left_part = word[:j]
                right_part = word[j:]

                if j > 0 and is_palindrome(left_part) and right_part[::-1] in word_index:
                    result.append([word_index[right_part[::-1]], i])

                if is_palindrome(right_part) and left_part[::-1] in word_index and i != word_index[left_part[::-1]]:
                    result.append([i, word_index[left_part[::-1]]])

        return result

solution = Solution()
words = ["abcd","dcba","lls","s","sssll"]
print(solution.palindromePairs(words))