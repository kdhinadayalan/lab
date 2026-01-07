import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class LoginServer {
    public static void main(String[] args) {
        try {
            LocateRegistry.createRegistry(2000);
            LoginImplementation loginService = new LoginImplementation();
            Naming.rebind("rmi://localhost:2000/loginservice", loginService);

            System.out.println("Login server is ready...");

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
