class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        #res = []
        strs.sort()
        hm = {}
        
        for word in strs:
            
            #hmkey = dict(Counter(word))

            #hmkey = frozenset(hmkey)
            
            count = [0] * 26
            
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            #if hmkey not in hm:
            #    hm[hmkey] = []
            
            if tuple(count) not in hm:
                hm[tuple(count)] = []
            
            hm[tuple(count)].append(word)
        
        return hm.values()
        
        """
        
        #res = []
        #strs.sort()
        hm = {}
        
        for word in strs:
            
            #hmkey = dict(Counter(word))

            #hmkey = frozenset(hmkey)
            
            
            count = {}
            
            for c in word:
                theid = ord(c) - ord('a')
                count[theid] = count.get(theid,0) + 1

            #if hmkey not in hm:
            #    hm[hmkey] = []
            
            string = str(OrderedDict(sorted( count.items(), key=lambda t: t[0])))
            
            #print(string)
            if string not in hm:
                hm[string] = []
            
            hm[string].append(word)
        
        return hm.values()
            """