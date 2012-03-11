/**
 * Solution to Project Euler #17:
 * Sum of all the characters needed to write each
 * number in range [1, 1000] in words.
 * 
 * 3-9-12
 * @author Ryan McCann
 */
public class Problem17
{
	static String[] num_str_one = {
		"", /* place holder */
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",
		"ten"
	};
	static String[] num_str_teen = {
		"ten", //
		"eleven",
		"twelve",
		"thirteen",
		"fourteen",
		"fifteen",
		"sixteen",
		"seventeen",
		"eighteen",
		"nineteen",
		"twenty"
	};	
	static String[] num_str_ten = {
		"", /* place holder */
		"ten",
		"twenty",
		"thirty",
		"fourty",
		"fify",
		"sixty",
		"seventy",
		"eighty",
		"ninety",
		"onehundred"
	};

	String hund = "hundred";
	String thou = "thousand";
	
	static int total = 0;
	
	public static void main(String[] args)
	{
		for(int i=1; i<=1000; i++)
		{
//			System.out.println(i);//debug
			String s;
			s = intToString(i);
//			System.out.println(s);//debug
			total += s.length();
		}
		System.out.println("Total letters used: " + total);
	}
	
	//returns a string representation of the argument. assumes bounded 1-1000.
	static String intToString(int i)
	{
		String s = "";
		if(i<10){
			s = num_str_one[i];
		} else if(i<20){
			s = num_str_teen[i-10];
		} else if(i<100){
			int ten = Integer.parseInt(Integer.toString(i).substring(0,1));
			int one = Integer.parseInt(Integer.toString(i).substring(1));
			s = num_str_ten[ten];
			s+= num_str_one[one];
		} else if(i<1000){
			int hun = Integer.parseInt(Integer.toString(i).substring(0,1));
			int ten = Integer.parseInt(Integer.toString(i).substring(1,2));
			int one = Integer.parseInt(Integer.toString(i).substring(2));
			s = num_str_one[hun] + "hundred";
			if(!(one==0 && ten==0)) s+= "and";
			
			if(ten!=1) s+= num_str_ten[ten];
			
			if(ten==1)
				s+= num_str_teen[one];
			else s+= num_str_one[one];
			
		} else { //i==1000
			s = "onethousand";
		}
		
		return s;
	}
}
