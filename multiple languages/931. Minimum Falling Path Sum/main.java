class Solution {
    public int minFallingPathSum(int[][] matrix) {

        int res = 0;
        int[] row1 = matrix[0];

        int[] cur = matrix[0];

        int[] new_cur = new int[matrix[0].length];
        for (int i = 1 ; i< matrix.length; i++) {
            new_cur = new int[matrix[0].length];
            for (int j = 0; j < matrix[0].length; j++){
                new_cur[j] = matrix[i][j] + Math.min(Math.min(j>0 ? cur[j-1] : Integer.MAX_VALUE,j+1<matrix[0].length ? cur[j+1]  : Integer.MAX_VALUE), cur[j]);
            }
            cur = new_cur;
        }

        return Arrays.stream(cur).min().getAsInt();
    }
}