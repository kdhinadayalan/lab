import java.rmi.*;
import java.rmi.registry.*;
import java.util.Scanner;
public class arithclient{

public static void main (String[] args)throws Exception
{

Scanner sc=new Scanner(System.in);
System.out.println("\t\tARITHMETIC OPERATIONS");
System.out.print("Enter a value:");
int a=sc.nextInt();
System.out.print("Enter b value:");
int b=sc.nextInt();
arithmetic c=(arithmetic)Naming.lookup("rmi://localhost/arithmetic");
System.out.println("Addition of two number:"+c.add(a,b));
System.out.println("Subtraction of two number:"+c.sub(a,b));
System.out.println("Multiplication of two number:"+c.mul(a,b));
System.out.println("Division of two number:"+c.div(a,b));
}
}