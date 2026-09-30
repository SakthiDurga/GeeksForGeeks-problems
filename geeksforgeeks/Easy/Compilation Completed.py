class Solution {
    public long inversionCount(int arr[]) {
        // code here
        return mergeSort(arr, 0, arr.length-1);
    }
    public long mergeSort(int[] arr, int left, int right){
        long count = 0;
        if(left < right){
            int mid = (left + right)/2;
            count += mergeSort(arr, left, mid);
            count += mergeSort(arr, mid+1, right);
            count += merge(arr, left, mid, right);
        }
        return count;
    }
    public long merge(int[] arr, int left, int mid, int right){
        int[] leftArr = Arrays.copyOfRange(arr, left, mid+1);
        int[] rightArr = Arrays.copyOfRange(arr, mid+1, right+1);
        int i = 0, j = 0, k = left;
        long count = 0;
        while(i < leftArr.length && j < rightArr.length){
            if(leftArr[i] <= rightArr[j]){
                arr[k++] = leftArr[i++];
            } else{
                arr[k++] = rightArr[j++];
                count += (leftArr.length - i);
            }
        }
        while(i < leftArr.length){
            arr[k++] = leftArr[i++];
        }
        while(j < rightArr.length){
            arr[k++] = rightArr[j++];
        }
        return count;
    }
}