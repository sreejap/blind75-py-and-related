class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        mapping = {}

        for c in magazine:
            mapping[c] = mapping.get(c,0)+1
        
        for p in ransomNote:
            if mapping.get(p,0) == 0:
                return False
            else:
                mapping[p] -= 1 #You don’t need get because you already checked that mapping.get(p, 0) != 0, so we are updating here
                if mapping[p] == 0:
                    del mapping[p]
        
        return True
