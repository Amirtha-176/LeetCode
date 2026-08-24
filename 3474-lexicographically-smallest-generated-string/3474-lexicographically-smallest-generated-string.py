class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        ans = ['?'] * (n + m - 1)
        for i, b in enumerate(str1):
            if b != 'T':
                continue
            for j, ch in enumerate(str2):
                cur = ans[i + j]
                if cur != '?' and cur != ch:
                    # Conflict
                    return ""
                ans[i + j] = ch
        new_ans = ['a' if ch == '?' else ch for ch in ans]
        for i, b in enumerate(str1):
            if b != 'F':
                continue
            if "".join(new_ans[i:i + m]) != str2:
                continue
            # Check substring new_ans[i:i + m]
            for j in range(i + m - 1, i - 1, -1):
                if ans[j] == '?':
                    new_ans[j] = 'b'
                    break
            else:
                # Not able to adjust the substring
                return ""
        return "".join(new_ans)