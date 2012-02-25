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
#include <stdio.h>
#include <stdlib.h>
#define MAXM 150000
#define MAXN 100000

int con[MAXN*3],p[MAXN*3],q[MAXN*3];
char answer[MAXN+1];

int par(char* s) {
  int i,num=0;
  for(i=0;s[i]<='9';i++) num=num*10+(s[i]-'0');
  return (num-1)*3+(s[i]-'A');
}

int main() {
  int i,j,M,N,now,next,n1,n2,pos[2];
  char s1[100],s2[100];
  scanf("%d %d", &N, &M);
  for(i=0;i<3*N;i++) {
    con[i]=-1;
    p[i]=-1;
  }
  for(i=0;i<M;i++) {
    scanf("%s %s", s1,s2);
    n1=par(s1); n2=par(s2);
    con[n1]=n2;
    con[n2]=n1;
  }
  q[0]=0;
  next=1;
  now=0;
  while(now<next) {
    if(q[now]==0 && now>0) {
      for(i=0;i<N;i++) answer[i]='B';
      answer[N]=0;
      i=0;
      do {
	if(p[i]%3==0) answer[p[i]/3]=(con[p[i]+1]==i)?'B':'C';
	i=p[i];
      } while(i!=0);
      printf("%s\n",answer);
      return 0;
    }    
    if(q[now]%3==0) {
      pos[0]=con[q[now]+1];
      pos[1]=con[q[now]+2];
    }
    else {
      pos[0]=con[q[now]-q[now]%3];
      pos[1]=-1;
    }
    for(i=0;i<2;i++) if(pos[i]!=-1) {
	if (p[pos[i]]==-1) {
	  q[next++]=pos[i];
	  p[pos[i]]=q[now];
	}
      }
    now++;
  }
  printf("Impossible\n");
  return 0;
}
    
    
    
