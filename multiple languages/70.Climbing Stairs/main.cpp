class Solution {
public:
    int climbStairs(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;
        if (n == 2) return 2;
        int prev_prev = 1;
        int prev = 2;
        int result =0;
        for (int i =0; i<n-2; i++){
            result = prev_prev + prev;
            prev_prev = prev;
            prev = result;
        }
        return result;
    }
};