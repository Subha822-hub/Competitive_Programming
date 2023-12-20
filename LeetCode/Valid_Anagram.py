class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        else:
            s=sorted(s)
            t=sorted(t)
            if s==t:
                return True
            else:
                return False