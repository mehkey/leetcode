res = []
        #c= CustomFunction()
        for i in range(1,z+1):
            for j in range(1,z+1):
                
                if customfunction.f(i, j) == z: #and (i < j or j <i):
                    res.append([i,j])
                    
        return res