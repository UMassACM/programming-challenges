/* This is an example solution to the "Streaming Statistics" problem from
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
#include <algorithm>
#include <set>

using namespace std;
typedef long long ll;
typedef pair<ll,ll> ival;

ll times[600000];
ll tot[600000];
ll rat[600000];

void add(int v, int a, int b, ll t1, ll t2, ll r) {
  ll tA = max(times[a], t1), tB = min(times[b], t2);
  if (tA >= tB) return;
  if (tA == times[a] && tB == times[b]) {
    rat[v] += r;
    return;
  } 
  tot[v] += (tB-tA)*r;
  if (b-a >= 2) {
    int m = (a+b)/2;
    add(2*v, a, m, t1, t2, r);
    add(2*v+1, m, b, t1, t2, r);
  }
}

ll query(int v, int a, int b, ll t1, ll t2) {
  ll tA = max(times[a], t1), tB = min(times[b], t2);
  if (tA >= tB) return 0;
  ll base = (tB-tA)*rat[v];
  if (tA == times[a] && tB == times[b] || b-a==1) return base+tot[v];
  int m = (a+b)/2;
  return base + query(2*v, a, m, t1, t2) + query(2*v+1, m, b, t1, t2);
}

ll t[150000], d[150000], r[150000];

int main(void) {
  int N;
  scanf("%d", &N);
  for (int i = 0; i < N; ++i) {
    scanf("%lld%lld%lld", t+i, d+i, r+i);
    times[2*i] = t[i];
    times[2*i+1] = t[i]-d[i];
  }
  sort(times, times+2*N);
  int M = unique(times, times+2*N)-times;
  for (int i = 0; i < N; ++i)
    add(1, 0, M-1, t[i]-d[i], t[i], r[i]);
  int Q;
  scanf("%d", &Q);
  for (int i = 0; i < Q; ++i) {
    ll a, b;
    scanf("%lld%lld", &a, &b);
    printf("%.3lf\n", 0.001*query(1, 0, M-1, a, b));
  }
  return 0;
}
