class Solution {
    public boolean solve(int i, int n, int[] arr, int k) {
        if (k == 0) 
            return true;
        }
        if (k < 0) {
            return false;
        }
        if (i == n) {
            return k == 0;
        }
        return solve(i + 1, n, arr, k - arr[i]) || solve(i + 1, n, arr, k);
    }

    public boolean checkSubsequenceSum(int[] nums, int target) {
        int n = nums.length; 
        return solve(0, n, nums, target); 
    }
}