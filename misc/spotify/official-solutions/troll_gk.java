/* This is an example solution to the "Troll Hunt" problem from
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
import java.util.Scanner;

public class troll_gk {
    Scanner in  = new Scanner(System.in);

    int solve(int B, int K, int G) {
        assert(2 <= B);
        assert(B <= 1000);
        assert(1 <= K);
        assert(K <= 100);
        assert(1 <= G);
        assert(G <= K);
        --B;
        int g = K / G;
        int ret = 0;
        while(B > 0) {
            B -= g;
            ++ret;
        }
        return ret;
    }

    void run() {
        int B = in.nextInt();
        int K = in.nextInt();
        int G = in.nextInt();
        System.out.println(solve(B, K, G));
    }

    public static void main(String[] aa) {
        new troll_gk().run();
    }
}
