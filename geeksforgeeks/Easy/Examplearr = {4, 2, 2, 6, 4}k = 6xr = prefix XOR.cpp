class Solution {
    public long subarrayXor(int arr[], int k) {
        // code here
        HashMap<Integer, Integer> map  = new HashMap();
        int result = 0, xor = 0;
        map.put(0,1);
        for(int i = 0; i < arr.length; i++){
            xor ^= arr[i];
            if(map.containsKey(xor^k)){
                result += map.get(xor^k);
            }
            map.put(xor, map.getOrDefault(xor,0)+1);
        }
        return result;
    }
}