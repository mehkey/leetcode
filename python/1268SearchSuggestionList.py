class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        #print(products)
        
        l = 0
        r = len(products)-1

        answer = []
        
        for i in range(len(searchWord)):
            
            sub = searchWord[:i+1]
            
            while l <= r and sub != products[l][:i+1]:
                l += 1
            
            while l <= r and sub != products[r][:i+1]:
                r -= 1
            
            if l <= r:
                lis = []
                for i in range(l,min(l+3,r+1)):
                    lis.append(products[i])
                answer.append(lis)
            else:
                answer.append([])
            
        
        return answer



class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort()

        #print(products)
        
        l = 0
        r = len(products)-1

        answer = []
        
        for i in range(len(searchWord)):
            
            sub = searchWord[:i+1]
            
            while l <= r and sub != products[l][:i+1]:
                l += 1
            
            while l <= r and sub != products[r][:i+1]:
                r -= 1
            
            
            lis = []
            for i in range(l,min(l+3,r+1)):
                lis.append(products[i])
            answer.append(lis)
            
            
        
        return answer
            
        
        
        
        