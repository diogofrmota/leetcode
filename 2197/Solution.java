import java.util.*;
import java.math.BigInteger;

class Solution {
    public List<Integer> replaceNonCoprimes(int[] nums) {
        LinkedList<Integer> stack = new LinkedList<>();
        for (int num : nums) {
            stack.addLast(num);
            while (stack.size() >= 2) {
                int a = stack.get(stack.size() - 2);
                int b = stack.get(stack.size() - 1);
                int g = gcd(a, b);
                if (g > 1) {
                    stack.removeLast();
                    stack.removeLast();
                    long lcm = (long) a * b / g;
                    stack.addLast((int) lcm);
                } else {
                    break;
                }
            }
        }
        return stack;
    }
    
    private int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}