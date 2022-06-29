class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        
        """
            
            What is the leading number?
            
            Find the minimum number of switch such that either the top is all min or the bottom is all min
        
            runtime: O(n)  space: O(n)
        
        """

        ct = Counter(tops)
        cb = Counter(bottoms)
        call = ct + cb
        
        l = len(tops)
        
        m = c =  0

        for k in call:
            if call[k] > c:
                m = k
                c = call[k]

        if c < l - 1:
            return -1
        
        for i in range(l):
            if tops[i] != m and bottoms[i] !=m:
                return -1
        
        return min(l - ct[m], l - cb[m])
            
        
        
        
        #more clean solution
        
        
        public int minDominoRotations(int[] A, int[] B) {
        int ans = min(
                f(A[0], A, B),
                f(B[0], A, B),
                f(A[0], B, A),
                f(B[0], B, A));
            return ans == Integer.MAX_VALUE ? -1 : ans;
        }

        private int min(int a, int b, int c, int d) {
            return Math.min(Math.min(Math.min(a, b), c), d);
        }

        /* Count number of rotations to make values in A equal to target. */
        private int f(int target, int[] A, int[] B) {
            int swap = 0;
            for (int i = 0; i < A.length; i++) {
                if (A[i] != target) {
                    if (B[i] != target) {
                        return Integer.MAX_VALUE;
                    } else {
                        swap++;
                    }
                }
            }
            return swap;
        }

        
        