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
// Author: Per Austrin
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

vpii adj[200000];
int thres[200000];

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 1; i <= N; ++i) {
    int k;
    scanf("%d%d", thres+i, &k);
    for (int j = 0; j < k; ++j) {
      int s, v;
      scanf("%d%d", &s, &v);
      adj[s].push_back(pii(i, v));
      thres[i] -= v;
    }
  }

  queue<int> Q;
  thres[1] = 1;
  Q.push(1);
  while (!Q.empty()) {
    int v = Q.front(); Q.pop();
    --N;
    for (vpii::iterator it = adj[v].begin(); it != adj[v].end(); ++it) {
      if (thres[it->first] <= 0) {
	thres[it->first] += it->second;
	if (thres[it->first] > 0) 
	  Q.push(it->first);
      }
    }
  }
  printf("%d\n", N);
  return 0;
}
