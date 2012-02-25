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
// Author: Per Austrin
#include <cstdio>

int main(void) {
	int b, k, g;
	scanf("%d%d%d", &b, &k, &g);
	int groups = k/g;
	// days = ceil((b-1)/groups)
	int days = (b-1+groups-1)/groups;
	printf("%d\n", days);
	return 0;
}
