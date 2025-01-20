
import java.util.Scanner;

public class LeapYearChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to enter a year
        System.out.print("Enter a year: ");
        int year = scanner.nextInt();

        // Check if the year is a leap year
        if (isLeapYear(year)) {
            System.out.println(year + " is a leap year and has 366 days.");
        } else {
            System.out.println(year + " is not a leap year and has 365 days.");
        }
    }

    // Method to check if a year is a leap year
    public static boolean isLeapYear(int year) {
        // A year is a leap year if it is divisible by 4
        // but not divisible by 100 unless it is also divisible by 400
        if (year % 4 == 0) {
            if (year % 100 == 0) {
                return year % 400 == 0;
            } else {
                return true;
            }
        } else {
            return false;
        }
    }
}

/*
Explanation of leap year calculation:
1. A year is a leap year if it is divisible by 4. This accounts for most leap years.
2. However, if the year is divisible by 100, it is not a leap year unless it is also divisible by 400.
   - This rule exists because a year is approximately 365.2422 days, not exactly 365.25 days.
   - Without this rule, the calendar would drift over centuries.
   - The 400-year rule ensures better alignment with the solar year.

Examples:
- 2000: Divisible by 4, divisible by 100, and divisible by 400 -> Leap year.
- 1900: Divisible by 4 and 100, but not by 400 -> Not a leap year.
- 2024: Divisible by 4, not divisible by 100 -> Leap year.
- 2023: Not divisible by 4 -> Not a leap year.
*/
