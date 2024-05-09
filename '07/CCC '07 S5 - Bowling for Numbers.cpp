#include <bits/stdc++.h>

using namespace std;

int t, n, k, w, psa[40000], dp[40000][600], nums[40000];

int sum(int i, int j) {
    return psa[j]-psa[i-1];
}

int solve(int i, int j) {
    if (i > n) return 0;
    if (j <= 0) return 0;
    if (dp[i][j] != -1) return dp[i][j];

    int a = sum(i, i+w-1) + solve(i+w, j-1);
    int b = solve(i+1, j);
    
    return dp[i][j] = max(a, b);
}

int main() {
    cin >> t;
    for (int x=0; x < t; x++) {
        cin >> n >> k >> w;
        for (int i=0; i < n+1; i++) {
            for (int j=0; j < k+1; j++) {
                dp[i][j] = -1;
            }
        }
        psa[0] = 0;
        for (int i=1; i < n+1; i++) {
            cin >> nums[i];
            psa[i] = psa[i-1] + nums[i];
        }
        cout << solve(1, k) << "\n";
    }
}