/**
 * Solution to Project Euler #25:
 * What is the first term in the Fibonacci sequence to contain 1000 digits?
 * 
 * 3-14-12
 * @author Ryan McCann
 */
 
import java.math.BigInteger;

public class euler25
{
	public static void main(String[] args)
	{
		BigInteger a = BigInteger.ONE;
		BigInteger b = BigInteger.ONE;
		long count = 2; //next value is f3 (f1=1, f2=1, f3=2, etc.)
		
		//iterative solution to prevent a stack overflow
		while(true)
		{			
			a = a.add(b);
			count++;
			if(a.toString().length() >= 1000){
				break;
			}
			
			b = a.add(b);
			count++;
			if(b.toString().length() >= 1000){
				break;
			}
		}
		
		System.out.println(count);
	}
}
