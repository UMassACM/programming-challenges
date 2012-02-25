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
// Author: Per Austrin
#include <cstdio>
#include <cstring>
#include <queue>

using namespace std;

int back[400000];
int dist[400000];
int nxt[200000][3];

int main(void) {
  int N, M;
  scanf("%d%d", &N, &M);
  memset(nxt, -1, sizeof(nxt));
  memset(dist, -1, sizeof(dist));
  for (int i = 0; i < M; ++i) {
    int x, y;
    char X[10], Y[10];
    scanf("%d%s%d%s", &x, X, &y, Y);
    --x; --y;
    nxt[x][*X-'A'] = 2*y+(*Y != 'A');
    nxt[y][*Y-'A'] = 2*x+(*X != 'A');
  }
  queue<int> q;
  for (int i = 1; i < 3; ++i) {
    if (nxt[0][i] != -1) {
      dist[nxt[0][i]] = 0;
      back[nxt[0][i]] = -1;
      q.push(nxt[0][i]);
    }
  }
  while (!q.empty()) {
    int x = q.front(); q.pop();
    int v = x/2, dir = x % 2;
    int lo = dir ? 0 : 1, hi = dir ? 1 : 3;
    for (int i = lo; i < hi; ++i) {
      int w = nxt[v][i];
      if (w != -1 && dist[w] == -1) {
	dist[w] = dist[x] + 1;
	back[w] = x;
	q.push(w);
      }
    }
  }
  if (dist[0] == -1) {
    printf("Impossible\n");
  } else {
    char setting[200000];
    memset(setting, 'B', sizeof(setting));
    setting[N] = 0;
    int w = 0;
    while (back[w] != -1) {
      int x = back[w];
      if (nxt[x/2][1] != w) setting[x/2] = 'C';
      w = x;
    }
    if (nxt[0][1] != w) setting[0] = 'C';
    printf("%s\n", setting);
  }
  return 0;
}
