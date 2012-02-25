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
// Author: Per Austrin
#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;
typedef vector<int> vi;

const int MOD = 1000000009;
vi adj[200000];
int vis[200000];

void dfs(int v) {
  vis[v] = true;
  for (vi::iterator it = adj[v].begin(); it != adj[v].end(); ++it)
    if (!vis[*it]) dfs(*it);
}

int main(void) {
  int N, M;
  scanf("%d%d", &N, &M);
  for (int i = 0; i < M; ++i) {
    int a, b;
    scanf("%d%d", &a, &b);
    adj[a].push_back(b);
    adj[b].push_back(a);
  }
  memset(vis, 0, sizeof(vis));
  int C = 0;
  for (int i = 1; i <= N; ++i)
    if (!vis[i]) ++C, dfs(i);
  int ans = 1;
  for (int i = 0; i < M-N+C; ++i)
    ans = (2*ans) % MOD;
  printf("%d\n", ans);
  return 0;
}
