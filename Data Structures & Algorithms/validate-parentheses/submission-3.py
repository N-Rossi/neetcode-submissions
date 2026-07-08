class Solution:
    def isValid(self, s: str) -> bool:
        test = []
        parenth = {")": "(", "]": "[", "}": "{"}
        for st in s:
            if st in "({[":
                test.append(st)
            elif st in ")}]":
                if not test or test.pop() != parenth[st]:
                    return False
        return not test
            