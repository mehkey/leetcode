class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        count = 0

        for w in words:
            if w in s:
                count += 1

        return count
