/* This is an example solution to the "Smooth Monkey" problem from
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

import java.util.Scanner;

public class monkey_mg {
    Scanner in  = new Scanner(System.in);

    double solve(double D, int W, int C) {
	if (W <= 0)
	    return 0.0;

	// the cost of moving is (2*ceil(W/C)-1) ml / m
	int ceil  = (W+C-1)/C;

	// how far do we get if we reach amount (ceil-1) * C ?
	double dist = (double)(W-(ceil-1)*C) / (2*ceil - 1);
	if (dist < D) {
	    // walk dist m and then recurse, as by then cost of moving has dropped
	    return solve(D-dist, (ceil-1)*C, C);
	} else {
	    // need to walk the last D m
	    return W - (2*ceil - 1)*D;
	}
    }

    void run() {
	double D = in.nextInt();
	int W = in.nextInt();
	int C = in.nextInt();
	System.out.println(solve(D, W, C));
    }

    public static void main(String[] aa) {
	new monkey_mg().run();
    }
}