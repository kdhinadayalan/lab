import java.rmi.*;
import java.rmi.registry.*;
import java.rmi.server.*;
public class factserver extends UnicastRemoteObject implements factint
{
	public factserver()throws Exception
	{
	
	}
public int factorial(int n)throws RemoteException
{
int fact=1;
for(int i=1;i<=n;i++){
fact=fact*i;
}
return fact;
}
public static void main(String[] args)throws Exception
{
factserver s=new factserver();
Naming.rebind("factint",s);
System.out.println("factorial Server is Ready...");
}
}

