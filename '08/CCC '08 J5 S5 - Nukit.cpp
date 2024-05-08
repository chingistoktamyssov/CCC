#include <bits/stdc++.h>

using namespace std;

int n;
vector <vector<int>> moves {{2, 1, 0, 2}, {1, 1, 1, 1}, {0, 0, 2, 1}, {0, 3, 0, 0}, {1, 0, 0, 1}};
int dp[31][31][31][31];

int canWin(int a, int b, int c, int d) {
    if (a < 0 || b < 0 || c < 0 || d < 0) {
        return false;
    }
    if (dp[a][b][c][d] != -1) {
        return dp[a][b][c][d];
    }
    for (int i=0; i < 5; i++) {
        int a2 = moves[i][0];
        int b2 = moves[i][1];
        int c2 = moves[i][2];
        int d2 = moves[i][3];
        if (a-a2 >= 0 && b-b2 >= 0 && c-c2 >= 0 && d-d2 >= 0) {
            if (canWin(a-a2, b-b2, c-c2, d-d2) == false) {
                dp[a][b][c][d] = true;
                return true;
            }
        }
    }
    dp[a][b][c][d] = false;
    return false;
}


int main() {
    cin >> n;

    for (int i=0; i < n; i++) {
        int a, b, c, d;
        bool winner;
        cin >> a >> b >> c >> d;
        for (int w = 0; w < 31; w++) {
            for (int x = 0; x < 31; x++) {
                for (int y = 0; y < 31; y++) {
                    for (int z = 0; z < 31; z++) {
                        dp[w][x][y][z] = -1;
                    }
                }
            }
        }
        winner = canWin(a, b, c, d);
        if (winner == true) cout << "Patrick" << "\n";
        else cout << "Roland" << "\n";
    }
}