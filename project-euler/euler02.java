/**
 * Solution to Project Euler #2:
 * By considering the terms in the Fibonacci sequence whose values
 * do not exceed four million, find the sum of the even-valued terms.
 * 
 * 3-14-12
 * @author Ryan McCann
 */

import java.math.BigInteger;

public class euler02
{
	final static int Four_Million = 4000000;
	public static void main(String[] args)
	{
		BigInteger a = BigInteger.ONE;
		BigInteger b = BigInteger.ONE;
		long total = 0;
		
		while(a.max(b).intValue() < Four_Million)
		{
			a = a.add(b);
			if(a.intValue()%2 == 0){
				total += a.intValue();
			}
			
			b = a.add(b);
			if(b.intValue()%2 == 0){
				total += b.intValue();
			}
		}
		
		System.out.println(total);
	}
}
