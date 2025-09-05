class Solution {
    public int makeTheIntegerZero(int num1, int num2) {
        long n1 = num1;
        long n2 = num2;
        for (int k = 1; k <= 100; k++) {
            long x = n1 - k * n2;
            if (x < k) {
                continue;
            }
            int bits = Long.bitCount(x);
            if (bits <= k) {
                return k;
            }
        }
        return -1;        
    }
}