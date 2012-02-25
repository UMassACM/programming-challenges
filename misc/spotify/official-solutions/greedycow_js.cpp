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
#include <cstdio>
#include <vector>

using namespace std;

typedef long long int ll;
typedef pair<ll, ll> post;

ll n, F;
vector<post> Fs;

ll bindp[100000][5];

ll bin(int n, int k) {
	return bindp[n][k];
}

ll c(int points1, int count1, int points2, int count2){
	int pp = points1*count1 + points2*count2;
	ll points = bin(count1*points1 + count2*points2, 4) + bin(count1*points1 + count2*points2, 2) + 1;
	points -= (bin(points1, 2) + bin(points1, 3)*(pp-points1) +bin(points1, 4)) * count1;
	points -= (bin(points2, 2) + bin(points2, 3)*(pp-points2) +bin(points2, 4)) * count2;
	return points;
}

int main(){
	for(int nb = 0; nb<100000; nb++){
		for(int kb = 0; kb<=4; kb++){
			if(kb == 0) bindp[nb][kb] = 1;
			else if (nb == 0) bindp[nb][kb] = 0;
			else bindp[nb][kb] = bindp[nb-1][kb-1] + bindp[nb-1][kb];
		}
	}
	scanf("%lld%lld", &n, &F);
	for(int i = 0; i<F; i++){
		ll x, y;
		scanf("%lld%lld", &x, &y);
		Fs.push_back(post(x, y));
	}
	for(size_t i = 1; i<=Fs.size()*3; i++){
		post prev = Fs[(i-1+Fs.size())%Fs.size()];
		post cur = Fs[(i+Fs.size())%Fs.size()];
		post next = Fs[(i+1+Fs.size())%Fs.size()];
		ll dx1 = cur.first - prev.first;
		ll dx2 = next.first - cur.first;
		ll dy1 = cur.second - prev.second;
		ll dy2 = next.second - cur.second;
		if(dx1*dy2 == dy1*dx2){
			Fs.erase(Fs.begin()+i);
			i--;
		}
	}
	F = Fs.size();
	int minpoints = 0;
	int hasmin = F;
	while(c(minpoints, hasmin, minpoints+1, F-hasmin) < n){
		hasmin--;
		if(hasmin == 0){
			minpoints++;
			hasmin = F;
		}
	}
	printf("%lld\n", minpoints*hasmin + (minpoints+1)*(F-hasmin));
}
