```java
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
```



```python
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        res = 0
        cur= [matrix[0][i] for i in range(len(matrix[0]))]

        for i in range(1,len(matrix)):
            new_cur = [0] * len(matrix[0])
            for j in range(len(matrix[0])):
                new_cur[j] = matrix[i][j] + min(cur[j-1] if j>0 else float('inf'),cur[j],cur[j+1] if j+1<len(matrix[0])else float('inf'))

            cur = new_cur
        return min(cur)

```


```typescript
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
```


```go
func minFallingPathSum(matrix [][]int) int {
	for i := 1; i < len(matrix); i++ {
		for j := 0; j < len(matrix[0]); j++ {

			if j == 0 {
				matrix[i][j] += min(matrix[i-1][j+1], matrix[i-1][j])
			} else if j+1 == len(matrix[0]) {
				matrix[i][j] += min(matrix[i-1][j-1], matrix[i-1][j])
			} else {
				matrix[i][j] += min(min(matrix[i-1][j-1], matrix[i-1][j]), matrix[i-1][j+1])
			}
		}
	}

	var m int = math.MaxInt32

	for _, val := range matrix[len(matrix)-1] {
		m = min(m, val)
	}
	return m

}

func min(a int, b int) int {
	if a < b {
		return a
	}
	return b
}
```