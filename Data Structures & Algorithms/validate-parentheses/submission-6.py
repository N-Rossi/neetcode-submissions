class Solution:
    def isValid(self, s: str) -> bool:
        p = {')': '(', '}': '{', ']': '['}
        found = []
        for symbol in s:
            if symbol in "({[":
                found.append(symbol)
            elif symbol in ")]}":
                if not found or found.pop() != p[symbol]:
                    return False
        return not found
            
        