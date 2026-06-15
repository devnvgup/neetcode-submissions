class Solution {
    public int[] productExceptSelf(int[] nums) {
        int countZero = 0;
        int totalProduct = 1;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                // caculate zero
                countZero++;
            } else {
                // caculate total product except zero value
                totalProduct *= nums[i];
            }
        }
        int[] res = new int[nums.length];
        if (countZero > 1) {
            return new int[nums.length];
        } else if (countZero == 1) {
            for (int i = 0; i < nums.length; i++) {
                if (nums[i] != 0) {
                    res[i] = 0;
                } else {
                    res[i] = totalProduct;
                }
            }
        } else {
            for (int i = 0; i < nums.length; i++) {
                res[i] = totalProduct / nums[i];
            }
        }
        return res;
    }
}  
