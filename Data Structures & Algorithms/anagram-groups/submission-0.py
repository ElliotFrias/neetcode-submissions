class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicts = {}
        resp = []
        for pal in strs:
            aspTupla = [0]*26
            for letter in pal:
                aspTupla[ord(letter) - ord('a')] += 1
            tupla = tuple(aspTupla)
            if tupla in dicts:
                dicts[tupla].append(pal)
            else:
                dicts[tupla] = [pal]
        
        for values in dicts:
            resp.append(dicts[values])

        return resp