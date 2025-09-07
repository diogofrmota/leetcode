import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] sumZero(int n) {
        List<Integer> list = new ArrayList<>();

        if (n % 2 != 0) {
            list.add(0);
        }

        for (int i = 1; i <= n/2; i++) {
            list.add(i);
            list.add(-i);
        }

        int[] result = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            result[i] = list.get(i);
        }
        return result;
    }
}