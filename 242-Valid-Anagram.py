class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length first since if its not equal then it cannot be an anagram
        if len(s) != len(t):
            return False
        # create empty hashmaps to keep value of our char's as keys and count as values
        countS = {}
        countT = {}

        # go through the strings and +1 for each char that appears and reappears in the strings
        for i in range(len(s)):
            # need to give a default value since the hashmap is initialized as empty with no key/value pairs
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            # need a default value incase the strings are the same length but do not have the same number of chars
            if countS[c] != countT.get(c, 0):
                return False
        return True
