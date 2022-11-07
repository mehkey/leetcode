class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        
        
        rl = len(mat)
        cl = len(mat[0])
        
        
        arr = [i for i in range(cl)]
        

        def count_0(mat):
            total = 0
            for i in range(rl):
                count = 0
                for j in range(cl):
                    if mat[i][j] == 0:
                        count+=1
                if count == cl:
                    total+=1
            
            return total
        
        m = 0

        for a in itertools.combinations(arr,cols):
            c = copy.deepcopy(mat)
            print(c)
            
            for j in a:
                for i in range(rl):
                    c[i][j] = 0

            m = max(m, count_0(c))

        return m

        '''def count_0(mat):
            total = 0
            for i in range(rl):
                count = 0
                for j in range(cl):
                    if mat[i][j] == 0:
                        count+=1
                if count == cl:
                    total+=1
            
            return total
                    
        def fill_0(mat,col):
            for i in range(rl):
                mat[i][col] = 0
        
        def count_1(mat,col):
            total = 0
            for i in range(rl):
                total += mat[i][col]
            
            return total
        
        def count_2(mat,row):
            total = 0
            for j in range(cl):
                total += mat[row][j]
            
            return total
        
        if cols == 0:
            return 0
        
        while True:

            
            max_val = 0
            max_col = 0
            
            for j in range(cl):
                count = count_1(mat,j) 
                #print(j, count)
                if count > max_val:
                    max_val = count
                    max_col = j
            
            
            min_v = float('inf')
            min_c = 0
            for i in range(rl):
                count = count_2(mat,i)
                if count >0 and min_v < count:
                    min_v = count
                    min_c = i

                elif count >0 and min_v == count:
                    min_v = count
                    min_c = i
            
            if min_v <= cols:
                
                for k in range(rl):
                    if i == k:
                        for j in range(cl):
                            if mat[k][j] == 1:
                                fill_0(mat,j)

                cols -= min_v
            else:
                break
                
            
            
            
            
                    
            
            #print('fill ' , j)
            #print('val ' , max_val)
            #if 
            #fill_0(mat,max_col)
            #print(mat)

            
        #print(count_0(mat))
        
        return count_0(mat)
        
        
        #rl = len(mat)
        #cl = len(mat[0])
        
        
        
        
        
        
        def int_to_binary(integer):
            binary_string = ''
            while(integer > 0):
                digit = integer % 2
                binary_string += str(digit)
                integer = integer // 2
            binary_string = binary_string[::-1]
            return binary_string
        
        rl = len(mat)
        cl = len(mat[0])
        
        c = [0] * len(mat[0])
        
        for j in range(cl):
            for i in range(rl):
                c[j] = c[j] | mat[i][j] << i
        
        c = set(c)
        
        for i in range(cols):
            
            #nums[i] == 0
            
        #print(list(map(int_to_binary,c )))
        
        
        rl = len(mat)
        cl = len(mat[0])
        #c = [False] * rl
        
        t = 0
        
        
        for k in range(rl):
            c = 0
            print("k " , k)
            
            for j in range(cl):
                #print("j " , j)
                for i in range(rl):
                    if i != k:
                        #print(i,j,mat[i][j])
                        if mat[i][j] == 1:
                            print('count')
                            c+=1
                            break
                
            
            if c == cl:
                print('found')
                t+=1
        
        return t

        
        for i in range(cl):
            
            for j in range(rl):
                
                if mat[j][i] == 1:
                    c[j] = True
        
        print(c)
        '''
                