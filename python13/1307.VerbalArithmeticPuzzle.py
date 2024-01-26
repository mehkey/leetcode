class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        
        var = {}
        digits = set()
        
        def check(column, carry):
            s = sum((var[w[-1-column]] for w in words if len(w) > column)) + carry
            c = result[-1-column]
            if c in var:
                if var[c] != s % 10:
                    return -1, False
                else:
                    return s // 10, False
            if s % 10 == 0 and c in leadings:
                return -1, False
            if s % 10 in digits:
                return -1, False
            var[c] = s % 10
            digits.add(s % 10)
            return s // 10, c

        def dfs(column, word_id, carry):
            reset = False
            if word_id >= len(words):
                carry, reset = check(column, carry)
                if carry < 0:
                    return False
                word_id = 0
                column += 1
            if column >= len(result):
                if carry == 0:
                    return True
            elif len(words[word_id]) <= column or words[word_id][-1-column] in var:
                if dfs(column, word_id+1, carry):
                    return True
            else:
                c = words[word_id][-1-column]
                for d in range(10):
                    if (d in digits) or (d == 0 and c in leadings):
                        continue
                    digits.add(d)
                    var[c] = d
                    if dfs(column, word_id+1, carry):
                        return True
                    digits.remove(d)
                    del var[c]
            if reset != False:
                digits.remove(var[reset])
                del var[reset]
            return False

        leadings = set([w[0] for w in words + [result] if len(w) > 1])
        if any(len(w) > len(result) for w in words):
            return False
        return dfs(0, 0, 0)

        letters = set([l for word in words for l in word] + [l for l in result])
        let = list(sorted(letters))
        #print(let)
        N = len(let)
        
        avail = set(range(0,10))
        #mmmm = {'D': 0, 'E': 1, 'M': 2, 'N': 3, 'O': 4, 'R': 5, 'S': 6}
        #mmmm = {'D': 7, 'E': 5, 'M': 1, 'N': 6, 'O': 4, 'R': 5, 'S': 9}
        
        
        def solve(mm):

            s = 0
            #print(mm)
            for w in words:

                sss = 0
                i = len(w)-1
                for l in w:
                    sss +=  mm[l] * 10 ** i
                    i-=1
                s += sss

            s1 = 0
            sss = 0
            i = len(result)-1
            for l in result:
                sss +=  mm[l] * 10 ** i
                i-=1
            s2 = sss

            return s == s1
        
        #print(solve(mmmm))
        
        m = {}
        ss = avail
        def tr(i,ss):
            if i == N:
                if solve(m):
                    return True
                else:
                    return False
            
            for v in list(ss):
                #print(i)
                m[let[i]] = v
                ss.remove(v)
                if tr(i+1,ss):
                    return True
                ss.add(v)
                del m[let[i]]

            return False

        return tr(0,ss)
