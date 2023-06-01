class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        
        int z_cnt = 0;
        int a_cnt = 7;
        
        for (int l: lottos){
            if (l == 0){
                z_cnt += 1;
            }else{
                for (int w: win_nums){
                    if (l == w){
                        a_cnt -= 1;
                    }
                }
            }
            
        }
        
        if(z_cnt == 0){
            answer[0] = (a_cnt > 6) ? 6 : a_cnt ;
            answer[1] = (a_cnt > 6) ? 6 : a_cnt ;
        }else{
            answer[0] = a_cnt - z_cnt;
            answer[1] = (a_cnt > 6) ? 6 : a_cnt ;
        }
        
        
        return answer;
    }
}