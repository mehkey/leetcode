class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        

        def countUnique( n) :
            if (n < 1): return 0
            cur = 9
            nine = 9
            while(n-1 > 0) :
                if (nine == 0) :
                    return 0
                cur = cur* nine
                nine-=1
                n -=1
            return cur
        
        
        def isUniqueDigits( n) :
            u = set()
            if (n < 10) :
                return True
            while (n > 0) :
                digit = n % 10
                if digit in u:
                    return False
                u.add(digit)
                n = n // 10

            return True

        used = defaultdict(int)
        
        s = str(n)
            
        res = 0
        
        N = len(s)
            
        
        for i in range(1,N):

            res += countUnique(i)
        
        res += (int(s[0]) -1) * factorial(9) // factorial( 9 - N + 1)

        used[int(s[0])] = 1
        
                
        for i in range(1,N):
            count = 0
            for j in range(0,int(s[i])):
                if used[j] != 1:
                    count+=1
            res += count * factorial(9-i) // factorial(9 - N + 1)
                        
            used[int(s[i])] = 1

        
        if (isUniqueDigits(n)) :
            res += 1

        return res




class Solution {

     public int toInt(char ch) {
        return ch - '0';
    }
    
    public int factorial(int n) {
        if (n < 2) return 1;
        int res = 1;            
        for (int i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }
    
    public int uniqueDigits(int n) {
        if (n < 1) return 0;
        int cur = 9;
        int numOptions = 9;
        while(--n > 0) {
            if (numOptions == 0) {
                return 0;
            }
            cur = cur* numOptions;
            numOptions--;
            
        }
        return cur;
    }
    
    public int countSpecialNumbers(int n) {

        int[] u = new int[10];
        String seq = String.valueOf(n);
        char[] ca = seq.toCharArray();
        int res = 0;

        for (int i = 1; i <= ca.length - 1; i++) {
            res += uniqueDigits(i);
        }
        System.out.println(res);
        res += (toInt(ca[0]) - 1) * factorial(9) / factorial(9 - ca.length + 1);
        System.out.println(res);
        u[toInt(ca[0])] = 1;
        for (int i = 1; i < ca.length; i++) {
            int count = 0;
            for (int j = 0; j < toInt(ca[i]); j++) {
                if (u[j] != 1) count++;
            }
            System.out.println(count);
            System.out.println(res);
            res += count * factorial(9 - i) / factorial(9 - ca.length + 1);
            if (u[toInt(ca[i])] == 1)
                break;
            u[toInt(ca[i])] = 1;
        }
        
        if (isUniqueDigits(n)) {
            res += 1;
        }
        return res;
    }


    public boolean isUniqueDigits(int n) {
        int[] u = new int[10];
        if (n < 10) return true;
        while (n > 0) {
            int digit = n % 10;
            if (u[digit] == 1)
                return false;
            u[digit] = 1;
            n = n / 10;
        }
        return true;
    }

}



class Solution {

     public int toInt(char ch) {
        return ch - '0';
    }
    
    public int factorial(int n) {
        if (n < 2) return 1;
        int res = 1;            
        for (int i = 2; i <= n; i++) {
            res *= i;
        }
        return res;
    }
    
    public int uniqueDigits(int n) {
        if (n < 1) return 0;
        int cur = 9;
        int numOptions = 9;
        while(--n > 0) {
            if (numOptions == 0) {
                return 0;
            }
            cur = cur* numOptions;
            numOptions--;
            
        }
        return cur;
    }
    
    public int countSpecialNumbers(int n) {

        int[] u = new int[10];
        String seq = String.valueOf(n);
        char[] ca = seq.toCharArray();
        int res = 0;

        for (int i = 1; i <= ca.length - 1; i++) {
            res += uniqueDigits(i);
        }

        res += (toInt(ca[0]) - 1) * factorial(9) / factorial(9 - ca.length + 1);
        u[toInt(ca[0])] = 1;
        for (int i = 1; i < ca.length; i++) {
            int count = 0;
            for (int j = 0; j < toInt(ca[i]); j++) {
                if (u[j] != 1) count++;
            }
            res += count * factorial(9 - i) / factorial(9 - ca.length + 1);
            if (u[toInt(ca[i])] == 1)
                break;
            u[toInt(ca[i])] = 1;
        }
        
        if (isUniqueDigits(n)) {
            res += 1;
        }
        return res;
    }


    public boolean isUniqueDigits(int n) {
        int[] u = new int[10];
        if (n < 10) return true;
        while (n > 0) {
            int digit = n % 10;
            if (u[digit] == 1)
                return false;
            u[digit] = 1;
            n = n / 10;
        }
        return true;
    }

}