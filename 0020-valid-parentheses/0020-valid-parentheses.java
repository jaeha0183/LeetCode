import java.util.*;

class Solution {
    public boolean isValid(String s) {
        // 닫는 괄호 → 여는 괄호 매핑
        Map<Character, Character> mapping = new HashMap<>();
        mapping.put(')', '(');
        mapping.put(']', '[');
        mapping.put('}', '{');

        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            // 여는 괄호면 스택에 push
            if (mapping.containsValue(c)) {
                stack.push(c);
            } 
            // 닫는 괄호면 스택 top 확인
            else if (mapping.containsKey(c)) {
                if (stack.isEmpty() || stack.pop() != mapping.get(c)) {
                    return false;
                }
            } 
            // 다른 문자는 없으므로 else 불필요
        }

        // 스택이 비어야 유효
        return stack.isEmpty();
    }
}
