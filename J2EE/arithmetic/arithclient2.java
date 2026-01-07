import java.rmi.*;
import java.rmi.registry.*;
public class arithclient2{
public static void main (String[] args)throws Exception
{
System.out.println("\t\tARITHMETIC OPERATIONS");
arithmetic c=(arithmetic)Naming.lookup("rmi://localhost/arithmetic");
System.out.println("Addition of two number:"+c.add(10,5));
System.out.println("Subtraction of two number:"+c.sub(10,5));
System.out.println("Multiplication of two number:"+c.mul(40,5));
System.out.println("Division of two number:"+c.div(10,2));
}
}