#include <bits/stdc++.h>
#include <string>
using namespace std;

long desnafu(string s, unordered_map<char, long> h) {
    long r = 0;
    for (int i=0; i<s.size(); i++) {
        r = 5*r + h[s[i]];
    }
    return r;
}

string snafu(long n, unordered_map<long, string> r) {
    vector<string> ss;
    while (n > 0) {
        ss.push_back(r[n%5 - 5*(n%5>2)]);
        n = n/5 + (n%5>2);
    }
    string res = "";
    for (int i=ss.size(); i>=0; i--) {
        res += ss[i];
    }
    return res;
}

int main() {
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    unordered_map<char, long> h = {
        {'0', 0},
        {'1', 1},
        {'2', 2},
        {'-', -1},
        {'=', -2}
    };
    unordered_map<long, string> r = {
        {0, "0"},
        {1, "1"},
        {2, "2"},
        {-1, "-"},
        {-2, "="}
    };

    long a = 0;
    string s;
    while (cin >> s) {
        a += desnafu(s, h);
    }
    cout << "Part 1: " << snafu(a, r) << endl;
    cout << "Part 2: THE END!" << endl;

    return 0;
}