#include<bits/stdc++.h>
#define fi first
#define se second
#define pb push_back
using namespace std;
int pref[2][1000010];
int hell[2];
void sol(int mi,int d,bool c)
{
	int p,k,s;
	d+=pref[c][mi-1];
	p=1;
	k=hell[!c];
	while(p<k)
	{
		s=(p+k)/2;
		if(pref[!c][s]>=d)
			k=s;
		else
			p=s+1;
	}
	cout<<d-pref[!c][p-1]<<" "<<p<<"\n";
	return;
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	int n,m,z,mi,d,i;
	char c;
	cin>>n>>m;
	hell[0]=n;
	hell[1]=m;
	for(i=1;i<=n;i++)
	{
		cin>>pref[0][i];
		pref[0][i]+=pref[0][i-1];
	}
	for(i=1;i<=m;i++)
	{
		cin>>pref[1][i];
		pref[1][i]+=pref[1][i-1];
	}
	cin>>z;
	for(i=1;i<=z;i++)
	{
		cin>>d>>mi>>c;
		sol(mi,d,(c=='B'));
	}
	return 0;
}