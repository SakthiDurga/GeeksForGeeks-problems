class Solution {
    public int countStudents(int[] arr, long pages) {
        int count = 1;
        long studentPage = 0;
        for (int i : arr) {
            if (studentPage + i <= pages) {
                studentPage += i;
            } else {
                count++;
                studentPage = i;
            }
        }
        return count;
    }
    public int findPages(int[] arr, int students) {
        if (students > arr.length)
            return -1;
        long low = 0;
        long high = 0;
        for (int i : arr) {
            low = Math.max(low, i);
            high += i;
        }
        while (low <= high) {
            long mid = low + (high - low) / 2;
            int count = countStudents(arr, mid);
            if (count > students) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
        return (int) low;
    }
}