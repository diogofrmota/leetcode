class Solution {
    public int maxFreqSum(String s) {
        int[] vowelFreq = new int[26];
        int[] consonantFreq = new int[26];
        boolean[] isVowel = new boolean[26];
        
        char[] vowels = {'a', 'e', 'i', 'o', 'u'};
        for (char c : vowels) {
            isVowel[c - 'a'] = true;
        }

        for (char c : s.toCharArray()) {
            int index = c - 'a';
            if (isVowel[index]) {
                vowelFreq[index]++;
            } else {
                consonantFreq[index]++;
            }
        }

        int maxVowel = 0;
        for (int freq : vowelFreq) {
            if (freq > maxVowel) {
                maxVowel = freq;
            }
        }
        
        int maxConsonant = 0;
        for (int freq : consonantFreq) {
            if (freq > maxConsonant) {
                maxConsonant = freq;
            }
        }
        return maxVowel + maxConsonant;
    }
}