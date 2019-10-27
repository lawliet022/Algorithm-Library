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

// Classical Application of KMP - finding all occurances of a given string in another string
vi kmp(string s, string t){
	s = t + '#' + s;
	int n = s.size();
	vi pi(n,0);
	for(int i = 1; i < n; i++){
		int j = pi[i-1];
		while(j > 0 && s[i] != s[j])
			j = pi[j-1];
		if(s[i] == s[j])
			j++;
		pi[i] = j;
	}
	vi occ;
	for(int i = (int)t.size(); i < n; i++){
		if(pi[i] == (int)t.size())
			occ.PB(i-2*(int)t.size());
	}
	return occ;
}


int32_t main(){
	string s = "aaadpqaacaaa";
	string t = "aa";
	
	vi v = kmp(s,t);
	
	for(auto x : v){
		cout << x << " ";
	}

	return 0;
}
