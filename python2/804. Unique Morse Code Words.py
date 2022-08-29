class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        mc = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        #print([map(lambda w: [mc[x] for x in w],words)])

        #print([map(lambda w: [mc[x] for x in w],words)])

        #squared =  list(map(lambda w: mc[w],words))
        
        #squared =  list(reduce(lambda w,o: mc[w] + mc[w],words))

        s = set(map(lambda x: "".join([mc[ord(i) - ord('a')] for i in x]), words))
        
        return len(s)
        #print(s)

        #s = set([map(lambda w: [mc[x] for x in w],words)])

        

        #return len(s)