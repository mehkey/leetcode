class Solution {
    public int removeElement(int[] nums, int elem) {
        int len = nums.length;
        for (int i = 0 ; i< len; ++i){
            while (nums[i]==elem && i< len) {
                nums[i]=nums[--len];
            }
        }
        return len;
    }
}


