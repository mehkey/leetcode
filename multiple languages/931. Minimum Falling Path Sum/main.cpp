class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {

        int i = 0;

        for (int i = 1 ; i< matrix.size(); i++) {

            for (int j = 0; j < matrix[0].size(); j++){
                matrix[i][j] = matrix[i][j] + min(min(j>0 ? matrix[i-1][j-1] : INT_MAX,j+1<matrix[0].size() ? matrix[i-1][j+1]  : INT_MAX), matrix[i-1][j]);
            }

        }

        return *min_element(matrix.back().begin(), matrix.back().end());

    }
};