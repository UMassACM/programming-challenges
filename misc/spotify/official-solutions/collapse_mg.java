/* This is an example solution to the "Collapse" problem from
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

class Node {
    int surplus;
    int [] to;
    int [] quantity;
}

public class collapse_mg {
    static BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
    static final int MAX_ISLANDS = 100000;
    static final int MAX_EDGES = 500000;

    StringTokenizer st = new StringTokenizer("");

    public static void main(String[] atgs)  throws Exception {
	new collapse_mg().solve();
    }

    int getInt() throws Exception {
	while (! st.hasMoreTokens())
	    st = new StringTokenizer(in.readLine());
	return Integer.parseInt(st.nextToken());
    }

    void solve()  throws Exception {
	int N = getInt();
	Node[] nodes = new Node[N];
	int[] deg = new int[N];
	int[] from = new int[MAX_EDGES]; 
	int[] to = new int[MAX_EDGES]; 
	int[] quantity = new int[MAX_EDGES]; 
	int j = 0;
	// read info for all nodes, but just save edges in from, to, quntity
	// since we want outgoing edges but we get incoming edges
	for (int i = 0; i < N; ++i) {
	    Node u = nodes[i] = new Node();
	    u.surplus = - getInt(); // - threshold
	    int K = getInt();
	    while (K-->0) {
		to[j] = i;
		from[j] = getInt()-1;
		++deg[from[j]];
		quantity[j] = getInt();
		++j;
	    }
	}
	// move edge information into nodes
	// and while doing so, add amount to surplus of to node
	for (int i = 0; i < N; ++i) {
	    nodes[i].to = new int[deg[i]];
	    nodes[i].quantity = new int[deg[i]];
	    deg[i]=0;
	}
	while(j-->0) {
	    int i = from[j];
	    Node u = nodes[i];
	    u.to[deg[i]] = to[j];
	    u.quantity[deg[i]] = quantity[j];
	    nodes[to[j]].surplus += quantity[j];
	    ++deg[i];
	}

	// Enqueue first island
	// While q is not empty, pop an island and subtract its contributions from all islands it delivers to
	//   If surplus of an island goes negative, then enqueue that island
	int[] q = new int[N];
	int hd = 0;
	int tl = 0;
	nodes[0].surplus = -1;
	q[tl++] = 0;
	while (hd < tl) {
	    Node u = nodes[q[hd++]];
	    for (int i = 0; i < u.to.length; ++i) {
		int w = u.to[i];
		if (nodes[w].surplus < 0)
		    continue; // w already handled
		nodes[w].surplus -= u.quantity[i];
		if (nodes[w].surplus < 0)
		    q[tl++] = w;
	    }
	}

	// tl islands have collapsed, so N-tl are still there
	System.out.println(N-tl);
	
    }
}
