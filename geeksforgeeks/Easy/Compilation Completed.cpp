class Solution {
    public int findCeil(int[] arr, int x) {
        // code here
        int left = 0, right = arr.length - 1, res = -1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(arr[mid] < x){
                left = mid + 1;
            } else{
                 res = mid;
                 right = mid - 1;
            }
        }
        return res;
    }
}