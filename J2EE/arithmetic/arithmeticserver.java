import java.rmi.*;
import java.rmi.registry.*;
import java.rmi.server.*;
public class arithmeticserver extends UnicastRemoteObject implements arithmetic
{
	public arithmeticserver()throws Exception
	{
	
	}
public int add(int a,int b)throws RemoteException
{
	return a+b;
}
public int sub(int a,int b)throws RemoteException
{
	return a-b;
}
public int mul(int a,int b)throws RemoteException
{
	return a*b;
}
public int div(int a,int b)throws RemoteException
{
	return a%b;
}
public static void main(String[] args)throws Exception
{
arithmeticserver as=new arithmeticserver();
Naming.rebind("arithmetic",as);
System.out.println("arithmetic Server is Ready...");
}
}

