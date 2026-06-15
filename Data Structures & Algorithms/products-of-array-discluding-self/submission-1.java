class Solution {
    public int[] productExceptSelf(int[] nums) {
         int[] res = new int[nums.length];
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < nums.length; i++) {
            int j = i + 1;
            int result = 1;
            while (j <= nums.length - 1) {
                result *= nums[j];
                j++;
            }
            for (Integer item : stack) {
                result *= item;
            }
            stack.push(nums[i]);
            res[i] = result;
        }
        return res;
    }
}  
