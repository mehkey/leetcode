const minFallingPathSum = (matrix: number[][]): number => {


    let cur:number[] = matrix[0];

    let new_cur:number[]  = new Array(matrix[0].length);
    for (let i = 1 ; i< matrix.length; i++) {
        new_cur = new Array(matrix[0].length);
        for (let j = 0; j < matrix[0].length; j++){
            new_cur[j] = matrix[i][j] + Math.min(Math.min(j>0 ? cur[j-1] : Number.MAX_VALUE,j+1<matrix[0].length ? cur[j+1]  : Number.MAX_VALUE), cur[j]);
        }
        cur = new_cur;
    }

    return Math.min(...cur);

};