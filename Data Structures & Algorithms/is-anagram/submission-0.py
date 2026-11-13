class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1={}
        freq2={}
        for x in s:
            freq1[x]=freq1.get(x,0)+1
        for y in t:
            freq2[y]=freq2.get(y,0)+1
        return freq1==freq2
                   

        


        