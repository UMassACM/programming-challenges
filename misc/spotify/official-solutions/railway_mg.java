/* This is an example solution to the "Toy Railway" problem from
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
/** Simple yet moderately fast I/O routines.
 *
 * Example usage:
 *
 * Kattio io = new Kattio(System.in, System.out);
 *
 * while (io.hasMoreTokens()) {
 *    int n = io.getInt();
 *    double d = io.getDouble();
 *    double ans = d*n;
 *
 *    io.println("Answer: " + ans);
 * }
 *
 * io.close();
 *
 *
 * Some notes:
 *
 * - When done, you should always do io.close() or io.flush() on the
 *   Kattio-instance, otherwise, you may lose output.
 *
 * - The getInt(), getDouble(), and getLong() methods will throw an
 *   exception if there is no more data in the input, so it is generally
 *   a good idea to use hasMoreTokens() to check for end-of-file.
 *
 * @author: Kattis
 */

import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.io.OutputStream;

class Kattio extends PrintWriter {
    public Kattio(InputStream i) {
	super(new BufferedOutputStream(System.out));
	r = new BufferedReader(new InputStreamReader(i));
    }
    public Kattio(InputStream i, OutputStream o) {
	super(new BufferedOutputStream(o));
	r = new BufferedReader(new InputStreamReader(i));
    }

    public boolean hasMoreTokens() {
	return peekToken() != null;
    }

    public int getInt() {
	return Integer.parseInt(nextToken());
    }

    public double getDouble() { 
	return Double.parseDouble(nextToken());
    }

    public long getLong() {
	return Long.parseLong(nextToken());
    }

    public String getWord() {
	return nextToken();
    }



    private BufferedReader r;
    private String line;
    private StringTokenizer st;
    private String token;

    private String peekToken() {
	if (token == null) 
	    try {
		while (st == null || !st.hasMoreTokens()) {
		    line = r.readLine();
		    if (line == null) return null;
		    st = new StringTokenizer(line);
		}
		token = st.nextToken();
	    } catch (IOException e) { }
	return token;
    }

    private String nextToken() {
	String ans = peekToken();
	token = null;
	return ans;
    }
}


// Mikael Goldmann

/* Really a graph problem. For each switch, make 3 nodes.
 * Switch 10 corresponds to three nodes: 10A, 10B, 10C.
 * 10A corresponds to train being about to enter 10 at A etc.
 *
 * Create edges as follows:
 *    if 1A is connected to 2B
 *    then we have edges 1B --> 2B , 1C --> 2B
 *          and 2A --> 1B (entering at 2A, taking exit 2B)
 *
 * So problem becomes, how can we most quickly return to 1A if we start at 1A.
 * This can be determined by a a breadth-first-search. After a moments reflection
 * you realize that you will never want to enter the same switch at A twice, so you do not need
 * to worry about finding solutions where the swtich settings are not static.
 */
public class railway_mg {
    Kattio io = new Kattio(System.in);

    int nodeAsInt(String s) {
	// convert <num>X to 3*<num> + (X-'A')
	// for instance nodeAsInt("10B") returns 31
	int n = 0;
	for(char c : s.toCharArray()) {
	    if (c <= '9') n = n*10 + (c - '0');
	    else return (n-1)*3 + (c - 'A'); 
	}
	return -1;
    }

    void connect (int[][] adj, int u1, int u2) {
	// create edges implied by switch u1 being connected to switch u2
	int switch2 = u2 / 3;
	int entry2  = u2 - 3*switch2;
	int switch1 = u1 / 3;
	int exit1  = u1 - 3*switch1;
	if (exit1 == 0) { // exiting from A
	    adj[switch1*3 + 1][0] = u2;
	    adj[switch1*3 + 2][0] = u2;
	} else {
	    adj[switch1*3][exit1] = u2;
	}
    }
    
    void bfs(int[][] adj) {
	int N = adj.length;
	int[] q = new int[N+1]; // extra cell if we push 0 twice and visit everything
	int[] prev = new int[N];
	char[] sw = new char[N/3];
	for (int i = 0; i < N/3; ++i) sw[i] = 'B';
	for (int i = 0; i < N; ++i) prev[i] = -1;
	int hd = 0;
	int tl = 0;
	q[tl++] = 0;
	while ( hd < tl && prev[0] == -1 ) {
	    int u = q[hd++];
	    for (int i = 0; i < 3; ++i) {
		int w = adj[u][i];
		if (w == -1 || prev[w] != -1)
		    continue;
		prev[w] = u;
		q[tl++] = w;
	    }
	}
	if (prev[0] == -1)
	    io.println("Impossible");
	else {
	    int u = 0;
	    do {
		int w = prev[u];
		if (adj[w][2] == u) sw[w/3] = 'C';
		u = w;
	    } while (u != 0);
	    for (int i = 0; i < N/3; ++i)
		io.print(sw[i]);
	    io.println();
	}
    }

    void run() throws Exception {
	int N = io.getInt();
	int M = io.getInt();
	// Nodes are in {A,B,C} x [N]
	// Edges from A-nodes are labelled B or C
	// However, it is probably easier to map f(A)=0, f(B)=1, f(C)=2
	// and map a vertex (X,u) to 3*u + f(X)
	int[][] adj = new int[3*N][3];
	for (int i = 0; i < 3*N; ++i) {
	    adj[i][0] = adj[i][1] = adj[i][2] = -1;
	}

	for (int i=0; i<M; ++i) {
	    int u = nodeAsInt(io.getWord());
	    int v = nodeAsInt(io.getWord());
	    connect(adj, u, v);
	    connect(adj, v, u);
	}
	bfs(adj);
	io.close();
    }

    public static void main(String[] aa) throws Exception {
	new railway_mg().run();
    }
}
