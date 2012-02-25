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
// Author: Per Austrin
#include <cstdio>

int main(void) {
  double D;
  int W, C;
  double ans = 0;
  scanf("%lf%d%d", &D, &W, &C);
  while (W > 0) {
    int reps = (W+C-1)/C;
    int until = W % C ? W % C : C;
    double d = 1.0*until/(2*reps-1);
    if (d > D) {
      ans = W - (2*reps-1)*D;
      W = 0;
    } else {
      W -= until;
      D -= d;
    }
  }
  printf("%.9lf\n", ans);
  return 0;
}
