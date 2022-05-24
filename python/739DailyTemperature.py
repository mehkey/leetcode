
def dailyTemperature(self, temperatures):
    
    stack = [] # array of arrays

    output = [0] * len(temperatures)

    for i in range(len(temperatures)):
        t = temperatures[i]

        while len(stack) > 0  and stack[-1][0] > t:
            val = stack.pop()       
            output[val[1]] = i - val[1]

        stack.append([t,i])
    
    return output