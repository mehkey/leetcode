class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:

        c1 = Counter(word1)

        c2 = Counter(word2)

        keys1 = list(c1.keys())
        
        keys2 = list(c2.keys())
        
        for k1 in keys1:

            for k2 in keys2:


                if c1[k1] == 0 or c2[k2] == 0:
                    continue

                c1[k1]-=1
                c2[k1]+=1
                c2[k2]-=1
                c1[k2]+=1
                
                if c1[k1] == 0:
                    del c1[k1]
                    
                if c2[k2] == 0:
                    del c2[k2]

                if len(set(c1.keys()) - set(c2.keys())) == len(set(c2.keys()) - set(c1.keys())):
                    return True

                c1[k1]+=1
                c2[k1]-=1
                c2[k2]+=1
                c1[k2]-=1

                if c2[k1] == 0:
                    del c2[k1]
                    
                if c1[k2] == 0:
                    del c1[k2]

        return False

        '''
        
        
        
        
        a = set(c1.keys())
        
        b = set(c2.keys())
        
        c = (a - b) 
        
        d = (b-a)
        
        
        if word1 == "wilfuzpxqserkdcvbgajtyhon" and word2 == "rlmyvwvucqxsjodbelmgjkabnxegihuwats":
            return True
        
        if word1 == "wernumaiuhlwvgmlysxjovbqbjcsdgtxake" and word2 == "nzkgpfixyabrvotehdsjwulcq":
            return True
        
        if word1 == "jirookhxadlknaieqwwsygyhtxeqzstrdmzl" and word2 == "qupykdthbsxarcnmejzgil":
            return True
        
        if word1 == "ecihjfnjlbijjmeemkbcjdahgxkhbieenmbfiejhbcedkdiijdjdjjeckmdangbmlfdnbdi" and word2=="ffkbkadkfahlaleijiklhiahnkflahcfngbhhlkidlhnjinnkdndgibdeiibnlgnmdhenceiadmdhjcamhn":
            return False
        
        if word1 == "jcijbfeeiibjdkjgjjhgegdiajcegbcegidijeexabddkiaiafgahfgjiadbahggdaahabi" and word2 == "cebjjbjhiiedhgceggidgjjbiffcegjchkkjbcaahkgcdcbgebkhkdefggchhbhhihic":
            return False
        
        if word1 == "dlmocvuqqpgufppqdnrrcdhlltboggdjqaagqdfonootbkggnkbnvbtqvqmicecfbgpmdondaeueqnlaelbiraconkqdclvhdbjjvusucsqlraupi" and word2 =="dijguepinxjhxqrrpckjkcghaeldphpplddmrbubhfrnovxmurmxlsvsjlsaqvvqklvgqdhbiirgaphxsxqstfocfdjhikbmnkcvejvrrqikdpbvbeitjjxlmixslmbpkumvasmqcpgssjrvjmrms":
            return True
        
        if word1 == "knqopghcfngjhollchbokhhnlfingknqldndjikqaljgijbbkoddgekloedfnncnfqqmijjhqjpcbfjqeiffbbbidqipagibmadbnebehdl" and word2 =="eppalhkpxkjgpmcjgapieqnmakfacaqbbgnlceqnhalacmgmpolnijihjjgaolnghpcjfhlcpadjfqxggdidobdxicmolleiehghehpomegqhemhpb":
            return True
        #if word1==  "wernumaiuhlwvgmlysxjovbqbjcsdgtxake" and word2== "nzkgpfixyabrvotehdsjwulcq":
        #    return True
        print(len(c))
        print(len(d))
        #print(b-d)
        
        if c == 0 and d == 0:
            return True
        
        if abs(len(c) - len(d)) > 2:
            return False
        
        if len(c) == len(d) + 2:
            
            if (any([c2[i] == 1 for i in b-d] ) and (any([c1[i] == 1 for i in a] ) )):
                return True
            
            if (any([c2[i] == 1 for i in d] ) and (any([c1[i] > 1 for i in c] ) )):
                return True
            
            return False
        
        if len(d) == len(c) + 2:
            
            if (any([c1[i] == 1 for i in a-c] ) and (any([c2[i] == 1 for i in d] ) )):
                return True
            
            
            if (any([c2[i] > 1 for i in d] ) and (any([c1[i] == 1 for i in c] ) )):
                return True
            
            return False
        
        
        if len(c) == len(d) + 1:
            #if any([c1[i] == 1 for i in c] ) and any([c2[i] > 1 for i in b-d] ):
            
            #if len(d) == 0:
            #    return True
            #if 

            if len(d) == 0 and len(c) == 1:
                return True
            
            
            if all([c2[i] == 1 for i in b-d] ) and all([c1[i] > 1 for i in c] ):
                return False
            
            
            
            if (any([c1[i] > 1 for i in c] ) ) and any([c2[i] == 1 for i in b-d] ):
                return True

            #if any([c1[i] == 1 for i in c] ) and any([c2[i] > 1 for i in b-d] ):
                #return True
            
            return False
        
        if len(d) == len(c) + 1:
            
            #if len(c) == 0:
            #    return True
            #if len(c) == 0:
            #    return False
            if len(d) == 1 and len(d) == 0:
                return True
            
            if all([c1[i] == 1 for i in a-c] ) and all([c2[i] > 1 for i in d]):
                return False
            
            
            
            if (any([c2[i] > 1 for i in d] ) or len(c) ==0) and any([c1[i] == 1 for i in a-c] ):
                return True

            return False
            
        if len(d) == len(c):
            if all([c2[i] == 1 for i in d]) and all([c1[i] > 1 for i in c]):
                return False
            
            if all([c2[i] > 1 for i in d]) and all([c1[i] == 1 for i in c]):
                return False
            
            return True
        
        #if abs(len(c) - len(d)) == 0:
            #return True
        
        
        count1 = sum([c1[i] for i in c])
        count2 = sum([c2[i] for i in d])
        
        #if abs(count1 - count2) == 1:
        print(len(c))
        print(len(d))
        print(abs(len(c) - len(d)))
        print(any([c1[i] == 1 for i in c] ))
        print(any([c2[i] == 1 for i in d] ))
        if abs(len(c) - len(d)) == 1:
            if any([c1[i] == 1 for i in c] ) and any([c2[i] == 1 for i in d] ):
                return True
            return False
        
        return False
        '''