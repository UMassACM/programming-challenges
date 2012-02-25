/* This is an example solution to the "Greedy Cows" problem from
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
#include <cassert>
#include <cstdio>
#include <vector>

using namespace std;
typedef long long ll;

struct point {
  ll x, y;
  point(int x=0, int y=0): x(x), y(y) {}
  ll cross(point p) { return x*p.y - y*p.x; }
  point operator-(point p) { return point(x-p.x, y-p.y); }
};

ll choose(ll n, ll k) { 
  ll res = 1;
  for (int i = 0; i < k; ++i)
    res = res*(n-i)/(i+1);
  return res;
}

ll scross(ll v0, ll F0, ll F1) {
  ll res = 0;
  for (int i = 0; i <= 4; ++i) {
    ll x = choose(F0, 4-i)*choose(F1, i);
    for (int j = 0; j < 4; ++j) x *= v0 + (i>j);
    res += x;
  }
  for (int i1 = 0; i1 <= 1; ++i1)
    for (int i2 = 0; i2 <= 2; ++i2) {
      ll x = choose(F0, 1-i1)*choose(F0-(1-i1),2-i2)*choose(F1,i1)*choose(F1-i1,i2);
      x *= choose(v0 + i1, 2) * (v0 + (i2 > 0)) * (v0 + (i2 > 1));
      res += x;
    }
  for (int i = 0; i <= 2; ++i) {
    ll x = choose(F0, 2-i)*choose(F1, i);
    for (int j = 0; j < 2; ++j) x *= choose(v0 + (i>j), 2);
    res += x;
  }
  return res;
}

ll areas(int F, ll V) {
  ll v0 = V / F, extra = V % F;
  ll crossings = scross(v0, F-extra, extra);
  ll e = v0*v0*choose(F, 2) + extra*(V-v0-1) - choose(extra, 2) + 2*crossings + V + F;
  return e-V-F-crossings+1;
}

int main(void) {
  ll N;
  int F;
  scanf("%lld%d", &N, &F);
  vector<point> fence(F);
  for (int i = 0; i < F; ++i)
    scanf("%lld%lld", &fence[i].x, &fence[i].y);

  int f_orig = F;
  for (int i = 0; i < F; ++i) {
	  ll c = (fence[i]-fence[(i+F-1)%F]).cross(fence[(i+1)%F]-fence[i]);
	  if (!c) { --F, fence.erase(fence.begin()+i--); }
  }
  F = fence.size();
  assert(F >= 3);
  fprintf(stderr, "F %3d removed %3d cows %lld\n", F, f_orig-F, N);

  ll lo = -1, hi = 100000;
  while (hi-lo > 1) {
    ll v = (lo+hi)/2;
    if (areas(F, v) >= N) hi = v;
    else lo = v;
  }
  printf("%lld\n", hi);
  return 0;
}
