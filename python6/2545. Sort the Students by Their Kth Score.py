
import numpy as np

class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        a = np.array(score)

        return a[a[:, k].argsort()[::-1]]


Java

    public int[][] sortTheStudents(int[][] A, int k) {
        Arrays.sort(A, (a, b) -> b[k] - a[k]);
        return A;
    }
C++

    vector<vector<int>> sortTheStudents(vector<vector<int>>& A, int k) {
        sort(A.begin(), A.end(), [&](auto const & a, auto const & b) {
            return a[k] > b[k];
        });
        return A;
    }
Python
return new copy

    def sortTheStudents(self, A, k):
        return sorted(A, key=lambda a: -a[k])