class Solution {
    public int solution(int a, int b) {
        // 1. a ⊕ b 계산: 문자열로 변환 후 붙이고 다시 정수로 변환
        int abConcat = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        
        // 2. 2 * a * b 계산
        int doubleProduct = 2 * a * b;
        
        // 3. 더 큰 값 반환 (같으면 abConcat 반환)
        return Math.max(abConcat, doubleProduct);
    }
}
