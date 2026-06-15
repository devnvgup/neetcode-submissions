class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Input: numbers = [1,2,3,4,7], target = 9
        // Output: [1,2]
        // i = 0
        int i = 0;
        // j = len - 1
        int j = numbers.length - 1;
        // loop , condion i < j
        while (i < j) {
            // if numsber[i] + number[j] > target
            // j --
            if (numbers[i] + numbers[j] > target) {
                j--;
            } else if (numbers[i] + numbers[j] < target) {
                // else > target
                // i ++
                i++;
            } else {
                return new int[]{i+1,j+1};
            }
            // else == target
            // return [i+1;j+1]
        }
        return new int[]{};
    }
}
