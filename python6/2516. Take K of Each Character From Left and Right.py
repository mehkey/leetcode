class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        '''
        ra = s.count('a') - k
        rb = s.count('b') - k
        rc = s.count('c') - k
        
		# if any of them is less than 0, it means there are less than k occurences of a character.
        if any(i < 0 for i in [ra, rb, rc]):
            return -1
        
        hm = defaultdict(int)
        length = left = res = 0

        for right in s:
            
            hm[right] += 1
            length += 1
            
            print(hm)
            print(length)

            while hm['a'] > ra or hm['b'] > rb or hm['c'] > rc:
                hm[s[left]] -= 1
                length -= 1
                left += 1

                print('hminside', hm)
                print(length)

            print("SETTING RES", length)
            res = max(res, length)

        return len(s) - res
        '''

        dict1 = Counter(s)

        if dict1["a"] < k or dict1["b"] < k or dict1["c"] < k:
            return -1

        min_val, left = len(s), 0

        for right in range(len(s)):
            dict1[s[right]] -= 1
            print(dict1)
            while left <= right and (dict1["a"] < k or dict1["b"] < k or dict1["c"] < k):
                dict1[s[left]] += 1
                left += 1

            print(dict1)
            print( dict1["a"] + dict1["b"] + dict1["c"])

            min_val = min(min_val, dict1["a"] + dict1["b"] + dict1["c"])

        return min_val
