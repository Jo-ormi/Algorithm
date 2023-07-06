import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String sn = String.valueOf(n);
        double m = Math.pow(10, sn.length());
        
        while (m >= 1){
            answer += n / m;
            n = (int)(n % m);
            m /= 10;
        }

        return answer;
    }
}