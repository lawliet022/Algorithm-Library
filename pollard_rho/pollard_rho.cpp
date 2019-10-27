#include<bits/stdc++.h>
using namespace std;

typedef long long ll;

#define PB push_back
#define MP make_pair
#define F first
#define S second
#define MOD 1000000007
#define EPS 1e-9



#define max 1000009


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


ll prime[max];

void sieve(){
	prime[0] = prime[1] = 1;

	for(ll i = 2; i*i <= max; i++){
		if(prime[i])
			continue;
		for(ll j = 2*i; j <= max; j += i){
			prime[j] = 1;
		}
	}
}

ll myrand(ll n) {
	return rand()*rand()%n*rand()%n;
}

inline ll pollardrho(ll n) { // O(n^0.25)
	if(n==1)
		return 1;
	if(n%2==0)
		return 2;
	ll c=myrand(n-1)+1, x=myrand(n-2)+2, y=x;
	ll d=1; 
	while(d==1) {
		x=modmul(x,x,n)+c; if(x>=n) x-=n;
		y=modmul(y,y,n)+c; if(y>=n) y-=n;
		y=modmul(y,y,n)+c; if(y>=n) y-=n;
		d=__gcd(abs(x-y),n);
		if(d==n) return (isprime(n) ? n:pollardrho(n));
	}
	return d;
}

map<ll, ll> factors(ll n){
	map<ll, ll> m;
	for(ll i = 2; i <= 1000000; i++){
		if(!prime[i]){
			if(i*i*i > n)
				break;
			// ll count = 1;
			while(n % i == 0){
				m[i]++;
				n /= i;
			}
		}
	}
	if(isprime(n)){
		m[n]++;
	}
	else{
		ll fac = pollardrho(n);
		ll fac2 = n / fac;
		if(fac != 1)
			m[fac]++;
		if(fac2 != 1)
			m[fac2]++;
	}
	return m;
}

ll power(ll a, ll e){
	ll ans = 0;
	for(int i = 0; i <= e; i++){
		ans += pow(a,i);
	}
	return ans;
}


ll sumDiv(ll n){
	map<ll, ll> m = factors(n);
	ll sum = 1;
	for(auto x : m){
		ll z = power(x.F, x.S);
		sum *= z;
	}
	return sum;
}


int main(){

	sieve();

	int t;
	cin >> t;
	while(t--){
		ll n;
		cin >> n;
		cout << (sumDiv(n)-n) << "\n";
	}
	return 0;
}
