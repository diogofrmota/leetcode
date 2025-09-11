import java.util.PriorityQueue;

class Solution {
    public String sortVowels(String s) {
        PriorityQueue<Character> pq = new PriorityQueue<>();
        for(int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if("AEIOUaeiou".indexOf(ch) != -1) {
                pq.offer(ch);
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i =0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if("AEIOUaeiou".indexOf(ch) != -1) {
                sb.append(pq.poll());
            }else {
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}