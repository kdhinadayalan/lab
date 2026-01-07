import java.rmi.Remote;
import java.rmi.RemoteException;
public interface LoginInterface extends Remote{
boolean login(String username,String password)throws RemoteException;
}

