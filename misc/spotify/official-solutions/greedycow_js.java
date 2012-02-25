/* This is an example solution to the "Greedy Cows" problem from
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
import java.io.BufferedInputStream;
import java.io.InputStream;
import java.io.PrintStream;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class greedycow_js {

	private Scanner in;
	private PrintStream out;

	public greedycow_js(InputStream stream, PrintStream out) {
		in = new Scanner(new BufferedInputStream(stream));
		this.out = out;
	}

	long n;
	int f;
	List<Pair<Long, Long>> points = new ArrayList<Pair<Long, Long>>(f);

	private void indata() {
		n = in.nextLong();
		f = in.nextInt();
		for (int i = 0; i < f; i++) points.add(new Pair(in.nextLong(), in.nextLong()));
	}

	private void removeColinear() {
		for (int i = 0; i < (1000 * points.size()) && points.size() >= 3; i++) {
			Pair<Long, Long> a = points.get(i % points.size());
			Pair<Long, Long> b = points.get((i + 1) % points.size());
			Pair<Long, Long> c = points.get((i + 2) % points.size());
			//vector a -> b
			long x1 = b.first - a.first;
			long y1 = b.second - a.second;
			//vector b -> c
			long x2 = c.first - b.first;
			long y2 = c.second - b.second;

			//check if cross product is zero
			long cprod = x1 * y2 - y1 * x2;
			if (cprod == 0) {
				points.remove((i + 1) % points.size());
			}
		}
		f = points.size();
	}

	long[][] binom = binomialTable(100000, 5);

	public boolean ok(int ans) {
		int points1 = ans / f;
		int count1 = f - (ans % f);
		int points2 = points1+1;
		int count2 = ans % f;
		int totPoints = points1 * count1 + points2 * count2;
		assert totPoints == ans;
		long points = binom[totPoints][4] + binom[totPoints][2] + 1;
		points -= ((binom[points1][2] + binom[points1][3] * (totPoints - points1) + binom[points1][4])) * count1;
		points -= ((binom[points2][2] + binom[points2][3] * (totPoints - points2) + binom[points2][4])) * count2;
		return points >= n;
	}

	private void solve() {
		indata();
		removeColinear();
		int ans = 0;
		while (!ok(ans)) ans++;
		out.println(ans);
	}

	public static long[][] binomialTable(int n, int k) {
		long[][] binoms = new long[n + 1][k + 1];
		for (int i = 0; i <= n; i++) {
			binoms[i][0] = 1;
			for (int j = 1; i > 0 && j <= k; j++) binoms[i][j] = (binoms[i - 1][j - 1] + binoms[i - 1][j]);
		}
		return binoms;
	}

	public static void main(String... args) {
		new greedycow_js(System.in, System.out).solve();
	}

	public class Pair<A, B> {

		public A first;
		public B second;

		public Pair(A first, B second) {
			this.first = first;
			this.second = second;
		}
	}


}
