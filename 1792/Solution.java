import java.util.PriorityQueue;

class Solution {
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        // Priority queue that prioritizes classes by the potential improvement
        PriorityQueue<double[]> heap = new PriorityQueue<>((a, b) -> {
            double diffA = (a[0] + 1) / (a[1] + 1) - a[0] / a[1];
            double diffB = (b[0] + 1) / (b[1] + 1) - b[0] / b[1];
            return Double.compare(diffB, diffA);
        });

        // Add all classes to the heap
        for (int[] cls : classes) {
            heap.offer(new double[]{cls[0], cls[1]});
        }

        // Assign extra students one by one to the class with maximum current improvement
        while (extraStudents-- > 0) {
            double[] cls = heap.poll();
            cls[0] += 1; // Add one passing student
            cls[1] += 1; // Add one total student
            heap.offer(cls);
        }

        // Calculate the final average pass ratio
        double totalRatio = 0;
        while(!heap.isEmpty()) {
            double[] cls = heap.poll();
            totalRatio += cls[0] / cls[1];
        }

        return totalRatio / classes.length;
        
    }
}