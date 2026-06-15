class Solution {
    public int[] topKFrequent(int[] nums, int k) {
         Map<Integer, Integer> map = new HashMap();
        for (int el : nums) {
            if (!map.containsKey(el)) {
                map.put(el, 1);
            } else {
                int value = map.get(el);
                map.put(el, ++value);
            }
        }
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(map.entrySet());
        list.sort(Map.Entry.comparingByValue());
        Map<Integer, Integer> sortedMap = new LinkedHashMap<>();
        for (Map.Entry<Integer, Integer> entry : list) {
            sortedMap.put(entry.getKey(), entry.getValue());
        }
        List<Integer> keys = new ArrayList<>(sortedMap.keySet());
        List<Integer> sublist = keys.subList(keys.size() - k, keys.size());
        int[] arr = new int[sublist.size()];
        for (int i = 0; i < sublist.size(); i++) {
            arr[i] = sublist.get(i);
        }
        return arr;
    
    }
}
