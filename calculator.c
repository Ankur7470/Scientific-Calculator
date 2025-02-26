#include <stdio.h>
#include <math.h>

// Function to calculate square root
double square_root(double x) {
    if (x < 0) {
        printf("Cannot calculate square root of a negative number.\n");
        return -1;
    }
    return sqrt(x);
}

// Function to calculate factorial
long factorial(int x) {
    if (x < 0) {
        printf("Cannot calculate factorial of a negative number.\n");
        return -1;
    }
    long result = 1;
    for (int i = 2; i <= x; i++) {
        result *= i;
    }
    return result;
}

// Function to calculate natural logarithm
double natural_logarithm(double x) {
    if (x <= 0) {
        printf("Cannot calculate natural logarithm of a non-positive number.\n");
        return -1;
    }
    return log(x);
}

// Function to calculate power
double power_function(double x, double b) {
    return pow(x, b);
}

// Main function
int main() {
    int choice;
    double x, b;

    while (1) {
        printf("\nScientific Calculator Menu:\n");
        printf("1. Square Root (√x)\n");
        printf("2. Factorial (x!)\n");
        printf("3. Natural Logarithm (ln(x))\n");
        printf("4. Power Function (x^b)\n");
        printf("5. Exit\n");
        printf("Enter your choice (1-5): ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                printf("Enter a number to find its square root: ");
                scanf("%lf", &x);
                printf("Square root of %.2f is: %.2f\n", x, square_root(x));
                break;
            case 2:
                printf("Enter a number to find its factorial: ");
                scanf("%lf", &x);
                printf("Factorial of %.2f is: %ld\n", x, factorial((int)x));
                break;
            case 3:
                printf("Enter a number to find its natural logarithm: ");
                scanf("%lf", &x);
                printf("Natural logarithm of %.2f is: %.2f\n", x, natural_logarithm(x));
                break;
            case 4:
                printf("Enter the base (x): ");
                scanf("%lf", &x);
                printf("Enter the exponent (b): ");
                scanf("%lf", &b);
                printf("%.2f raised to the power of %.2f is: %.2f\n", x, b, power_function(x, b));
                break;
            case 5:
                printf("Exiting the calculator. Goodbye!\n");
                return 0;
            default:
                printf("Invalid choice. Please enter a number between 1 and 5.\n");
        }
    }
}