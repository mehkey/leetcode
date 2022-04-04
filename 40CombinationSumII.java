class Solution {

    public List<List<Integer>> combinationSum2(int[] candidate, int target) {
        Arrays.sort(candidate);
        List<List<Integer>> response = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        dfs(candidate, 0, target, path, response);
        return response;
    }

    private void dfs(int[] candidate, int cur, int target, List<Integer> path, List<List<Integer>> response) {
        if (target == 0) {
            response.add(new ArrayList(path));
            return ;
        }
        if (target < 0) return;
        for (int i = cur; i < candidate.length; i++){
            if (i > cur && candidate[i] == candidate[i-1]) continue;
            path.add(path.size(), candidate[i]);
            dfs(candidate, i+1, target - candidate[i], path, response);
            path.remove(path.size()-1);
        }
    }

    
}