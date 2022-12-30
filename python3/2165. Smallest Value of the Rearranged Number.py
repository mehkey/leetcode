class Solution:
    def smallestNumber(self, num: int) -> int:
        
        s = sorted(str(abs(a)))
        if a <= 0:
            return -int(''.join(s[::-1]))
        i = next(i for i,a in enumerate(s) if a > '0')
        s[i], s[0] = s[0], s[i]
        return int(''.join(s))



        if num==0:
            return 0
        if num>=0:
            num=str(num)
            num=sorted(num)
            ans=''
            z=num.count('0')
            for i in range(z):
                num.pop(0)
            if len(num)>0:
                ans+=num[0]
            ans+='0'*z
            for i in range(1,len(num)):
                ans+=num[i]
        else:
            num=str(num)
            num=sorted(num[1:])
            num.sort(reverse=True)
            ans='-'
            for i in range(len(num)):
                ans+=num[i]
        return ans