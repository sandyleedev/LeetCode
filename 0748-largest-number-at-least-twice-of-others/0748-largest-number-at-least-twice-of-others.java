class Solution {
    public int dominantIndex(int[] nums) {
        int index = -1;
        int max = 0;

        for (int i = 0; i < nums.length; i++){
            if (max < nums[i]){
                max = nums[i];
                index = i;
            }
        }

        for (int i = 0; i < nums.length ; i++){
            if (nums[i] != max && nums[i] * 2 > max){
                index = -1;
            }
        }

        return index;
    }
}