class Solution {
    int upperBound(int[] arr, int target) {
        // code here
        int left = 0, right = arr.length - 1, ans = arr.length;
        while (left <= right){
            int mid = left + (right - left) / 2;
            if(arr[mid] == target) left = mid + 1;
            else if(arr[mid] <= target) left = mid + 1;
            else{
                ans = mid;
                right = mid - 1;
            }
        }
        return ans;
    }
}