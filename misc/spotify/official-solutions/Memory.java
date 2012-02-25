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
import java.util.*;
import java.io.*;

public class Memory {
	public static final int MOD = 1000000009;
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));
        String b = sc.next();
        int a[] = new int[b.length()];
        for (int i = 0; i < b.length(); i++)
            a[i] = b.charAt(i) - '0';

        int p[][] = new int[b.length()][4];
        for (int i = 0; i < b.length(); i++)
            for (int j = 0; j < 4; j++)
                p[i][j] = 0;
        p[0][a[0]] = 1;

        for (int i = 0; i < b.length() - 1; i++)
            for (int j = 0; j < 4; j++)
            {
                if (j > 0)
                    p[i + 1][a[i + 1] + 2] = (p[i][j] + p[i + 1][a[i + 1] + 2]) % MOD;
                if (j < 3)
                    p[i + 1][a[i + 1]] = (p[i][j] + p[i + 1][a[i + 1]]) % MOD;
            }

        int res = 0;
        for (int i = 0; i < 3; i++)
            res = (res + p[b.length() - 1][i]) % MOD;
        System.out.println(res);
    }
}
