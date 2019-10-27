#include<bits/stdc++.h>
using namespace std;
#define PB push_back
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007
typedef long long ll;

ll modmul(ll a, ll b, ll n){
	ll res = 0;
	a = a % n;
	while(b > 0){
		if(b&1)
			res = (res+a)%n;
		a = (a*2) % n;

		b /= 2;
	}
	return (res%n);
}

ll modpow(ll a, ll d, ll n){
	if(d == 0)
		return 1 % n;
	ll u = modpow(a, d/2, n);
	
	// u = (u*u) % n;
	u = modmul(u,u,n);

	if(d&1){
		// u = (u*a)%n;
		u = modmul(u, a, n);
	}
	return u;
}
	
ll millerTest(ll d, ll n){
	ll a = 2 + rand() % (n-4);
	ll x = modpow(a, d, n);

	if(x == 1 || x == n-1)
		return true;

	while(d != n-1){
		// x = (x*x)%n;
		x = modmul(x, x, n);
		d *= 2;
		if(x == 1){
			return false;
		}
		if(x == n-1){
			return true;
		}
	}
	return false;
}


ll isprime(ll n){
	if(n <= 1 || n == 4)
		return false;
	if(n == 2 || n == 3)
		return true;
	if( (n&1) == 0)
		return false;

	ll d = n-1;
	while( (d&1) == 0){
		d >>= 1;
	}

	for(ll i = 0; i < 40; i++){
		if(!millerTest(d, n))
			return false;
	}
	return true;
}


int main(){

	ll n = 999998727900037;

	if(isprime(n)){
		cout << "prime\n";
	}
	else{
		cout << "No\n";
	}
	
	return 0;
}

