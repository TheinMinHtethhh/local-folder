import java.util.Scanner;

public class Calculator {
    public static void main(String[] args) {
        System.out.println("this is calculator");
        System.out.println("you can do +, -, *, / with two (double) numbers");
        System.out.println("first number is:");

        Scanner in = new Scanner(System.in);
        double num1 = in.nextDouble();
        System.out.println("second number is:");
        double num2 = in.nextDouble();

        System.out.println("operator is:(+, -, *, /)");
        String operator = in.next();

        double result = 0.0;

        // todo: do the calculation here
        if (operator.equals("+")) {
            result = num1 + num2;
        } else if (operator.equals("-")) {
            result = num1 - num2;
        } else if (operator.equals("*")) {
            result = num1 * num2;
        } else if (operator.equals("/")) {
            result = num1 / num2;
            // todo: tell user num2 should not be zero
        } else {
            System.out.println("Invalid operator.");
        }

        System.out.println(num1 + " " + operator + " " + num2 + " = " + result);
    }

    // todo: move the calculation here
    // public double doCalculation() {}
}
