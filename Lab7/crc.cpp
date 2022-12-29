#include <bits/stdc++.h>
using namespace std;

string xoring(string a, string b, int n)
{
    string ans = "";

    for (int i = 0; i < n; i++)
    {
        if (a[i] == b[i])
            ans += "0";
        else
            ans += "1";
    }
    return ans;
}

int main()
{
    string a = "1011";
    string b = "1010";
    string d = "1011010101";
    string c = "1010";
    int n = a.length();
    c = xoring(a, b, n);
    cout << c << endl;
}