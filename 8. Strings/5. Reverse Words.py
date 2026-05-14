class Solution:
    def reverseWords(self, s):
        words = [w for w in s.split(".") if w]
        reverse = []
        
        for i in range(len(words)-1, -1, -1):
            reverse.append(words[i])
        
        return ".".join(reverse)