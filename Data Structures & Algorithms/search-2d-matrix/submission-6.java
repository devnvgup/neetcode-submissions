class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        for (int i = 0 ; i < matrix.length;i++){
            boolean isFound = binarySearch(0,matrix[0].length-1,matrix[i],target);
            if (isFound){
                return true;
            }
        }
        return false;
    }
    public boolean binarySearch(int start, int end, int[]arr, int target){
        if (start > end){
            return false;
        }
        int mid = start + (end - start)/2;
        if (arr[mid] == target){
            return true;
        }
        if (target < arr[mid]){
            return binarySearch(start, mid - 1, arr, target);
        } else {
            return binarySearch(mid + 1, end, arr, target);
        }
    }
}
