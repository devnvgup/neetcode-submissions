class Solution {
    List<List<Integer>> res = new ArrayList<List<Integer>>();
    public List<List<Integer>> subsets(int[] nums) {
        backtrack(nums, 0, new ArrayList<>());
        return res;
    }

    public void backtrack(int[]nums, int start, List path){
        res.add(new ArrayList<Integer>(path));
        for (int i = start ; i < nums.length ; i++){
            // add
            path.add(nums[i]);
            // recursive
            backtrack(nums, i+1, path);
            // remove
            path.remove(path.size()-1);
        }
    }
}

