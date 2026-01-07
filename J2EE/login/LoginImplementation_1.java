import java.rmi.*;
import java.rmi.server.*;
public class LoginImplementation extends UnicastRemoteObject implements LoginInterface{
protected LoginImplementation()throws RemoteException{
super();
}
@Override
public boolean login (String username,String password)throws RemoteException {
if(username.equals("admin")&&password.equals("1234567")){
return true;
}
else if(username.equals("user")&&password.equals("pass")){
return true;
}
else{
return false;
}
}
}
 