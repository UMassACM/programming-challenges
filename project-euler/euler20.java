/**
 * Solution to Project Euler #20:
 * Find the sum of the digits in the number 100!
 * 
 * 3-14-12
 * @author Ryan McCann
 */

import java.math.BigInteger;

public class euler20
{
	static BigInteger ONE = BigInteger.ONE;
	static BigInteger TWO = ONE.add(ONE);
	
	public static void main(String[] args)
	{
		//first find 100!
		BigInteger fact = new BigInteger("100");
		BigInteger i = new BigInteger("99");
		for(; i.compareTo(TWO) >= 0; i=i.subtract(ONE))
		{
			fact = fact.multiply(i);
		}
		
		//convert it to a string
		String str = fact.toString();
		
		//then get the individual digits
		char[] digits = str.toCharArray();
		
		//finally sum the digits
		long result = 0;
		for(char c : digits)
		{
			/*
			Note: Character.digit(char c, int radix) returns -1 if the integer represented by
				the char c is greater than the radix. A value of 10 is used here for the radix
				since the possible values of c, [0-9], will always be less than 10.
			*/
			result += Character.digit(c, 10);
		}
		
		System.out.println(result);
	}
}
