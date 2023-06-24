class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        
        """
        
        
        
        """
        
        def canBeFormed(s,w):
            
            l1 = 0
            l2 = 0
            
            while l1 < len(s) and l2 < len(w):
                if s[l1] == w[l2]:
                    l2+= 1
                
                l1+=1
            
            if l2 == len(w):
                return True
            
            return False
        
        res = []
        maxLength = 0

        for w in dictionary:
            
            if canBeFormed(s,w):
                
                if len(w) > maxLength:
                    maxLength = len(w)
                    res = []
                    res.append(w)
                elif len(w) == maxLength: 
                    res.append(w)


        if len(res) == 1:
            return res[0]

        if len(res) > 0:
            return sorted(res)[0]
        
        return ''
        


        def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    return max(sorted(filter(isSubsequence, d)) + [''], key=len)
More efficient version (no sorting):

def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    return min(filter(isSubsequence, d) + [''], key=lambda x: (-len(x), x))
Different style:

def findLongestWord(self, s, d):
    best = ''
    for x in d:
        if (-len(x), x) < (-len(best), best):
            it = iter(s)
            if all(c in it for c in x):
                best = x
    return best
Optimized as suggested by @easton042, testing from longest to shortest and returning the first valid one without testing the rest:

def findLongestWord(self, s, d):
    def isSubsequence(x):
        it = iter(s)
        return all(c in it for c in x)
    d.sort(key=lambda x: (-len(x), x))
    return next(itertools.ifilter(isSubsequence, d), '')
Or:

def findLongestWord(self, s, d):
    for x in sorted(d, key=lambda x: (-len(x), x)):
        it = iter(s)
        if all(c in it for c in x):
            return x
    return ''
And taking that even further by not sorting unnecessarily much:

def findLongestWord(self, s, d):
    heap = [(-len(word), word) for word in d]
    heapq.heapify(heap)
    while heap:
        word = heapq.heappop(heap)[1]
        it = iter(s)
        if all(c in it for c in word):
            return word
    return ''


    public String findLongestWord(String s, List<String> d) {
    Collections.sort(d, (a,b) -> a.length() != b.length() ? -Integer.compare(a.length(), b.length()) :  a.compareTo(b));
    for (String dictWord : d) {
        int i = 0;
        for (char c : s.toCharArray()) 
            if (i < dictWord.length() && c == dictWord.charAt(i)) i++;
        if (i == dictWord.length()) return dictWord;
    }
    return "";
}