import java.rmi.Naming;

public class LoginServer {
    public static void main(String[] args) {
        try {
            LoginImplementation loginService = new LoginImplementation();

            Naming.rebind("rmi://localhost:1099/loginservice", loginService);

            System.out.println("Login server is ready...");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
