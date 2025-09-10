class Solution {
    public int minimumTeachings(int n, int[][] languages, int[][] friendships) {
        Set<Integer> needTeach = new HashSet<>();
        for (int[] f : friendships) {
            int u = f[0], v = f[1];
            if (!canCommunicate(u, v, languages)) {
                needTeach.add(u);
                needTeach.add(v);
            }
        }
        if (needTeach.isEmpty()) return 0;

        int[] count = new int[n + 1];
        for (int u : needTeach) {
            for (int lang : languages[u - 1]) {
                count[lang]++;
            }
        }

        int maxKnown = 0;
        for (int lang = 1; lang <= n; lang++) {
            maxKnown = Math.max(maxKnown, count[lang]);
        }

        return needTeach.size() - maxKnown;
    }

    private boolean canCommunicate(int u, int v, int[][] languages) {
        for (int langU : languages[u - 1]) {
            for (int langV : languages[v - 1]) {
                if (langU == langV) return true;
            }
        }
        return false;
    }
}