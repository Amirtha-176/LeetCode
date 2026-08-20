class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel=[]
        for w in s:
            if w in "aeiouAEIOU":
                vowel.append(w)
        res=""
        for w in s:
            if w in "aeiouAEIOU":
                res+=vowel.pop()#pop(-1)🤩NO need vowel[::-1]!!!
            else:
                res+=w
        return res