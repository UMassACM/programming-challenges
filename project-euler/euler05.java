/**
 * Solution to Project Euler #5:
 * What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
 * 
 * 3-14-12
 * @author Ryan McCann
 */

public class euler05
{
	/*
	 * Pretty cheap, brute force solution: start at a known lower bound,
	 * and increment it by 1 each time until the value is found.
	 */

	static int answer = 2520; //lowest number for [1,10] so use it as a lower bound
	
	public static void main(String[] args)
	{
		//temp!!
		//answer = ; //start here
		
		while(true)
		{
			//System.out.println(answer); //debug
			answer = test(answer);
			
			if(answer == -1) break; //found it
		}
		
		//System.out.println(answer);
	}
	
	static int test(int tmp)
	{
		for(int i=20; i>=2; i--)
		{
			if(tmp%i != 0)
			{
				return (tmp + 1);
				//return (tmp + tmp%i); //clever way?
			}
		}
		
		//passed
		System.out.println(tmp);
		return -1; //apease the compiler
	}
}
