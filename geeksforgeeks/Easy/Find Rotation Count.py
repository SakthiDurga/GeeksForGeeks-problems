class Solution {
    public int findKRotation(int arr[]) {
        // Code here
        if(arr.length == 0) return -1;
        if(arr.length == 1) return 0;
        int left = 0, right = arr.length - 1;
        while(left < right){
            int midpoint = left + (right - left) / 2;
            if(midpoint > 0 && arr[midpoint] < arr[midpoint-1]){
                return midpoint;
            }
            else if(arr[left] <= arr[midpoint] && arr[midpoint] > arr[right]){
                left = midpoint + 1;
            } else{
                right = midpoint - 1;
            }
        }
        return left;
    }
}