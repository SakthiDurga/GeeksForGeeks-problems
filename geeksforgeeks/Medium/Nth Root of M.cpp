class Solution {
    public int nthRoot(int n, int m) {
        // code here
        if (m==0) return 0;
        int left = 1, right = m;
        while(left <= right){
            int mid = left + (right - left) / 2;
            long power = 1;
            for(int i = 1; i <= n; i++){
                power *= mid;
                if(power > m){
                    break;
                }
            }
            if(power == m) return mid;
            else if (power > m) right = mid - 1;
            else left = mid + 1;
        }
        return -1;
    }
}