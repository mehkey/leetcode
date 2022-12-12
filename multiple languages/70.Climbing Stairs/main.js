const climbStairs = (n: number): number => {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (n == 2) return 2;
    let prev_prev = 1;
    let prev = 2;
    let result =0;
    for (let i =0; i<n-2; i++){
        result = prev_prev + prev;
        prev_prev = prev;
        prev = result;
    }
    return result;

};