class Solution {
    public boolean possible(int[] arr, int dist, int k){
        int count = 1, last = arr[0];
        for(int i = 1; i < arr.length; i++){
            if(arr[i] - last >= dist){
                count++;
                last = arr[i];
            }
            if(count >= k) return true;
        }
        return false;
    }
    public int aggressiveCows(int[] arr, int k) {
        // code here
        Arrays.sort(arr);
        int low = 0, high = arr[arr.length - 1] - arr[0];
        while(low <= high){
            int mid = low + (high - low) / 2;
            if(possible(arr, mid, k))
                low = mid + 1;
            else
                high = mid - 1;
        }
        return high;
    }
}