#include<bits/stdc++.h>
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define EPS 1e-9
#define MOD	1000000007
#define int	long long
#define sz(x) (int)x.size()
#define all(a) (a).begin(),(a).end()
#define pii pair<int,int> 
#define vi vector<int>
using namespace std;

// Finding all occurances of a given string in another string in O(n+m)

vi rabin_karp(string const& s, string const& t){
	int p = 31;
	int n = s.size(), m = t.size();
	vi pa(max(n,m)+1,0);
	pa[0] = 1;
	for(int i = 1; i <= (int)pa.size(); i++)
		pa[i] = (pa[i-1]*p)%MOD;
	
	vi hs(m+1,0);
	for(int i = 0; i < m; i++){
		hs[i+1] = (hs[i] + (t[i] - 'a' + 1)*pa[i]) % MOD;
	}
	vi h(n+1,0);
	for(int i = 0; i < n; i++){
		h[i+1] = (h[i] + (s[i] - 'a' + 1)*pa[i]) % MOD;
	}
	vi v;
	for(int i = 0; i <= n-m; i++){
		int temp = (h[i+m] - h[i]) % MOD;
		int temp2 = hs[m]*pa[i] % MOD;
		if(temp < 0)	temp += MOD;
		if(temp == temp2)
			v.PB(i);
	}
	return v;
}

int32_t main(){
	string s = "abcdabfcdabcdwabac";
	string t = "bcd";
	
	vi v = rabin_karp(s,t);
	
	for(auto x : v)
		cout << x << " " ;


	return 0;
}
