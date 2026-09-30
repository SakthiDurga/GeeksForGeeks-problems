class Solution {
    public int median(int[][] mat) {
        // code here
        int n = mat.length, m = mat[0].length;
        int low = Integer.MAX_VALUE, high = Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            low = Math.min(low, mat[i][0]);
            high = Math.max(high, mat[i][m-1]);
        }
        int required = (n*m)/2;
        while(low <= high){
            int mid = low + (high - low)/2;
            int SmallerEquals = findSmaller(mat, mid);
            if(SmallerEquals <= required){
                low = mid + 1;
            } else{
                high = mid - 1;
            }
        }
        return low;
    }
    public int findSmaller(int[][] mat, int element){
        int count = 0;
        for(int i = 0; i < mat.length; i++){
            count += upperBound(mat[i], element);
        }
        return count;
    }
    public int upperBound(int[] arr, int target){
        int left = 0, right = arr.length - 1, ans = arr.length;
        while(left <= right){
            int mid = left + (right - left)/2;
            if(arr[mid] <= target)
                left = mid + 1;
            else{
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
}