/* This is an example solution to the "Streaming Statistics" problem from
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

import java.io.*;
import java.util.*;


class Val implements Comparable<Val> {
    long time;
    long val;
    Val(long t, long d) { time = t; val = d; }
    public int compareTo(Val that) {
	if (this == that) return 0;
	if (time < that.time) return -1;
	if (time > that.time) return 1;
	return 0;
    }
}


public class streamstats_mg {

    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static PrintWriter out = new PrintWriter(new OutputStreamWriter(System.out));
    static StringTokenizer st = new StringTokenizer("");
 
    static long getLong() {
	try {
	    while (!st.hasMoreTokens())
		st = new StringTokenizer(in.readLine());
	    return Long.parseLong(st.nextToken());
	} catch (IOException e) {
	    throw new RuntimeException(e);
	}
    }

    static Val[] combine(Val[] ds) {
	int n = ds.length;
	int j = 0;
	// First, sort and combine deltas that occur at the same time.
	Arrays.sort(ds);
	for (int i = 1; i < n; ++i) {
	    if (ds[j].time == ds[i].time)
		ds[j].val += ds[i].val;
	    else
		ds[++j] = ds[i];
	}

	// Then compute the rates at the various times.
	n = j + 1;
	Val[] rates = new Val[n];
	for (int i = 0; i < n; ++i) {
	    rates[i] = ds[i];
	}
	for (int i = 1; i < n; ++i) {
	    rates[i].val += rates[i-1].val;
	}
	return rates;
    }

    // Compute amount of data streamed at time t.
    // We can compute amount of data streamed until a particular time by binary searching for the time
    // and use the rate and the data to compute how much data was sent.
    static long streamed(long t, Val[] rates, Val[] data) {
	int n =rates.length;
	if (t < rates[0].time) return 0;
	if (t >= rates[n-1].time) return data[n-1].val;
	int lft = 0, rte = n-1;
	// now rates[lft].time <= t < rates[rte].time
	// we keep this invariant
	int m = 0;
	while (lft < rte - 1) {
	    m = (lft+rte) / 2;
	    if (rates[m].time <= t)
		lft = m;
	    else
		rte = m;
	}
	return data[lft].val + (t - rates[lft].time) * rates[lft].val;
    }

    public static void main(String[] args) throws Exception{
	int N = (int)getLong();
	// For each log item store two deltas, one increase and one decrease in bitrate
	Val[] deltas = new Val[2*N];
	for(int i = 0; i < N; ++i) {
	    long t = getLong();
	    long d = getLong();
	    long r = getLong();
	    deltas[2 * i] = new Val(t - d, r);
	    deltas[2 * i + 1] = new Val(t, -r);
	}

	// From deltas, compute the rates at the given times.
	// rate[i].val is the rate between rate[i].time and rate[i+1].time
	Val[]rates = combine(deltas);
	assert rates[rates.length-1].val == 0;

	// compute data[i].val which is the amount of data streamed until data[i].time, in bits (rather than kbits as we use ms for time).
	Val[] data = new Val[rates.length];
	data[0] = new Val(rates[0].time, 0);
	for (int i = 1; i < rates.length; ++i) {
	    data[i] = new Val(rates[i].time, data[i-1].val + rates[i-1].val * (rates[i].time - rates[i-1].time));
	}

	int Q = (int)getLong();
	while (Q-->0) {
	    long a = getLong();
	    long b = getLong();
	    long x = streamed(b, rates, data)-streamed(a, rates, data);
	    out.printf("%1.3f\n", (double)(x) / 1000.0 + 0.00001);
	}
	
	out.close();
    }
}
