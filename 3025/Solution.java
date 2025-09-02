import java.util.Arrays;

class Solution {
    public int numberOfPairs(int[][] points) {
        int numberOfPoints = points.length;

        // Sort points by x ascending, and for same x, by y descending
        Arrays.sort(points, (a, b) -> {
            if (a[0] == b[0]) {
                return b[1] - a[1]; // y descending
            }
            return a[0] - b[0]; // x ascending
        });

        int totalCount = 0;

        // Iterate through each point as candidate A
        for (int i = 0; i < numberOfPoints; i++) {
            int x_A = points[i][0];
            int y_A = points[i][1];

            // For each candidate A, iterate through points with larger or equal x as candidate B
            for (int j = i + 1; j < numberOfPoints; j++) {
                int x_B = points[j][0];
                int y_B = points[j][1];

                // Check if A is truly upper left of B (x_A <= x_B and y_A >= y_B)
                if (y_A >= y_B) {
                    boolean valid = true;

                    // Check ALL other points to see if any fall inside or on the border of the rectangle
                    for (int k = 0; k < numberOfPoints; k++) {
                        if (k == i || k == j) continue; // Skip points A and B themselves
                        
                        int x_C = points[k][0];
                        int y_C = points[k][1];

                        // If any point is found within the rectangle bounds, mark as invalid
                        if (x_C >= x_A && x_C <= x_B && y_C <= y_A && y_C >= y_B) {
                            valid = false;
                            break;
                        }
                    }

                    // If no invalid points found, increment count
                    if (valid) {
                        totalCount++;
                    }
                }
            }
        }
        
        return totalCount;
    }
}