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
// Author: Per Austrin
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;

const int MOD = 1000000009;

char num[20000];
int ways[20000][6];

int Ways(int at, int need) {
	if (!num[at] || need > 5 || need < 0) return need == 0;
	int &ans = ways[at][need];
	if (!ans)
		for (int x = 0; x <= 2; ++x)
			ans = (ans + Ways(at+1, 2*need+num[at]-'0'-x)) % MOD;
	return ans;
}

int main(void) {
	scanf("%s", num);
	memset(ways, 0, sizeof(ways));
	cout << Ways(0, 0) << endl;
	return 0;
}
