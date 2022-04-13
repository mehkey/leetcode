class Solution
{
    public int divide(int dividend, int divisor)
	{
        if(dividend == Integer.MIN_VALUE && divisor == -1)
            return Integer.MAX_VALUE;
        
		int sign = (dividend < 0) ^ (divisor < 0) ? -1 : 1;
        int result = 0;
        int power = 32;
        long x = Math.abs((long)dividend);
        long y = Math.abs((long)divisor);
        
       while(x >= y)
		{
            while((y << power) > x)
			{
                power--;
            }
            x -= y << power;
            result += 1 << power;
        }
        return result * sign;
    }
}
