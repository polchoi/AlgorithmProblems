class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        match = 0
        for i in range(len(s1)):
            count[s1[i]] = 1 + count.get(s1[i], 0)
        
        for r in range(len(s2)):
            if s2[r] in count:
                count[s2[r]] -= 1
                if count[s2[r]] == 0:
                    match += 1
            
            if r >= len(s1):
                if s2[r-len(s1)] in count:
                    if count[s2[r-len(s1)]] == 0:
                        match -= 1
                    count[s2[r-len(s1)]] += 1
            
            if match == len(count):
                return True
        
        return False
