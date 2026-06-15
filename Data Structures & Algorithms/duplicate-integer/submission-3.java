class Solution {
    public boolean hasDuplicate(int[] nums) {
        Map<Integer, String> map = new HashMap<>();
        for (Integer i: nums){
            if(map.containsKey(i)){
                return true;
            }
            map.put(i,"added");
        }
        return false;
    }
}