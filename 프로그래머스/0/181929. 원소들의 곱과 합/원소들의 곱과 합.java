class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int a1 = 0;
        int b1 = 1;
        for(int num : num_list){
            a1 += num;
            b1 *= num;
        }
        a1 = a1*a1;
        
        if(a1>b1){
            answer = 1;
        }
        else if(a1<b1){
            answer = 0;
        }
        return answer;
    }
}