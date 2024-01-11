class Solution:
    def countCompleteSubstrings(self, w: str, k: int) -> int:
        def calc(s):
            res = 0
            v = len(s)
            for i in range(1, 27):
                if i * k > v: break
                l = i * k
                cnt = Counter(s[:l])
                freq = Counter(cnt.values())
                
                if freq[k] == i: res += 1
                
                for idx in range(v - l):
                    freq[cnt[s[idx]]] -= 1
                    cnt[s[idx]] -= 1
                    freq[cnt[s[idx]]] += 1

                    freq[cnt[s[idx+l]]] -= 1
                    cnt[s[idx+l]] += 1
                    freq[cnt[s[idx+l]]] += 1

                    if freq[k] == i: res += 1
            return res
        
        idx = 0
        ans = 0
        n = len(w)
        for i in range(1, n):
            if abs(ord(w[i]) - ord(w[i-1])) > 2:
                ans += calc(w[idx:i])
                idx = i
        ans += calc(w[idx:])
        return ans
        
        seen = {}
        running = [0] * 26
        seen[-1] = list(running)
        res = 0
        for id, char in enumerate(word):
            if id and abs(ord(char) - ord(word[id - 1])) > 2:
                # here we need to clear our memory because 
                # previous ones have become ineligible from here on as 
                # per the condition mentioned in the question
                running = [0] * 26
                seen = {}
                seen[id - 1] = list(running)
            this = ord(char) - ord('a')
            running[this] += 1
            j = id - k
            if running[this] >= k:
                while j in seen and j >= (id - 26 * k):
                    res += all((x - y) in (0, k) for x, y in zip(running, seen[j]))
                    j -= k
            seen[id] = list(running)
        return res


        count = 0
        unique_chars = len(set(word))

        for sub_len in range(1, unique_chars + 1):
            window_size = sub_len * k
            char_freq = {}
            start = 0
            end = start + window_size - 1

            for i in range(start, min(end, len(word))):
                char_freq[word[i]] = char_freq.get(word[i], 0) + 1

            while end < len(word):
                if self.has_equal_frequency(char_freq, k) and self.has_adjacent_difference_at_most_two(word, start, end):
                    count += 1
                #print(start)
                char_freq[word[start]] -= 1
                start += 1
                end += 1

                if window_size < len(word):
                    char_freq[word[end]] = char_freq.get(word[end], 0) + 1

        return count

    def has_equal_frequency(self, char_freq, k):
        for value in char_freq.values():
            if value != k and value != 0:
                return False
        return True

    def has_adjacent_difference_at_most_two(self, word, start, end):
        for i in range(start + 1, end + 1):
            if abs(ord(word[i]) - ord(word[i - 1])) > 2:
                return False
        return True
        
        n = len(word)
        l = 0
        res = 0
        
        r = 0

        resind = []
        count = 0

        def check(h):
            s = set()
            for v in h.values():
                if v != k:
                    return False
            return True
        
        def check2(start,end):
            for i in range(start,end):
                if abs(ord(word[i]) - ord(word[i+1])) > 2:
                    return False
            return True

        for r in range(1*k,27*k,k):
            
            d = Counter()
            
            if r > n:
                break

            '''
            for j in range(0,r):
                d[word[j]] += 1

            if check(d) and check2(0,r-1):
                #print('HERE',0,r-1)
                count+=1
            '''
            #last = word[r-1]
            last= '$' #word[0]
            #print(d)
            s = r
            
            while s < n:
            #for s in range(r,n):
                if abs(ord(last) - ord(word[s])) > 2:
                    d = Counter()
                    if s+r >= n:
                        break
                    for j in range(s,min(s+r,n)):
                        d[word[j]] += 1

                    if check(d) and check2(s,s+r-1):
                        #print('HERE',0,r-1)
                        count+=1
                    s = s+r
                    last = word[s+r-1]
                    continue

                d[word[s-r]] -= 1
                d[word[s]] += 1
                if d[word[s-r]] == 0:
                    del d[word[s-r]]
                #print(d)
                if check(d) and abs(ord(last) - ord(word[s])) < 2:
                    #print('HERE',s-r+1,s)
                    count+=1
                past= word[s]
                s += 1
        return count




        return d

        
        return 0

        while r < n:

            d[word[r]] += 1

            if l < n and all([v == k for v in d.values()]) :
                res += 1
                d[word[l]] -= 1
                l+=1

            r+= 1

        return res
