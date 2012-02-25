/* This is an example solution to the "Evenland" problem from
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
/*
** Author: Lukas Polacek
*/

import java.io.*;
import java.util.Scanner;
import java.lang.Math;

public class Evenland {
    public static class UnionFind
    {
        public int[] e;
        public UnionFind(int n)
        {
            e = new int[n];
            for (int i = 0; i < n; i++)
                e[i] = -1;
        }

        public void join(int a, int b) { // union sets
            a = find(a);
            b = find(b);
            if (a == b) return;
            if (e[a] > e[b])
            {
                int t = a;
                a = b;
                b = t;
            }
            e[a] += e[b];
            e[b] = a;
        }

        int find(int x) { // Find set-head with path-compression
            if (e[x] < 0) return x;
            return e[x] = find(e[x]);
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new BufferedInputStream(System.in));
        int n, m;
        n = sc.nextInt();
        m = sc.nextInt();

        UnionFind u = new UnionFind(n);
        for (int i = 0; i < m; i++)
        {
            int a, b;
            a = sc.nextInt();
            b = sc.nextInt();
            u.join(a - 1, b - 1);
        }

        int power = m - n;
        for (int i = 0; i < n; i++)
            if (u.e[i] < 0) power++;
        int mod = 1000000009, res = 1;
        for (int i = 0; i < power; i++)
            res = 2 * res % mod;
        System.out.println(res);
    }
}
