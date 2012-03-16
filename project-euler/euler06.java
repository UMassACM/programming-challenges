/**
 * Solution to Project Euler #6:
 * Find the difference between the sum of the squares of the
 * first one hundred natural numbers and the square of the sum.
 * 
 * 3-15-12
 * @author Ryan McCann
 */

public class euler06
{
	public static void main(String[] args)
	{
		long sum_squares = 0;
		long square_sums = 0;
		
		for(int i=1; i<=100; i++)
		{
			sum_squares += i*i;
			square_sums += i;
		}
		square_sums = square_sums*square_sums;
		
		long diff = square_sums - sum_squares;
		//System.out.println(sum_squares);
		//System.out.println(square_sums);
		System.out.println(diff);
	}
}
