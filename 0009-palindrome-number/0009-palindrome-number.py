class Solution(object):
    def isPalindrome(self, x):
        reverse = 0
        original = x
        test = False

        while x != 0 and x >0:
            rest = x % 10
            div = x // 10
            x = div
            reverse = reverse * 10 + rest

        if reverse == original and original >= 0:
            test = True

        return test