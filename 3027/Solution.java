import java.util.Arrays;

class Solution {
    public int numberOfPairs(int[][] points) {
        // Initialize n
        int n = points.length;

        // Sort points primarily by x (ascending), secondarily by y (descending)
        Arrays.sort(points, (a,b) -> {
            if (a[0] != b[0]) {
                return Integer.compare(a[0], b[0]);
            }
            return Integer.compare(b[1], a[1]);
        });

        int count = 0;

        for (int i = 0; i < n; i++) {
            int maxY = Integer.MIN_VALUE;

            for (int j = i + 1; j < n; j++) {
                // Check if Bob is below Alice and no other points are in between
                if (points[j][1] <= points[i][1] && points[j][1] > maxY) {
                    count++;
                    maxY = points[j][1];
                }
            }
        }

        return count;
    }
}