import java.rmi.*;
public interface factint extends Remote {
public int factorial(int n)throws RemoteException;
}