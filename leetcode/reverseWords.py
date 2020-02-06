class Solution:
    def reverseWords(self, s: str) -> str:
        l = []
        words = s.split(' ')
        for word in words:
            char = list(word)
            char.reverse()
            l.append(''.join(char))
        return ' '.join(l)
