class Solution {
    public int findClosest(int x, int y, int z) {
        // x position person 1 (move towards person 3)
        // y position person 2 (move towards person 3)
        // z position person 3 (doesnt move)
        // who arrives first?
        int xToZ = Math.abs(z - x);
        int yToZ = Math.abs(z - y);

        if (xToZ < yToZ) {
            return 1; // Person 1 arrives first
        } else if (xToZ > yToZ) {
            return 2; // Person 2 arrives first
        } else {
            return 0; // Both arrive at the same time
        }
    }
}