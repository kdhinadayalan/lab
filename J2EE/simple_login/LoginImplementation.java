import java.rmi.*;
import java.rmi.server.*;
import java.sql.*;

public class LoginImplementation extends UnicastRemoteObject implements LoginInterface {

    private static final String URL = "jdbc:mysql://localhost:3306/rmidb";
    private static final String USER = "root";
    private static final String PASS = "";

    protected LoginImplementation() throws RemoteException {
        super();
    }

    @Override
    public boolean login(String username, String password) throws RemoteException {
        boolean isValid = false;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection con = DriverManager.getConnection(URL, USER, PASS);
            String sql = "SELECT * FROM users WHERE username=? AND password=?";
            PreparedStatement ps = con.prepareStatement(sql);  // Fixed method name
            ps.setString(1, username);  // Set the username
            ps.setString(2, password);  // Set the password

            ResultSet rs = ps.executeQuery();
            if (rs.next()) {
                isValid = true;
            }

            rs.close();
            ps.close();
            con.close();
        } catch (Exception e) {
            System.out.println("Database Error: " + e.getMessage());
        }

        return isValid;
    }
}
