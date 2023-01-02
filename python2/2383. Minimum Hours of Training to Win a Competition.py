class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        
        
        ans = 0
        
        for e in energy:
            while e >= initialEnergy:
                initialEnergy +=1
                ans +=1
            initialEnergy -=e

        for e in experience:
            while e >= initialExperience:
                initialExperience +=1
                ans +=1
            initialExperience +=e
        return ans

        
        
        
        
        
        
        
        
        
        """
        ans = 0
        n = len(energy)

        for i in range(n):
            while initialEnergy <= energy[i] or initialExperience <= experience[i]:
                if initialEnergy <= energy[i]:
                    initialEnergy += 1
                    ans += 1
                if initialExperience <= experience[i]:
                    initialExperience += 1
                    ans += 1
            initialEnergy -= energy[i]
            initialExperience += experience[i]
        
        return ans
    
        
        total = 0
        
        #s = sum(energy)
        
        cur = initialEnergy
        add1 = 0
        for i,j in enumerate(energy):
            #print(cur)
            if cur <= j:
                add = j - cur + 1
                add1 += add
                #print('add', add1)
                cur += add - j
            else:
                cur -= j
            
        
        cur = initialExperience
        add = 0
        for i,j in enumerate(experience):
            #print(cur)
            if cur <= j:
                curadd = j - cur + 1
                #print(curadd)
                add += curadd
                cur += curadd
            else:
                cur += j
            
        #print(add)
        #print(s - initialEnergy + 1)
        #print('  ')
        #print(add1)
        #print(add)
        
        return add1 + add
        """