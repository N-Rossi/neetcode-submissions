class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = False
        left = 0
        stripped = s.replace(" ", "")
        clean_text = re.sub(r'[^a-zA-Z0-9]', '', stripped).lower()
        right = len(list(clean_text)) - 1
        clean_text = list(clean_text)
        while left < right:
            if clean_text[left] == clean_text[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

        