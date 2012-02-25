/* This is an example solution to the "Three-State Memory" problem from
 * Spotify Code Quest 2012, held on Feb 18, 2012.
 *
 * The solution is provided as-is, is not documented, and may be
 * generally difficult to read.
 *
 * This work by Scrool (http://scrool.se/) is licensed under a
 * Creative Commons Attribution-Share Alike 2.5 Sweden License
 * (http://creativecommons.org/licenses/by-sa/2.5/se/deed.en).  You
 * are free to redistribute it as you like as long as this license
 * information is not removed.
 */
// Mikael Goldmann
/*
 *  solve(0) = solve(1) = 1
 *  x = 2y + 1 --> solve(x) = solve(y)
 *  x = 2y     --> solve(x) = solve(y) + solve(y-1)
 *
 * Use memoization
 */

import java.util.*;
import java.math.BigInteger;

public class memory_mg {
    static BigInteger ZERO = BigInteger.ZERO;
    static BigInteger ONE = BigInteger.ONE;
    static BigInteger TWO = ONE.add(ONE);

    static Map<BigInteger,Long> tab = new HashMap<BigInteger, Long>();
    static final long M = 1000000009;
    static long solve(BigInteger x) {
	if (x.equals(ONE)) return 1;
	if (x.equals(ZERO)) return 1;
	if (! tab.containsKey(x)) {
	    int n = x.getLowestSetBit();
	    if (n==0) 
		tab.put(x, solve(x.divide(TWO)));
	    else
		tab.put(x, (solve(x.divide(TWO)) + solve(x.divide(TWO).subtract(ONE))) % M );
	}
	return tab.get(x).longValue();
    }

    public static void main(String[] args) {
	BigInteger x = new BigInteger(new Scanner(System.in).next(), 2);
	System.out.println(solve(x));
    }
}