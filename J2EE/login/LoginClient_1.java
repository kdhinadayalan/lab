
import java.rmi.Naming;
import java.util.Scanner;  

public class LoginClient {
    public static void main(String[] args) {
        try {
            
            LoginInterface login = (LoginInterface) Naming.lookup("rmi://localhost:2000/loginservice");

         
            Scanner sc = new Scanner(System.in);
            System.out.print("Enter username: ");
            String username = sc.nextLine();
            System.out.print("Enter password: ");
            String password = sc.nextLine();
            boolean status = login.login(username, password);

            if (status) {
                System.out.println("Login is successful.");
            } else {
                System.out.println("Invalid username or password.");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }
    } 
}

