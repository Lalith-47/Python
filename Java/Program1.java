import java.util.Scanner;

//package Java; // This ensures the file belongs to the correct package

public class Program1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter username: ");
        String username = scanner.nextLine();

        System.out.print("Enter password: ");
        String password = scanner.nextLine();

        System.out.println("Login credentials entered:");
        System.out.println("Username: " + username);
        System.out.println("Password: " + password);

        scanner.close();
    }
}