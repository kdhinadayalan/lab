import java.rmi.*;
import java.rmi.registry.*;
import java.util.Scanner;
public class factcli{
public static void main (String[] args)throws Exception{
factint c=(factint)Naming.lookup("rmi://localhost/factint");

Scanner sc=new Scanner(System.in);
System.out.print("Enter a number:");
int n=sc.nextInt();
int result=c.factorial(n);
System.out.println("Factorial of "+n+"is"+result);
}
}