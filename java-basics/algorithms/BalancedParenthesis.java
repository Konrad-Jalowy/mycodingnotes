
import java.util.Stack;

public class BalancedParenthesis {

    public static boolean isBalanced(String str) {
        Stack<Character> stack = new Stack<>();

        // Przechodzimy przez każdy znak w ciągu
        for (char ch : str.toCharArray()) {
            // Jeśli znak to otwierający nawias, dodaj go na stos
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            // Jeśli znak to zamykający nawias
            else if (ch == ')' || ch == '}' || ch == ']') {
                // Sprawdź, czy stos jest pusty (brak odpowiadającego otwierającego nawiasu)
                if (stack.isEmpty()) {
                    return false;
                }
                // Pobierz szczyt stosu i sprawdź, czy nawiasy pasują
                char top = stack.pop();
                if (!matches(top, ch)) {
                    return false;
                }
            }
        }

        // Na końcu stos powinien być pusty, jeśli nawiasy są zbalansowane
        return stack.isEmpty();
    }

    // Funkcja pomocnicza sprawdzająca, czy nawiasy pasują
    private static boolean matches(char open, char close) {
        return (open == '(' && close == ')') ||
                (open == '{' && close == '}') ||
                (open == '[' && close == ']');
    }

    public static void main(String[] args) {
        String test1 = "({[]})";
        String test2 = "({[)]}";
        String test3 = "(((())))";
        String test4 = "([{}])";

        System.out.println(test1 + " -> " + isBalanced(test1)); // true
        System.out.println(test2 + " -> " + isBalanced(test2)); // false
        System.out.println(test3 + " -> " + isBalanced(test3)); // true
        System.out.println(test4 + " -> " + isBalanced(test4)); // true
    }
}
