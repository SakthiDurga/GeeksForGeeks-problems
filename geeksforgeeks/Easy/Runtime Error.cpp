class Solution {
    static int findFloor(int[] arr, int x) {
        // code here
        int left = 0, right = arr.length - 1, res = -1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(arr[mid] <= x){
                res = mid;
                left = mid + 1;
            } else{
                right = mid - 1;
            }
        }
        return res;
    }
}
